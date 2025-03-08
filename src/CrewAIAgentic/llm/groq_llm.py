import streamlit as st
# Initialize the Groq model for use with agents
from crewai import LLM



class GroqLLM:
    def __init__(self):
       
        self.model = 'groq/'+st.session_state["selected_groq_model"]

    def groq_llm_config(self):
        llm = LLM(
            max_retries=3,
            temperature=0.7,
            model= self.model,
            api_key=st.session_state["GROQ_API_KEY"] 
        )
        # llm = LLM(model="groq/gemma2-9b-it",api_key=st.session_state["GROQ_API_KEY"])

        return llm
