from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Import the custom tool
from tools.github_tool import GitPushTool
from tools.file_tools import FileWriteTool
from crewai_tools import ScrapeWebsiteTool

load_dotenv()

@CrewBase
class WebCrew:
	"""WebCrew: 웹사이트 제작을 위한 전문가 팀"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self):
		self.llm = ChatGoogleGenerativeAI(
			model="gemini-2.0-flash",
			verbose=True,
			temperature=0.5,
			google_api_key=os.environ.get("GOOGLE_API_KEY")
		)

	@agent
	def project_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['project_manager'],
			tools=[ScrapeWebsiteTool()],
			verbose=True,
			llm=self.llm
		)

	@agent
	def web_designer(self) -> Agent:
		return Agent(
			config=self.agents_config['web_designer'],
			verbose=True,
			llm=self.llm
		)

	@agent
	def web_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['web_developer'],
			verbose=True,
			allow_delegation=False,
			llm=self.llm,
			tools=[GitPushTool(), FileWriteTool()] # Add FileWriteTool
		)

	@task
	def requirements_task(self) -> Task:
		return Task(
			config=self.tasks_config['requirements_task'],
		)

	@task
	def design_task(self) -> Task:
		return Task(
			config=self.tasks_config['design_task'],
		)

	@task
	def development_task(self) -> Task:
		return Task(
			config=self.tasks_config['development_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the WebCrew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
