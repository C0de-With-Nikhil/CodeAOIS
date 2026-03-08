import typer
from core.planner import create_plan
from core.orchestrator import AgentOrchestrator

app = typer.Typer()

@app.command()
def task(instruction: str):
    """Execute an AI task.  Wrap multi-word instructions in quotes."""
    instruction_text = instruction
    print(f"Instruction received: {instruction_text}")
    plan = create_plan(instruction_text)
    orchestrator = AgentOrchestrator()
    results = orchestrator.run(plan)
    print("Results:")
    for r in results:
        print(f"- {r}")

if __name__ == "__main__":
    app()