# src/factchecking_crew/crewai.py

import os
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class FactcheckingCrew():
	"""FactcheckingCrew: single-agent, fact-checking assistant"""

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
			config=self.tasks_config['factcheck_task']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the FactcheckingCrew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True
		)
