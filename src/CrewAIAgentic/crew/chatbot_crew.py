from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool


@CrewBase
class LatestAiDevelopmentCrew():
    """Latest AI Development Crew"""

    def __init__(self, llm):
        self.llm = llm
        self.agents_config = 'config/agents.yaml'
        self.tasks_config = 'config/tasks.yaml'
    

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            llm=self.llm,
            # tools=[SerperDevTool(n_results=1)]
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True,
            llm=self.llm
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Crewailatest crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            # memory= st.session_state["chat_with_history"],
            verbose=True,
            # max_rpm=1,
            # manager_llm=self.llm
        )
