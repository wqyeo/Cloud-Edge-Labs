import time
import torch
import numpy as np
from torchvision import models, transforms
from torchvision.models.quantization import MobileNet_V2_QuantizedWeights
import cv2
from PIL import Image
from torch.quantization import quantize_dynamic, get_default_qat_qconfig, prepare_qat, convert

# Webcam settings
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
cap.set(cv2.CAP_PROP_FPS, 36)

# Preprocessing
preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Select quantization method
QUANTIZATION_METHOD = "PTQ"  # Choose between "PTQ" or "QAT"

if QUANTIZATION_METHOD == "PTQ":
    # Post-Training Quantization (PTQ)
    print("Performing Post-Training Quantization...")
    net_fp32 = models.mobilenet_v2(pretrained=True)
    net = quantize_dynamic(net_fp32, {torch.nn.Linear}, dtype=torch.qint8)
    print("PTQ Model:", net)

elif QUANTIZATION_METHOD == "QAT":
    # Quantization Aware Training (QAT)
    print("Preparing for Quantization Aware Training...")
    net_fp32 = models.mobilenet_v2(pretrained=True)

    # Fuse layers (required for QAT)
    net_fp32.fuse_model()

    # Set QAT configuration
    net_fp32.qconfig = get_default_qat_qconfig('qnnpack')
    net_qat = prepare_qat(net_fp32)
    print("QAT Model Prepared for Training")

    # Simulate fine-tuning with dummy data
    optimizer = torch.optim.SGD(net_qat.parameters(), lr=0.001)
    dummy_input = torch.randn(4, 3, 224, 224)  # Batch of 4 images
    dummy_target = torch.randint(0, 1000, (4,))  # Dummy targets

    print("Fine-tuning QAT Model...")
    for epoch in range(5):
        optimizer.zero_grad()
        output = net_qat(dummy_input)
        loss = torch.nn.CrossEntropyLoss()(output, dummy_target)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch + 1}: Loss = {loss.item()}")

    # Convert QAT model to quantized version
    net = convert(net_qat.eval())
    print("QAT Model Converted to Quantized Version")

# Get class names (categories)
weights = MobileNet_V2_QuantizedWeights.DEFAULT
classes = weights.meta["categories"]

# Start inference loop
print("Starting inference...")
started = time.time()
last_logged = time.time()
frame_count = 0

with torch.no_grad():
    while True:
        # Read frame from webcam
        ret, image = cap.read()
        if not ret:
            raise RuntimeError("Failed to read frame from webcam.")

        # Convert BGR (OpenCV) to RGB
        image = image[:, :, [2, 1, 0]]

        # Preprocess image
        input_tensor = preprocess(image)
        input_batch = input_tensor.unsqueeze(0)

        # Run inference
        output = net(input_batch)

        # Get top predictions
        top = list(enumerate(output[0].softmax(dim=0)))
        top.sort(key=lambda x: x[1], reverse=True)

        print("Top Predictions:")
        for idx, val in top[:5]:  # Show top 5 predictions
            print(f"{val.item() * 100:.2f}% {classes[idx]}")
        print("=" * 72)

        # Log performance
        frame_count += 1
        now = time.time()
        if now - last_logged > 1:
            fps = frame_count / (now - last_logged)
            print(f"FPS: {fps:.2f}")
            last_logged = now
            frame_count = 0
