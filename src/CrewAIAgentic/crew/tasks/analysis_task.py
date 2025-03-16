import requests

from src.CrewAIAgentic.llm.groq_client import GroqLLM
from src.CrewAIAgentic.tools.customtoolbs4 import scrape_page_content

class AnalysisTask:
    def __init__(self, llm: GroqLLM):
        self.llm = llm

    def process_results(self, results):
        processed = []
        for res in results:
            url = res.get('href', '')
            body = res.get('body', '')
            page_content = scrape_page_content(url, requests)
            prompt = f"""Analyze this business listing for recommendation:
**URL**: {url}
**Content**: {page_content or body}

Provide in markdown:
- 🌟 Rating (convert to 5-star scale)
- 📏 Estimated distance
- 🏆 Top 3 features
- 💡 Why recommended (1 sentence)
- 📍 Google Maps link (if location found)
"""
            summary = self.llm.generate_completion(prompt, temperature=0.3)
            processed.append({
                "title": res.get('title', ''),
                "url": url,
                "summary": summary
            })
        return processed
