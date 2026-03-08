from agents.coder_agent import CoderAgent
from agents.tester_agent import TesterAgent
from agents.git_agent import GitAgent


class AgentOrchestrator:

    def __init__(self):

        self.agents = {
            "coder": CoderAgent(),
            "tester": TesterAgent(),
            "git": GitAgent()
        }

    def run(self, tasks):

        results = []

        for task in tasks:

            agent = self.agents.get(task["agent"])

            if agent:
                result = agent.execute(task["task"])
                results.append(result)

        return results