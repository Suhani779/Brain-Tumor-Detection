# 🧠 Brain Tumor Detection Using Deep Learning

An **AI-based Brain Tumor Detection System** that automatically detects and classifies brain tumors from MRI images using **Deep Learning and Transfer Learning (VGG16)**.  
The system is deployed as a **Flask web application** for real-time MRI image prediction.

---

## 📌 Project Overview
Brain tumor detection from MRI scans is a critical task in medical diagnosis. Manual analysis of MRI images is time-consuming and may lead to human errors.  
This project uses **Convolutional Neural Networks (CNNs)** with **Transfer Learning** to build an automated, accurate, and efficient brain tumor classification system.

---

## 🧪 Tumor Classes
The model classifies MRI images into the following categories:
- 🟣 Glioma  
- 🔵 Meningioma  
- 🟡 Pituitary Tumor  
- 🟢 No Tumor  

---

## 🚀 Features
- ✅ Automated brain tumor detection from MRI images  
- ✅ Multi-class classification  
- ✅ Transfer Learning using VGG16  
- ✅ High accuracy (~95%)  
- ✅ Performance evaluation using confusion matrix and ROC curve  
- ✅ Web-based deployment using Flask  
- ✅ Simple and user-friendly interface  

---

## 🛠️ Tech Stack

### 🔹 Programming & Frameworks
- Python  
- TensorFlow & Keras  
- Flask  

### 🔹 Libraries
- NumPy  
- Matplotlib  
- Scikit-learn  
- PIL (Image Processing)  

### 🔹 Tools
- Google Colab  
- Jupyter Notebook  
- HTML (Frontend)  

---

## 🧠 Model Architecture
- Pre-trained **VGG16** model (ImageNet weights)  
- Frozen base layers with fine-tuning of last layers  
- Flatten layer  
- Dense layer with ReLU activation  
- Dropout layers to prevent overfitting  
- Softmax output layer for multi-class classification  

---

## ⚙️ Workflow
1. 📂 Load MRI Dataset  
2. 📊 Data Visualization  
3. 🧹 Image Preprocessing & Augmentation  
4. 🔁 Transfer Learning using VGG16  
5. 🏗️ Model Building & Training  
6. 📈 Training & Validation Analysis  
7. 📋 Evaluation (Classification Report, Confusion Matrix, ROC Curve)  
8. 🧪 MRI Image Detection System  
9. 🌐 Deployment using Flask Web Application  

---

## 📈 Results
- Training Accuracy: ~97%  
- Testing Accuracy: ~95%  
- Strong classification performance across all tumor classes  
- Reliable predictions with confidence scores  

---

## 🖼️ Output
- Displays uploaded MRI image  
- Shows detected tumor type  
- Displays confidence percentage of prediction  

---

## 🌐 Web Application
- Upload MRI image through browser  
- Click predict button  
- View tumor detection result instantly  
- Backend handled using Flask  
- Frontend designed with HTML  

