%%writefile app.py
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import gdown
import os
import time

st.set_page_config(
    page_title="Breast Cancer Detection",
    page_icon="🩺",
    layout="wide"
)

# ---- Load Model from Google Drive ----
@st.cache_resource
def load_model():
    model_path = "breast_cancer_model_v3.keras"

    if not os.path.exists(model_path):
        with st.spinner("⏳ Downloading model... please wait"):
            # PASTE YOUR GOOGLE DRIVE FILE ID BELOW
            file_id = "1neiW-2yhVQe0FhqYSApuNU7yMCFWnWzy"
            url = f"https://drive.google.com/uc?id={1-EwzZkzDths-OpMPdX-ijn8ND8nNIOSz}"
            gdown.download(url, model_path, quiet=False)

    model = tf.keras.models.load_model(model_path)
    return model

model = load_model()

# ---- Header ----
st.title("🩺 Breast Cancer Detection")
st.write("Upload a histopathology image to get an AI-powered prediction.")
st.divider()

# ---- Layout ----
col1, col2 = st.columns(2)

with col1:
    st.subheader("Upload Image")
    uploaded = st.file_uploader("Choose an image", type=["jpg","jpeg","png"])
    threshold = st.slider(
        "Decision Threshold", 0.1, 0.9, 0.5, 0.05,
        help="Score above this = Malignant"
    )

    if uploaded is not None:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("🔍 Run Prediction", use_container_width=True):
            with st.spinner("Analyzing image..."):
                img_rgb = img.convert("RGB").resize((224, 224))
                arr = np.array(img_rgb) / 255.0
                arr = np.expand_dims(arr, axis=0)
                score = float(model.predict(arr, verbose=0)[0][0])
                time.sleep(0.5)
            st.session_state["score"] = score
            st.session_state["threshold"] = threshold

with col2:
    st.subheader("Prediction Result")

    if "score" in st.session_state:
        score = st.session_state["score"]
        thr = st.session_state["threshold"]
        conf = score * 100 if score > thr else (1 - score) * 100

        if score > thr:
            st.error("## ⚠️ MALIGNANT")
            st.write("**Cancer Detected** — Please consult a specialist immediately.")
        else:
            st.success("## ✅ BENIGN")
            st.write("**No Cancer Detected** — Continue routine checkups.")

        st.metric(label="Confidence", value=f"{conf:.1f}%")
        st.progress(conf / 100)

        with st.expander("See Details"):
            st.write(f"**Raw Model Score:** {score:.4f}")
            st.write(f"**Threshold Used:** {thr}")
            st.write(f"**Decision:** {'Malignant' if score > thr else 'Benign'}")

        st.divider()
        st.caption("⚠️ For educational purposes only. Not a substitute for medical diagnosis.")
    else:
        st.info("👈 Upload an image and click Run Prediction to see results.")
