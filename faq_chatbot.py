from dotenv import load_dotenv
import os
import streamlit as st
import requests

# Load the API key from .env
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

st.title("🧠 AI FAQ Chatbot")
st.write("Ask a question about our services!")

question = st.text_input("Your Question:")

faq_context = """
We offer AI chatbot development, web automation, and scriptwriting services.
Our pricing starts at $20 for simple chatbots and goes up based on complexity.
Support is available Monday to Friday, 9AM to 6PM.
We accept payments via PayPal and direct bank transfer.
"""

if question:
    with st.spinner("Thinking..."):
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": f"You are a helpful assistant. Here is the FAQ data: {faq_context}"},
                {"role": "user", "content": question}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]["content"]
            st.success(answer)
        else:
            st.error("Something went wrong. Please check your API key or try again later.")
