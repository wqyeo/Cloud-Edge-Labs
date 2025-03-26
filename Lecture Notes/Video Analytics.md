# Edge Analytics – Image and Video
## Table of Contents

1. [Overview and Applications](#overview-and-applications)
2. [Image/Video Acquisition and Formation](#imagevideo-acquisition-and-formation)
3. [Image Preprocessing Techniques](#image-preprocessing-techniques)
4. [Image Feature Extraction](#image-feature-extraction)
   - [Edge and Corner Detection](#edge-and-corner-detection)
   - [Histogram of Oriented Gradients (HOG)](#histogram-of-oriented-gradients-hog)
   - [Texture Features – Local Binary Patterns (LBP)](#texture-features-local-binary-patterns-lbp)
5. [Video Analytics and Motion Estimation](#video-analytics-and-motion-estimation)
   - [Optical Flow](#optical-flow)
   - [Landmark Detection](#landmark-detection)
6. [Low-Compute Analytics & State-of-the-Art Models](#low-compute-analytics--state-of-the-art-models)
7. [Building Models and Cloud-to-Edge Scalability](#building-models-and-cloud-to-edge-scalability)
8. [Summary and Demo](#summary-and-demo)

---

## 1. Overview and Applications

- **Image/Video Analytics Applications:**
  - **Scene Classification:** (e.g., surveillance)
  - **Scene Segmentation & Detection:** (e.g., traffic scene analysis)
  - **Human–Computer Interaction:**  
    - Hand gesture recognition  
    - Facial landmark detection
  - **Video Summarization** and **Motion/Depth Estimation**

- **Content Focus:**
  - Acquisition parameters, feature extraction (edges, shapes, textures), landmark detection, motion estimation, and lightweight machine learning for image/video analytics.

---

## 2. Image/Video Acquisition and Formation

### Image Formation

- **Spatial Resolution:**  
  Number of pixels per area.
  
- **Intensity Resolution:**  
  Number of intensity levels (bits). For instance, a *uint8* image represents 256 levels.

- **Dots Per Inch (dpi):**  
  Measures the density (pixels per inch).

### Histogram of an Image

- **Definition:**  
  The histogram \( h(D) \) is defined as the number of pixels in an image \( I(x,y) \) that have intensity \( D \) (with \( D \in \{0, 2^L-1\} \) for an \( L \)-bit image):
  $$
  h(D) = \sum_{x=0}^{M-1}\sum_{y=0}^{N-1} \mathbf{1}\{I(x,y) == D\}
  $$

### Image Contrast

- Contrast can vary from low to high, affecting the visibility of details in dark or bright areas.

---

## 3. Image Preprocessing Techniques

### Contrast Stretching

- **Purpose:**  
  Enhance the contrast of a low-contrast image.
  
- **Example Transformation:**  
  For an 8-bit image, a simple linear transformation might be:
  $$
  J(x,y) = 255 \cdot \frac{I(x,y) - L}{H - L}
  $$
  where \( L \) and \( H \) represent the low and high intensity limits.

### Histogram Equalization

- **Steps:**
  1. Compute the normalized histogram.
  2. Use the cumulative histogram as a transfer function to equalize the image intensity distribution.

### Filtering

- **Techniques:**
  - **Median Filter:** Removes noise while preserving edges.
  - **Gaussian Filter:** Smoothens the image.
  - **Filter Subtraction:** Enhances features by subtracting the filtered image from the original.

*Note:* Preprocessing can be performed on edge devices to reduce data before further analysis.

---

## 4. Image Feature Extraction

### Edge and Corner Detection

#### Canny Edge Detection

- **Steps:**
  1. Smoothing (using a Gaussian filter)
  2. Compute gradients:  
     \( M(x,y) = \sqrt{g_x^2 + g_y^2} \)  
     \( \alpha(x,y) = \tan^{-1}\left(\frac{g_y}{g_x}\right) \)
  3. Non-maxima suppression (phase-driven)
  4. Double thresholding and hysteresis

#### Harris Corner Detection

- **Concept:**  
  Uses gradient information to detect corners based on the local auto-correlation matrix:
  $$
  R = AB - C^2 - k (A+B)^2
  $$
  where \( A = (d_x)^2 \), \( B = (d_y)^2 \), and \( C = d_x d_y \).  
  A high response \( R \) indicates a corner.

### Histogram of Oriented Gradients (HOG)

- **Process:**
  - Compute gradient magnitude and orientation for each pixel.
  - Consider a small window (e.g., \(8 \times 8\)) and form a histogram for predefined orientation bins (e.g., 0°, 20°, …, 160°).
  - Normalize and concatenate histograms across the image to create a feature vector.
  
- **Reference:**  
  Dalal and Triggs, 2005.

### Texture Features – Local Binary Patterns (LBP)

- **Concept:**  
  LBP encodes the local texture by thresholding a pixel’s neighborhood and forming a binary number.
- **Usage:**  
  Effective for rotation-invariant texture classification.

---

## 5. Video Analytics and Motion Estimation

### Optical Flow – Motion Estimation and Tracking

- **Applications:**  
  - Optical mouse, traffic monitoring, image stabilization, hand/face tracking.
- **Concept:**  
  Optical flow captures the pattern of apparent motion between two frames.  
  **Lucas-Kanade Method:**  
  Solves for velocity \( \mathbf{v} = (v_x, v_y) \) using local gradients:
  $$
  \mathbf{v} = (A^T A)^{-1} A^T \mathbf{b}
  $$
  where \( A \) is built from image gradients \( I_x \) and \( I_y \) and \( \mathbf{b} \) from temporal gradient \( I_t \).

### Landmark Detection

#### Hand-Landmark Detection

- **Approach:**  
  Real-time hand tracking using lightweight models as demonstrated in Google’s MediaPipe.

#### Face-Landmark Detection

- **Approach:**  
  Uses similar techniques for detecting facial features (facial landmarks) with applications in human–computer interaction.

---

## 6. Low-Compute Analytics & State-of-the-Art Models

- **Low-Compute Strategies:**
  - Use texture, gradient, and shape features.
  - Apply machine learning models on these features for tasks such as object detection and video summarization.

- **State-of-the-Art Example: YOLOv11**
  - **YOLOv11:**  
    A lightweight model capable of object classification, detection (including oriented detection), instance segmentation, and pose estimation.
  - **Resources:**  
    [YOLOv11 Explained](https://medium.com/@nikhil-rao-20/yolov11-explained-next-level-object-detection-with-enhanced-speed-and-accuracy-2dbe2d376f71) and [Ultralytics YOLOv11 Documentation](https://docs.ultralytics.com/models/yolo11/)

---

## 7. Building Models and Cloud-to-Edge Scalability

### Building Your Own Model

- **Pipeline:**
  1. **Pre-processing:**  
     Normalization, segmentation, filtering.
  2. **Feature Extraction:**  
     Extract features such as edges, histograms, LBP, etc.
  3. **Model Selection:**  
     Consider CNNs, Transformers, or transfer learning.
  4. **Datasets:**  
     Examples include COCO, ImageNet, Open Images Dataset, PASCAL VOC, YouTube-8M, UCF-101, Kinetics, HMDB51, and Charades.

### Cloud-to-Edge Strategy

- **Edge Device Tasks:**  
  - Pre-processing, feature extraction, and machine learning inference.
- **Cloud Tasks:**  
  - Data storage, model training, and model trimming.
- **Example Platforms:**  
  Edge Impulse, AWS Rekognition, Google Cloud Vision API, IBM Watson Visual Recognition, Azure AI Vision.

---

## 8. Summary and Demo

- **Key Takeaways:**
  - Image/video analytics on edge provide faster response times, enhanced data security, and improved analysis.
  - Preprocessing (contrast stretching, histogram equalization, filtering) is critical.
  - Proper feature extraction (edges, corners, HOG, LBP) and model selection (e.g., YOLOv11) are vital.
  - A cloud-to-edge strategy supports scalability while handling resource constraints on edge devices.

- **Demo:**  
  Explore a live demo at [Edge Image Analytics](https://edgeimageanalytics.streamlit.app/) 