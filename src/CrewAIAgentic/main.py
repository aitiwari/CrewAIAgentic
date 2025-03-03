 
from src.CrewAIAgentic.ui.streamlitui.load_ui import LoadStreamlitUI


def load_crewai_agentic_app():
    try :
        ui = LoadStreamlitUI()
        ui.load_streamlit_ui()
        
    except Exception as e:
        raise ValueError(str(e))
    
    