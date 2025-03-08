import os
import streamlit as st

from src.CrewAIAgentic.ui.ui_config.ui_config import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def initialize_session(self):
        # Initialize session state for the API key if not already set
        if "GROQ_API_KEY" not in st.session_state:
            st.session_state["GROQ_API_KEY"] = ""
            
        if 'inputs' not in st.session_state:
            st.session_state.inputs = {'user_message': ''}
        st.session_state.inputs['user_message']


    def load_streamlit_ui(self):
        # Ensure session is initialized
        self.initialize_session()

        # Set up the Streamlit page
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🚣🏻 " + self.config.get_page_title())

        # Retrieve configuration options
        llm_options = self.config.get_llm_options()
        usecase_options = self.config.get_usecase_options()
        
        with st.sidebar:
            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                # Model selection for Groq LLM
                model_options = self.config.get_groq_model_options()
                st.session_state["selected_groq_model"] = self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                # API key input for Groq
                self.user_controls["GROQ_API_KEY"] = st.text_input("API Key", type="password")
                st.session_state["GROQ_API_KEY"] = self.user_controls["GROQ_API_KEY"]
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have one? Refer to https://console.groq.com/keys")

            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_options)
        if self.user_controls["selected_usecase"] == "Chatbot with Tool":
            st.subheader("Chatbot with Tool")
            with st.sidebar:
                # Input for API Key
                api_key = st.text_input("Enter your Serper.dev API Key:", type="password")
                # Store in session state and environment variable
                if api_key:
                    st.session_state.SERPER_API_KEY = api_key
                    os.environ["SERPER_API_KEY"] = api_key  # Store in environment
                else:
                    st.warning("⚠️ Please enter your Serper.dev API key to proceed. Don't have one? [Get it here](https://serper.dev/api-key)")
                    


            # Get user input using chat_input
            user_message = st.chat_input("Enter  your Topic here : e.g, AI Agents" )

            if user_message:
                # Store user message in session state
                st.session_state.inputs['user_message'] = user_message