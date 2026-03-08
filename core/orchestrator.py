from agents.coder_agent import CoderAgent

class AgentOrchestrator:

    def __init__(self):

        self.agents = {
            "coder": CoderAgent()
        }

    def run(self, tasks):

        results = []

        for task in tasks:

            agent_name = task["agent"]
            action = task["task"]

            agent = self.agents.get(agent_name)

            if agent:
                result = agent.execute(action)
                results.append(result)

        return results