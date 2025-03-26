# Edge Analytics – Audio
## Table of Contents

1. [Why Audio Analytics on the Edge](#why-audio-analytics-on-the-edge)
2. [Applications of Audio Analytics on Edge](#applications-of-audio-analytics-on-edge)
3. [Fundamentals of Sound and Digitization](#fundamentals-of-sound-and-digitization)
4. [Pre-processing and Feature Extraction](#pre-processing-and-feature-extraction)
5. [Time Domain and Frequency Domain Features](#time-domain-and-frequency-domain-features)
6. [Time-Frequency Analysis and Spectrograms](#time-frequency-analysis-and-spectrograms)
7. [Mel-Scale and MFCC](#mel-scale-and-mfcc)
8. [Low-Cost Audio Analytics and State-of-the-Art](#low-cost-audio-analytics-and-state-of-the-art)
9. [Building Your Own Model & Cloud-to-Edge Scalability](#building-your-own-model-cloud-to-edge-scalability)
10. [Summary and Demo](#summary-and-demo)

---

## 1. Why Audio Analytics on the Edge

- **Low Latency:**  
  Fast response is critical for applications such as audio scene classification.
- **Data Sensitivity and Security:**  
  Many applications require audio data to remain secure and locally processed.
- **Data Redundancy Reduction:**  
  Compression and selective analysis allow for efficient offline processing.

---

## 2. Applications of Audio Analytics on Edge

- **Audio Scene Classification:**  
  Useful in surveillance and environmental monitoring.
- **Audio Event Detection:**  
  For example, detecting screeching brakes or other unusual sounds.
- **Speaker/Speech Recognition:**  
  Including keyword recognition and converting speech to text (and vice versa).
- **Conversational User Interfaces (CUI):**  
  Enabling real-time voice interactions.

---

## 3. Fundamentals of Sound and Digitization

### Introduction to Sound Waves

- **Sound Wave Equation:**  
  \( y(t) = A \sin(2\pi f t + \phi) \)  
  where:  
  - \(A\) is the amplitude  
  - \(f\) is the frequency  
  - \(t\) is time  
  - \(\phi\) is the phase

- **Key Concepts:**  
  - **Compression and Rarefaction:** The alternating regions of high and low pressure in a sound wave.
  - **Amplitude and Frequency:**  
    - Amplitude corresponds to sound intensity.  
    - Frequency determines the pitch.

### Digitization of Sound

- **Analog-to-Digital Conversion:**  
  - **Sampling:**  
    The sampling frequency should be greater than twice the maximum frequency of interest (Nyquist Criterion). Typical sound cards support up to 48 kHz.
  - **Quantization:**  
    Higher bit resolution provides better fidelity.

---

## 4. Pre-processing and Feature Extraction

- **Pre-processing Steps:**
  - **Noise Reduction:**  
    Removing background noise and artefacts.
  - **Standardization:**  
    Converting different formats, sampling rates, and handling varying lengths.
  - **Normalization:**  
    Adjusting for varying signal amplitudes to improve model performance.

---

## 5. Time Domain and Frequency Domain Features

### Time Domain Features

- **Amplitude Envelope:**  
  Represents the overall shape of the sound amplitude over time.
- **Root Mean Square (RMS):**  
  \( \text{RMS}_k = \sqrt{\frac{1}{K} \sum_{k-\frac{K}{2}}^{k+\frac{K}{2}} s(k)^2} \)  
  Useful for estimating energy while being less sensitive to outliers.
- **Zero Crossing Rate (ZCR):**  
  \( \text{ZCR}_k = \frac{1}{2} \sum_{k-\frac{K}{2}}^{k+\frac{K}{2}} \left| \text{sgn}(s_k) - \text{sgn}(s_{k+1}) \right| \)  
  Indicates the rate at which the signal changes sign; useful in pitch estimation and segmentation.

### Frequency Domain Features

- **Discrete Fourier Transform (DFT):**  
  Calculated using the Fast Fourier Transform (FFT):  
  $$ X_k = \sum_{n=0}^{N-1} x_n \exp\left(-i\frac{2\pi k}{N}n\right) $$
  Helps identify which frequencies are present in the signal.
- **Spectral Features:**  
  - **Spectral Centroid:**  
    Represents the “center of gravity” of the spectrum (brightness of sound).  
  - **Spectral Contrast:**  
    Compares energy differences between low and high frequency bands, useful for music/speech discrimination.

---

## 6. Time-Frequency Analysis and Spectrograms

- **Short Time Fourier Transform (STFT):**  
  - **Process:**
    1. Divide the signal into overlapping time windows.
    2. Compute FFT for each window (often using a decaying window function like a Gaussian).
    3. Stack the results to form a spectrogram.
    4. Apply logarithmic scaling (in dB) to highlight subtle changes.
  - **Spectrogram Equation:**  
    $$ S_{k,m} = 20 \log_{10} \left| \sum_{n=0}^{N_w-1} x_n \, w_m(n) \exp\left(-i\frac{2\pi k}{N} n\right) \right| $$

- **Visual Representations:**  
  Spectrograms show how frequency content evolves over time.

---

## 7. Mel-Scale and MFCC

### Mel-Spectrograms

- **Perceptual Scale:**  
  Humans perceive pitch on a logarithmic scale; the mel scale reflects this perceptual property.
- **Mel Scale Conversion:**  
  $$ \text{mel}(f) = 2595 \log_{10}\left(1 + \frac{f}{700}\right) $$
- **Comparison:**  
  Changes in linear frequency versus mel frequency illustrate the non-linear human perception of sound.

### Mel Frequency Cepstral Coefficients (MFCC)

- **Definition:**  
  MFCCs are obtained by applying the Discrete Cosine Transform (DCT) to the log mel-spectrogram. They provide a compact representation of the timbre of a sound.
- **Significance:**  
  Widely used in machine learning for audio tasks because they reduce redundancy and focus on perceptually important aspects.

---

## 8. Low-Cost Audio Analytics and State-of-the-Art

### Low-Cost Audio Analytics Pipeline

- **Features Utilized:**
  - Time-domain: Amplitude Envelope, Zero Crossing Rate, RMS.
  - Frequency-domain: Spectral Centroid, Spectral Contrast.
  - Time-Frequency: Spectrograms, MFCC.
- **Machine Learning Tasks:**  
  Combining these features with simple models for tasks such as audio event detection and classification.

### State-of-the-Art Models

- **YAMNet:**  
  A deep convolutional neural network based on MobileNet v1 that predicts 521 audio event classes from the AudioSet-YouTube corpus.  
  [TensorFlow Hub Tutorial on YAMNet](https://www.tensorflow.org/hub/tutorials/yamnet)
- **conv-SPAD:**  
  A custom convolutional model for spectral audio-based anomaly detection, as presented by Lo Scudo et al. (2023).

---

## 9. Building Your Own Model & Cloud-to-Edge Scalability

### Building Your Own Audio Analytics Model

- **Pipeline Steps:**
  1. **Pre-processing:** Noise reduction, normalization, segmentation.
  2. **Feature Extraction:** Compute spectrograms and MFCCs.
  3. **Model Selection:**  
     Options include CNNs, RNNs, Transformers, and transfer learning approaches.
  4. **Data Sources:**  
     Datasets such as TAU Urban Acoustic Scenes, TUT Rare Sound Events, LibriSpeech, and AudioSet.

### Cloud-to-Edge Strategy for Scalability

- **Edge Device Responsibilities:**
  - Pre-processing, feature extraction, and ML inference.
- **Cloud Responsibilities:**
  - Data storage, model training, and model trimming.
- **Examples of Platforms:**
  - **Edge Impulse**, various cloud-based speech processing services (AWS Transcribe, Google Cloud Text-to-Speech, etc.), and APIs (Azure, IBM Watson).

---

## 10. Summary and Demo

- **Key Takeaways:**
  - **Audio Analytics on the Edge:**  
    Enables faster responses, better data security, and efficient analysis.
  - **Importance of Pre-processing:**  
    Critical for noise reduction and normalization.
  - **Feature and Model Selection:**  
    The choice of features (time, frequency, time-frequency) and models is crucial.
  - **Scalability:**  
    Building in the cloud and adapting to the edge allows for scalable and cost-effective solutions.

- **Demo:**  
  Try the demo at [Edge Audio Analytics](https://edgeaudioanalytics.streamlit.app/)
