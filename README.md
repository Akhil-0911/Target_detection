# 🛡️ **Smart Surveillance System using YOLOv8s** 🎥

## **1. Introduction** 📝

### **1.1 Problem Statement** ⚠️
Surveillance systems play a critical role in security, but traditional systems often lack advanced object detection capabilities, making them inefficient for monitoring complex environments. This project aims to develop a **smart surveillance system** using **YOLOv8s (You Only Look Once, Version 8 Small)**, a state-of-the-art object detection model, to detect and classify objects in real-time from video footage or live SSTV camera streams.

### **1.2 Motivation** 💡
Traditional surveillance systems are often limited by outdated technology and manual monitoring. With **YOLOv8s**, a highly efficient and accurate object detection model, this project aims to provide a solution for real-time detection, reducing human error and increasing the efficiency of security monitoring.

### **1.3 Objectives** 🎯
- Implement a **real-time smart surveillance system** using **YOLOv8s**.
- Enable detection of various objects (e.g., people, vehicles, animals) from video footage or SSTV camera input.
- Improve monitoring efficiency with **automated detections** and alerts.

### **1.4 Scope of the Project** 🌍
- The system will focus on **real-time detection of objects**.
- This solution will be designed for **general surveillance**, not specialized for a single type of object.
- The system will work with **video files** as well as live **SSTV camera streams**.

---

## **2. System Design & Implementation** 🖥️

### **2.1 Architecture** 🏗️
The system uses **YOLOv8s** for **real-time object detection** in video streams. It works with both pre-recorded video files and live video feeds from an **SSTV camera**.

**Step-by-step Process:**
1. **Load YOLOv8s pretrained model**.
2. **Accept video input** either from SSTV camera or a video file.
3. **Process each video frame** through YOLOv8s for object detection.
4. **Display detected objects** in real-time with bounding boxes and labels.
5. Optionally, **save the annotated video** for later review.

---

### **2.2 How to Clone and Run the Project Locally** 🛠️

To set up and run the **Smart Surveillance System** on your local machine, follow these steps:

1. **Clone the Repository** 📥
   git clone https://github.com/your-username/smart-surveillance-yolov8s.git
   cd smart-surveillance-yolov8s
   
2. **Create and Activate a Virtual Environment 🌱 (Recommended)**
python -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate         # For Windows

3, **Install Required Packages 📦**
pip install -r requirements.txt

4. **Run the Surveillance Script 🎬**

- For video detection:
    python detect_video.py

- For live camera stream (SSTV camera, adjust the camera index as needed):
    python detect_video.py --source 0

5.  **View Output** 👀

- The system will display detected objects in **real-time**.
- Optionally, the annotated video will be saved in the **output/** directory.

---

## **3. Requirements** ⚙️

### **3.1 Hardware Requirements** 💻
- **Processor**: Intel i5/i7 or AMD equivalent
- **RAM**: Minimum 8GB (16GB recommended for deep learning)
- **Storage**: At least 50GB of free space
- **GPU**: NVIDIA GTX 1650 or higher (optional but recommended)

### **3.2 Software Requirements** 🖥️
- **Frontend**: HTML, CSS (for UI, if needed)
- **Backend**: Python (Flask/Django for integration)
- **Libraries**:
  - TensorFlow, PyTorch (for Deep Learning)
  - OpenCV, PIL (for image processing)
  - NumPy, Pandas (for data handling)
- **Operating System**: Windows 10/11, Ubuntu 20.04+, macOS

---

## **4. Model Implementation & Results** 🔬

### **4.1 Model Selection** 🧠
- **YOLOv8s**: A lightweight and efficient version of YOLO that provides fast and accurate object detection in real-time, suitable for embedded systems and low-power devices.

### **4.2 Model Training & Testing** 🏋️‍♂️
- **Datasets Used**:
  - COCO Dataset (Common Objects in Context) for object detection.
  
- **Performance Metrics**:
  - **Precision**, **Recall**, **F1-Score** for evaluating object detection accuracy.

### **4.3 Results & Observations** 📊
- The system performed well on both **video files** and live **SSTV camera feeds**.
- **Real-time object detection** achieved high accuracy with bounding boxes and labels correctly identifying objects in various video scenarios.

---

## **5. Discussion and Conclusion** 💬

### **5.1 Future Work** 🚀
- Implement **multi-object tracking** for continuous monitoring of detected objects.
- Explore integrating additional **camera feeds** or **IoT devices** for enhanced surveillance coverage.
- Improve system performance on lower-end hardware by optimizing the model further.

### **5.2 Conclusion** 🎯
The **Smart Surveillance System** successfully utilizes **YOLOv8s** for **real-time object detection**. The system can be used for efficient surveillance, reducing the need for constant human monitoring. With further optimization and feature additions, it has the potential to be used in **commercial** and **home security applications**.
