# streamlit_app.py
import streamlit as st
import requests

st.title("🧠 Custom LLM Trainer")

backend_url = "http://127.0.0.1:8000"

st.header("📂 Upload Training Data")
uploaded_file = st.file_uploader("Choose a dataset (txt, csv, json)", type=["txt", "csv", "json", "pdf", "docx"])

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    res = requests.post(f"{backend_url}/upload", files=files)
    st.success(f"Uploaded: {res.json()['filename']}")

st.header("⚙️ Configure & Train")
model_name = st.selectbox("Choose Base Model", ["LLaMA-2", "Mistral", "GPT-Neo", "Gemma"])
if st.button("🚀 Start Training"):
    res = requests.post(f"{backend_url}/train", data={"model_name": model_name})
    st.success(res.json()["status"])
