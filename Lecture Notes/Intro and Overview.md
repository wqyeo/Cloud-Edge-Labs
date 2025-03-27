# Introduction to Edge Computing and Analytics

## Table of Contents

1. [Cloud Computing Foundations](#cloud-computing-foundations)
2. [Edge Computing Fundamentals](#edge-computing-fundamentals)
3. [Architectures, Definitions, and Key Mappings](#architectures-definitions-and-key-mappings)
4. [Applications and Real-World Use Cases](#applications-and-real-world-use-cases)
5. [Hardware, Networking, and Software Technologies](#hardware-networking-and-software-technologies)
6. [Analytics, AIoT, and Data Processing at the Edge](#analytics-aiot-and-data-processing-at-the-edge)
7. [Challenges, Design Considerations, and Future Trends](#challenges-design-considerations-and-future-trends)
8. [Summary](#summary)

---

## 1. Cloud Computing Foundations

### Introduction to Cloud Computing
- **Scalable Workload Management:**  
  Organisations shift from capital expenditures to operational expenses using pay-as-you-go models.  
  - Global access and rapid deployment are key.
- **Core Services Delivered:**  
  - **IaaS:** Infrastructure as a Service  
  - **PaaS:** Platform as a Service  
  - **SaaS:** Software as a Service
- **Deployment Models:**  
  Public, Private, and Hybrid Clouds.
- **Key Characteristics:**  
  - On-demand self-service  
  - Broad network access  
  - Resource pooling and elasticity  
  - Measured service

### Inherent Cloud Challenges
- **Latency & Bandwidth:**  
  Increased data transmission costs and unsuitability for time-sensitive applications.
- **Privacy & Regulatory Concerns:**  
  Risks due to off-premises storage and health or sensitive data regulations.
- **Connectivity & Control Issues:**  
  Dependence on internet connectivity, limited customisation, and vendor lock-in.

---

## 2. Edge Computing Fundamentals

### What is Edge Computing?
- **Definition:**  
  A distributed computing paradigm that brings computation and storage closer to where data is generated.
- **Key Benefits:**  
  - Reduces latency  
  - Improves response times  
  - Saves bandwidth

### A Changing World: The Need for Edge
- **Driving Forces:**  
  - More devices online generating vast data  
  - Increased demand for low latency  
  - Integration of machine learning in IoT  
  - Cheaper sensors and evolving data privacy regulations

### Evolution of Edge Computing
- From centralized cloud architectures to distributed edge deployments, paving the way for faster, localized data processing.

---

## 3. Architectures, Definitions, and Key Mappings

### Edge-Fog-Cloud Architecture
- **Overview:**  
  A multi-layered approach bridging the gap between centralized cloud and the physical edge.
- **Reference:**  
  Cao et al. (2019), *Analytics Everywhere: Generating Insights From the Internet of Things*  
  DOI: [10.1109/ACCESS.2019.2919514](https://doi.org/10.1109/ACCESS.2019.2919514)
- **Scalability:**  
  Scale from thousands to billions of devices.

### Diverse Definitions of Edge Computing
- **General:**  
  Processing data near its source to reduce latency and bandwidth.
- **NIST Perspective:**  
  Technologies enabling computation at the network’s edge for both IoT and cloud services.
- **Industry & Academic Views:**  
  Emphasize localized processing and distributed analytics for real-time responsiveness.

### Mapping Characteristics to Benefits
| **Characteristic**                     | **Benefit**                                         |
|----------------------------------------|-----------------------------------------------------|
| Local data processing                  | Low latency and real-time responses                 |
| Enhanced privacy (data remains local)  | Improved data security                              |
| Autonomous decisions                   | Increased responsiveness                            |
| Data filtering at the source           | Optimized bandwidth usage and reduced costs         |
| Resilience to network issues           | Greater reliability, with offline functionality     |
| Adaptation to resource constraints     | Energy and cost efficiency                          |
| Handling heterogeneous environments    | Scalability and flexibility                         |

---

## 4. Applications and Real-World Use Cases

### Illegal Parking Detection
- **Use Case:**  
  Vehicle localization, tracking, evidence collection, and image pre-processing.
- **Workflow:**  
  Involves classification (bus, car), background modeling, and foreground detection.

### Smart Manufacturing Examples
- **Airbus – Factory of the Future:**  
  - **MiRA Tablet:** A hybrid sensor and tablet for smart manufacturing.
  - **Internet-Connected Tools:** Auto-adjust to sensor inputs, reducing assembly time.
  - **Augmented Reality:** Enhanced instructional tutorials.
  - **Additional Innovations:**  
    Active RFID tags, geolocation, and collaborative robots for risk reduction.
- **Continental AG’s SMART Factory:**  
  Emphasizes asset tracking, just-in-time inventory management, and quality control.

---

## 5. Hardware, Networking, and Software Technologies

### Edge Devices & Platforms
- **CPU-Centric Devices:**  
  - Examples: Odroid N2+ (6-core CPU), Raspberry Pi 4.
- **GPU-Centric Devices:**  
  - **NVIDIA Jetson Series:**  
    Models include Jetson Nano, TX2 Series, Xavier NX, and AGX Xavier.
  - **Specifications:**  
    Varying GFLOPS/TFLOPS and TOPS, with advanced GPUs (e.g., NVIDIA Maxwell, Pascal, Volta with Tensor Cores).

### Networking in Edge Computing
- **Data Projections:**  
  IDC estimates by 2025, 41.6 billion connected IoT devices will generate roughly 79.4 zettabytes of data.
- **Local Connectivity:**  
  Protocols such as ZigBee, Z-Wave, and Wi-Fi connecting devices to gateways.
- **Cloud Connectivity:**  
  Options include LTE, emerging 5G, and other long-range protocols based on bandwidth needs.

### Software and Technologies at the Edge
- **Key Technologies:**  
  - **Fog Computing**
  - **Containerisation:** Docker  
  - **Orchestration:** Kubernetes for deployment and scaling  
  - **Fleet Management:** Tools like Balena

---

## 6. Analytics, AIoT, and Data Processing at the Edge

### Introduction to Edge Analytics
- **Local Data Processing:**  
  Analyses data where it is generated, reducing latency and bandwidth needs.
- **Edge vs. Traditional Analytics:**  
  Emphasizes real-time decision-making compared to slower centralized processing.

### AIoT: Fusion of AI and IoT
- **Definition:**  
  Combines AI with IoT devices for on-device data analysis.
- **Key Aspects:**  
  - Embedded AI capabilities  
  - Real-time decision-making  
  - Self-learning and adaptive systems  
  - Predictive maintenance; note that typically only inference is performed on edge devices while training remains offline.

### EDGE AI Ecosystem
- **Deep Neural Network Architectures:**  
  - Classification (e.g., VGG, MobileNet, SqueezeNet)  
  - Object detection (e.g., Faster R-CNN, YOLO, SSD)
- **Frameworks and Libraries:**  
  - Training and inference frameworks (Caffe, PyTorch, TensorFlow, MXNet, Darknet)  
  - Inference-optimized frameworks (TensorFlow Lite, NCNN, PyTorch Mobile)  
  - Hardware programming: CUDA, OpenCL, cuDNN; multi-core processing with OpenMP and NEON.
- **SoC Families:**  
  Hisilicon Kirin, Samsung Exynos, Qualcomm Snapdragon, NVIDIA Jetson, Apple Bionic.

### Data Processing Challenges in Action
- **Thermal and Environmental Considerations:**  
  For instance, CPU temperatures can exceed 85°C on a sunny day even with ventilation, highlighting the need for robust thermal designs.

---

## 7. Challenges, Design Considerations, and Future Trends

### Challenges in Edge Computing
- **Security:**  
  Distributed processing introduces unique vulnerabilities.
- **Computational Limitations:**  
  Edge devices have less power compared to centralized data centers.
- **Data Management:**  
  Coordinating vast, distributed data remains complex.

### Design Considerations for the Edge
- **Resource Constraints:**  
  - **Memory:** Limited RAM and flash storage.
  - **Processing Power:** Need for low-complexity algorithms.
  - **Energy Consumption:** Critical for battery-powered devices.
  - **Data Types & Model Sizes:**  
    Often integer-only arithmetic and compact models (tens to hundreds of kilobytes).

### Additional Considerations
- Latency and response time  
- Scalability (both in device count and geographic distribution)  
- Security and privacy  
- Network connectivity and bandwidth  
- Data management and storage  
- Robustness and reliability  
- User experience  
- Regulatory compliance  
- Cost-effectiveness  
- Customization and flexibility

### Future Trends
- Evolving smart manufacturing, streamlined factories, and enhanced inventory and quality control through sensor integration and automated alerts.
- Increasing demand for localized intelligence and AI-driven operational efficiency.

---

## 8. Summary

- **Edge Computing Overview:**  
  A distributed approach that processes data near its source to reduce latency and bandwidth requirements.
- **Integration with AIoT:**  
  Combining AI with IoT devices leads to real-time analytics, autonomous decision-making, and improved operational efficiency.
- **Architectures and Platforms:**  
  Covers everything from cloud foundations to heterogeneous edge devices, networking options, and software ecosystems.
- **Challenges and Future Outlook:**  
  Addressing security, computational limitations, and design constraints is crucial for advancing edge computing.