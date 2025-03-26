import cv2
import paho.mqtt.client as mqtt
import numpy as np
import base64

MQTT_BROKER = "192.168.254.106"
TOPIC_SUBSCRIBE = "capture/image"
TOPIC_PUBLISH = "image/data"

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker!")
    client.subscribe(TOPIC_SUBSCRIBE)

def on_message(client, userdata, msg):
    print("Capture request received...")
    
    # Capture Image
    cap = cv2.VideoCapture(0)  # Open webcam
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        _, buffer = cv2.imencode('.jpg', frame)
        image_base64 = base64.b64encode(buffer).decode()
        
        # Publish Image
        client.publish(TOPIC_PUBLISH, image_base64)
        print("Image published successfully!")
    else:
        print("Failed to capture image.")

# MQTT Client Setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, 1883, 60)

client.loop_forever()
