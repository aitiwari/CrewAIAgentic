from crewai.tools import BaseTool
from duckduckgo_search import DDGS

class CustomDuckDuckGoTool(BaseTool):
    name: str = "DuckDuckGoSearchTool"
    description: str = "Searches DuckDuckGo and returns text results for a given query."
    
    def _run(self, query: str) -> str:
        # Create a DuckDuckGo search instance and perform the search
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=1)
        return str(results)  # Convert results to string if needed

# Instantiate the custom tool
custom_duckduckgo_tool = CustomDuckDuckGoTool()
