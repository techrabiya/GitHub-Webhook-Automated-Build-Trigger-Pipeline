import streamlit as st
import datetime

st.title("⚡ Rabia's GitHub Webhook CI/CD Pipeline")
st.write("Simulate automated build triggers and continuous deployment upon code commits.")

if st.button("Simulate Push Event & Build Trigger"):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.info(f"Event Timestamp: {current_time}")
    st.success("🚀 **Webhook Payload Received:** `git commit -m 'update'`")
    st.success("✅ **CI/CD Pipeline Status:** Build Successful & Auto-Deployed!")
