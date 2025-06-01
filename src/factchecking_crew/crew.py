# src/factchecking_crew/crewai.py

import os
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class FactcheckingCrew:
    """Crew for conversational and fact-checking tasks"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def intelligent_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['intelligent_agent'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @task
    def factcheck_task(self) -> Task:
        return Task(
            config=self.tasks_config['factcheck_task'],
            output_file='output/report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.intelligent_agent],
            tasks=[self.factcheck_task],
            process=Process.sequential,
            verbose=True
        )
