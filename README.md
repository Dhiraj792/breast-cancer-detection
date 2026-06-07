# breast-cancer-detection
### Click here: https://breast-cancer-detection-feqfsmmsgmczy3kaxyo24n.streamlit.app/#breast-cancer-detection
### dataset use for training and testing:https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset
# 🩺 Breast Cancer Detection using Deep Learning 🚀

This project is an AI-powered web application that detects **Breast Cancer** from **Histopathology Images** using Deep Learning.

The model predicts whether the uploaded image is:

* ✅ Benign
* ⚠️ Malignant

with confidence score and adjustable decision threshold.

The application is deployed live using **Streamlit** and provides an interactive interface for image-based cancer prediction.

---

# 🌐 Live Demo

🚀 Upload a histopathology image and get real-time prediction results.

Features:

* Image Upload
* AI-powered Prediction
* Confidence Score
* Adjustable Threshold
* Prediction Details

---

# 📌 Project Overview

Breast cancer is one of the most common cancers worldwide.

This project aims to assist in:

* Early detection
* Faster diagnosis support
* AI-assisted medical image analysis

using Deep Learning and Computer Vision techniques.

---

# 📂 Project Structure

```text id="2pc9vt"
Breast-Cancer-Detection/
│── app.py                         # Streamlit web application
│── breast_cancer_model_v3.keras   # Trained deep learning model
│── requirements.txt               # Required dependencies
│── test_images/                   # Sample histopathology images
│── README.md                      # Project documentation
```

---

# 🧠 Features

## 🔹 AI-Based Prediction

Classifies histopathology images into:

* Benign
* Malignant

---

## 🔹 Adjustable Decision Threshold

Users can change prediction threshold dynamically for better sensitivity control.

Example:

```text id="c6lx8q"
Threshold = 0.7
```

---

## 🔹 Confidence Score

Displays prediction confidence percentage.

Example:

```text id="jlwmwi"
Confidence: 100%
```

---

## 🔹 Interactive UI

Built with Streamlit for easy usage and smooth interaction.

---

# ⚙️ Technologies Used

## 🔹 Programming Language

* Python 🐍

---

## 🔹 Libraries & Frameworks

* TensorFlow / Keras
* NumPy
* PIL
* Streamlit
* OpenCV

---

## 🔹 Deployment

* Streamlit Cloud

---

# 🧠 Deep Learning Workflow

## 1️⃣ Image Upload

User uploads histopathology image.

---

## 2️⃣ Image Preprocessing

* Resize image
* Normalize pixel values
* Convert image for model input

---

## 3️⃣ Model Prediction

Deep learning model predicts:

* Benign
* Malignant

---

## 4️⃣ Result Visualization

Displays:

* Prediction
* Confidence Score
* Threshold
* Raw Model Score

---

# 📊 Sample Prediction

## ⚠️ MALIGNANT

```text id="qqz57j"
Confidence: 100%
Raw Model Score: 1.0000
Threshold Used: 0.7
Decision: Malignant
```

---

# 🚀 How to Run Locally

## Clone the Repository

```bash id="v0e8qg"
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

## Install Dependencies

```bash id="3mw30n"
pip install -r requirements.txt
```

---

## Run Streamlit App

```bash id="6ebrt6"
streamlit run app.py
```

---

# 📈 Model Capabilities

The model can:

* Analyze histopathology images
* Predict cancer type
* Provide confidence score
* Assist in medical image analysis workflows

---

# ⚠️ Important Medical Disclaimer

This project is developed for:

* Educational purposes
* Research purposes
* Learning Deep Learning concepts

It should **NOT** be used as a replacement for professional medical diagnosis.

Always consult certified medical professionals for clinical decisions.

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Deep Learning model deployment
* Medical image classification
* Streamlit web app development
* TensorFlow/Keras model integration
* Real-time AI prediction systems

---

# 🔮 Future Improvements

* Improve model accuracy
* Add Grad-CAM visualization
* Deploy using Docker
* Add patient history integration
* Multi-class cancer detection
* Cloud deployment with GPU support

---

# 👨‍💻 Author

## Dhiraj Badre

AI & Data Science Enthusiast
---

# 🌟 Conclusion

This project demonstrates how Deep Learning can be applied in healthcare for intelligent image-based prediction systems.

It combines:

* Deep Learning
* Computer Vision
* Web Deployment
* Medical AI

into a real-world application.

---

⭐ Part of my AI & Machine Learning Learning Journey
