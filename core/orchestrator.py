class AgentOrchestrator:

    def __init__(self):
        self.agents = []

    def register(self, agent):
        self.agents.append(agent)

    def run(self, task):
        results = []

        for agent in self.agents:
            results.append(agent.execute(task))

        return results