class ComparisonTask:
    def __init__(self, llm, processed_results, user_preferences: str):
        self.llm = llm
        self.processed_results = processed_results
        self.user_preferences = user_preferences

    def run(self):
        details = "\n".join([f"{idx+1}. {res['summary']}" for idx, res in enumerate(self.processed_results)])
        prompt = f"""Act as a local expert comparing these options:
{details}

Create final verdict considering:
- User preferences: {self.user_preferences}
- Distance optimization
- Value for money
- Popularity

Format as:
## 🏅 Best Overall Choice
**Name**: ...  
✅ **Why**: ...

## 🥈 Top Alternatives
1. **Name**: ...  
   ✅ **Why**: ...

💡 **Expert Tip**: (1 practical advice)
"""
        return self.llm.generate_completion(prompt, temperature=0.5)
