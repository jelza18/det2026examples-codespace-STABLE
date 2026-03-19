from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from multi_agent_example.tools.custom_tool import RandomNumberTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MultiAgentExample():
    """MultiAgentExample crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def deep_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['deep_researcher'], # type: ignore[index]
            verbose=True,
            tools=[RandomNumberTool()]
        )

    @agent
    def broad_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['broad_researcher'], # type: ignore[index]
            verbose=True,
            tools=[RandomNumberTool()]
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def deep_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['deep_research_task'], # type: ignore[index]
        )

    @task
    def broad_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['broad_research_task'], # type: ignore[index]
        )

    @task
    def editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['editing_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MultiAgentExample crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        knowledge_source = TextFileKnowledgeSource(file_paths=["knowledge_source.txt"])

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            knowledge_source=[knowledge_source]
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
