import typer
from brain.scanner import analyze_project
from core.planner import create_plan
from core.orchestrator import AgentOrchestrator

app = typer.Typer()

print("AOIS CLI Started")

@app.command()
def analyze():
    result = analyze_project()
    print(result)

@app.command()
def init():
    print("CodeAOIS project initialized")

@app.command()
def task(instruction: str):
    """Execute an AI task"""
    print(f"Instruction received: {instruction}")
    plan = create_plan(instruction)
    orchestrator = AgentOrchestrator()
    results = orchestrator.run(plan)
    print("Results:")
    for r in results:
        print(f"- {r}")

if __name__ == "__main__":
    app()