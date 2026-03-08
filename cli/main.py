import typer
from core.planner import create_plan
from core.orchestrator import AgentOrchestrator

app = typer.Typer()

@app.command()
def task(instruction: str):
    print(f"Instruction received: {instruction}")
    plan = create_plan(instruction)
    orchestrator = AgentOrchestrator()
    results = orchestrator.run(plan)
    print("Results:")
    for r in results:
        print(f"- {r}")

if __name__ == "__main__":
    app()