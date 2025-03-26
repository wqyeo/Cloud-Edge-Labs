# Deployment on Edge Devices  
## Table of Contents

1. [Motivation - The Need for Optimisation](#motivation-the-need-for-optimisation)
2. [Deployment Optimisation Process](#deployment-optimisation-process)
3. [Advanced Profiling Techniques](#advanced-profiling-techniques)
4. [Case Studies](#case-studies)
   - [CPU & Memory Bottleneck Analysis](#cpu-memory-bottleneck-analysis)
   - [Smart Camera for Object Detection](#smart-camera-for-object-detection)
   - [Industrial Sensor Network](#industrial-sensor-network)
   - [Autonomous Drone Navigation](#autonomous-drone-navigation)
   - [Smart Security Camera with Motion-Activated Object Detection](#smart-security-camera-with-motion-activated-object-detection)
   - [Smart Home Camera Performing Real-Time Face Recognition](#smart-home-camera-performing-real-time-face-recognition)
   - [Smart Farm with Adaptive Crop Monitoring](#smart-farm-with-adaptive-crop-monitoring)
5. [Dynamic and Adaptive Scheduling](#dynamic-and-adaptive-scheduling)
6. [Advanced Optimisation Techniques](#advanced-optimisation-techniques)
7. [Future Trends](#future-trends)
8. [Summary](#summary)

---

## 1. Motivation - The Need for Optimisation

- **Aspect-Based Optimisation:**
  - **Model-Centric Optimisation** focuses on neural network architecture and parameters to reduce model size, complexity, and computation.
  - **System-Level Optimisation** targets hardware, OS, memory, and data movement to maximize hardware utilization and system efficiency.

- **Objective:**
  - Reduce model size, complexity, and computation to lower memory and computational costs.
  - Maximize hardware utilization for faster and more efficient inference.

- **Techniques:**
  - **Model-Centric:** Pruning, Quantization, Knowledge Distillation, NAS.
  - **System-Level:** I/O Optimization, Memory Management, Scheduling.

---

## 2. Deployment Optimisation Process

- **Steps:**
  - **Profiling:** Analyze performance and resource utilization.
  - **Analysing:** Identify bottlenecks like CPU/GPU utilization, memory/I/O, OS-level issues.
  - **Scheduling:** Optimize task scheduling, model partitioning, and adaptive precision.
  - **Optimisation:** Use hardware acceleration, code optimization, and graph optimization to minimize power usage and improve computation.

---

## 3. Advanced Profiling Techniques

- **Model Performance Analysis:**  
  Use tools like TensorBoard Profiler and NVIDIA Nsight Systems to analyze layer-wise execution time and memory usage, identifying bottlenecks.

- **Memory Analysis:**  
  Tools like Valgrind's Cachegrind and ARM Streamline analyze memory access patterns to optimize data locality and cache usage.

- **Power Profiling:**  
  Measure power consumption using ARM Energy Probe and Intel Power Gadget to optimize energy usage in battery-powered devices.

- **System-Level Profiling:**  
  Tools like `perf` provide insights into CPU cycles, instructions, cache misses, and branch mispredictions for optimizing hardware behavior.

- **Network Profiling:**  
  Capture and analyze network traffic with tcpdump and Wireshark to identify network-related performance issues in edge-cloud communication.

---

## 4. Case Studies

### CPU & Memory Bottleneck Analysis

- **Tools Used:** `perf` profiling tool on a Raspberry Pi 4 for object detection model inference.
- **Key Insights:**  
  - Low Instruction Per Cycle (IPC) suggests CPU bottlenecks.
  - Cache misses point to memory bottlenecks.
  - Branch misses indicate inefficiencies in control flow.
  
- **Optimization Actions:**
  - Improve memory access patterns to optimize cache usage.
  - Refactor loops and branches to reduce branch mispredictions.

### Smart Camera for Object Detection

- **Bottleneck:** High latency in transmitting results to the cloud.
- **Solution:**  
  - **Edge-Cloud Partitioning:** Move critical detection logic to the edge, sending summarized alerts to the cloud.
  - **Protocol Optimization:** Switch from HTTP to MQTT for faster communication.

### Industrial Sensor Network

- **Bottleneck:** Delays in aggregating and processing data from sensors.
- **Solution:**  
  - Implement memory pooling to reduce memory allocation overhead.
  - Use layer fusion to minimize data movement.
  - Introduce concurrency optimizations through asynchronous data processing.

### Autonomous Drone Navigation

- **Bottleneck:** GPU overload, CPU underutilization.
- **Solution:**  
  - **Load Balancing:** Offload pre-processing tasks to CPU to optimize GPU usage for model inference.
  - **Heterogeneous Computing:** Integrate an NPU for lightweight tasks.

---

## 5. Dynamic and Adaptive Scheduling

### Techniques:

- **Dynamic Task Scheduling:**  
  Dynamically assigns tasks to CPU, GPU, or NPU based on resource availability. Example: Work-stealing algorithms and priority-based scheduling.

- **Adaptive Model Partitioning:**  
  Split model execution across devices (edge and cloud) and adapt based on network latency and system conditions. Example: Neurosurgeon Framework.

- **Adaptive Resource Allocation:**  
  Allocates resources dynamically to tasks based on system load, ensuring optimal resource usage and system responsiveness.

---

## 6. Advanced Optimisation Techniques

### Techniques:

- **Hardware Acceleration:**  
  Use domain-specific accelerators (e.g., TPUs, NPUs, FPGAs) to speed up ML computations. Example: Google Edge TPU, NVIDIA TensorRT.

- **Code Optimization:**  
  Use techniques like kernel optimization, loop unrolling, and vectorization to improve execution speed and reduce memory usage. Tools like LLVM and GCC compilers help in low-level optimization.

- **Graph-Level Optimization:**  
  Rearranging computation graphs for better memory and computation efficiency. Tools like TensorFlow XLA and TVM are commonly used for this.

---

## 7. Future Trends

### Emerging Trends in Edge Computing:

- **AI-Driven Optimization:**  
  Machine learning algorithms dynamically adjust system parameters and model architectures, providing real-time optimization. Example: Google AutoML.

- **Dynamic and Adaptive Allocation:**  
  AI-driven scheduling optimizes resource allocation based on real-time demands, reducing latency and cost.

- **Cross-Layer Optimization:**  
  Optimizing across hardware, runtime, compiler, and application layers for holistic system performance. Example: TVM Compiler, Google Edge TPU Compiler.

- **Collaborative & Federated Optimization:**  
  Distributed optimization while maintaining data privacy. Example: Google Federated Learning, OpenMined PySyft.

---

## 8. Summary

- **Key Takeaways:**
  - **Profiling and System Analysis** help identify bottlenecks and guide optimization strategies.
  - **Dynamic Scheduling** and **Adaptive Resource Allocation** improve resource utilization and reduce latency.
  - **Advanced Optimization Techniques** such as hardware acceleration, code optimization, and graph-level optimization enhance performance on edge devices.
  - The **Future of Edge Computing** will involve AI-driven optimization, dynamic resource management, and collaborative learning approaches.
