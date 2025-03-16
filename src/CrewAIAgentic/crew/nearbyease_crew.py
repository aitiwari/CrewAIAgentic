from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew

from src.CrewAIAgentic.crew.tasks.analysis_task import AnalysisTask
from src.CrewAIAgentic.crew.tasks.comparison_task import ComparisonTask
from src.CrewAIAgentic.crew.tasks.search_task import SearchTask
# from src.CrewAIAgentic.llm.groq_client import GroqLLM

@CrewBase
class NearbyEaseCrew:
    # Override the default paths by setting these attributes at the class level.
    agents_config = "config/nearbyease_agents.yaml"
    tasks_config = "config/nearbyease_tasks.yaml"
    
    def __init__(self, llm):
        self.llm = llm
        self.inputs = {}
        self.previous_outputs = {}
        self.outputs = {}

    @agent
    def search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["search_agent"],
            verbose=True,
            llm=self.llm,
        )
    
    @agent
    def analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["analysis_agent"],
            verbose=True,
            llm=self.llm,
        )
    
    @task
    def search_task(self) -> Task:
        def run_search():
            category = self.inputs.get("category", "Restaurant")
            location = self.inputs.get("location", "Mumbai India")
            user_preferences = self.inputs.get("user_preferences", "")
            params = self.tasks_config["search_task"].get("parameters", {})
            max_results = params.get("max_results", 8)
            search = SearchTask(
                category=category,
                location=location,
                user_preferences=user_preferences,
                max_results=max_results
            )
            results = search.run()
            self.previous_outputs["search_task"] = results
            return results
        return Task(config=self.tasks_config["search_task"], run=run_search)
    
    @task
    def analysis_task(self) -> Task:
        def run_analysis():
            results = self.previous_outputs.get("search_task", [])
            analysis = AnalysisTask(self.llm)
            processed = analysis.process_results(results)
            self.outputs["processed_results"] = processed
            return processed
        return Task(config=self.tasks_config["analysis_task"], run=run_analysis)
    
    @task
    def comparison_task(self) -> Task:
        def run_comparison():
            processed_results = self.outputs.get("processed_results", [])
            user_preferences = self.inputs.get("user_preferences", "")
            comparison = ComparisonTask(self.llm, processed_results, user_preferences)
            return comparison.run()
        return Task(config=self.tasks_config["comparison_task"], run=run_comparison, output_file="expert_comparison.md")
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=[self.search_task(), self.analysis_task(), self.comparison_task()],
            process=Process.sequential,
            verbose=True,
        )
