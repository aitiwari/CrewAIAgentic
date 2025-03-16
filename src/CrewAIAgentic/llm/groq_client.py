import os
import streamlit as st
from groq import Groq

class GroqLLM:
    def __init__(self, api_key: str = None):
        key = api_key or st.session_state["GROQ_API_KEY"]
        self.client = Groq(api_key=key)
    
    def generate_completion(self, prompt: str, model: str = "llama-3.3-70b-versatile", temperature: float = 0.3) -> str:
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
