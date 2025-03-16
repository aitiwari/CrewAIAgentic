from duckduckgo_search import DDGS

class SearchTask:
    def __init__(self, category: str, location: str, user_preferences: str = "", max_results: int = 8):
        self.category = category
        self.location = location
        self.user_preferences = user_preferences
        self.max_results = max_results

    def run(self):
        query = f"Best {self.category} near {self.location}"
        if self.user_preferences.strip():
            query += f" {self.user_preferences.strip()}"
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=self.max_results)
        return results
