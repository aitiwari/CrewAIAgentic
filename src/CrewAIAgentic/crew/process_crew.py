import streamlit as st

from src.CrewAIAgentic.crew.nearbyease_crew import NearbyEaseCrew
from src.CrewAIAgentic.crew.chatbot_crew import LatestAiDevelopmentCrew

class Process_crew:
    def __init__(self,llm):
        self.selected_usecase = st.session_state["selected_usecase"]
        self.llm = llm
    
    def process_usecases(self):
        
        if self.selected_usecase == "Chatbot":
            if st.session_state.inputs['user_message']:
                inputs = {
                    'topic': st.session_state.inputs['user_message']
                }
                with st.chat_message('user'):
                    st.markdown(f"You have entered topic as: {inputs['topic']}")
                
                final_result= LatestAiDevelopmentCrew(self.llm).crew().kickoff(inputs=inputs)
                with st.chat_message("ai"):
                    st.markdown(f"final result:" )
                    with st.expander("view results 👁️"):
                        st.markdown(final_result)
        elif self.selected_usecase == "NearbyEase":
            # Initialize the crew, set inputs and reset intermediate outputs.
            inputs = st.session_state["inputs"]
            if inputs:
                crew_instance = NearbyEaseCrew(self.llm)
                crew_instance.inputs = inputs
                crew_instance.previous_outputs = {}
                crew_instance.outputs = {}
                # Kick off the crew – tasks will run sequentially.
                final_result = crew_instance.crew().kickoff(inputs=inputs)
                st.markdown("## 📋 Expert Comparison")
                st.markdown(final_result)