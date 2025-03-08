 
from src.CrewAIAgentic.llm.groq_llm import GroqLLM
from src.CrewAIAgentic.crew.chatbot_crew import LatestAiDevelopmentCrew
from src.CrewAIAgentic.ui.streamlitui.load_ui import LoadStreamlitUI

#packages
import streamlit as st

def load_crewai_agentic_app():
    try :
        ui = LoadStreamlitUI()
        ui.load_streamlit_ui()
        
        llm_config = GroqLLM()
        llm = llm_config.groq_llm_config()
        if st.session_state.inputs['user_message']:
            inputs = {
                'topic': st.session_state.inputs['user_message']
            }
            with st.chat_message('user'):
                st.markdown(f"You have entered topic as: {inputs['topic']}")
            
            final_result= LatestAiDevelopmentCrew(llm).crew().kickoff(inputs=inputs)
            with st.chat_message("ai"):
                st.markdown(f"final result:" )
                with st.expander("view results 👁️"):
                    st.markdown(final_result)
        
    except Exception as e:
        raise ValueError(str(e))
    
    