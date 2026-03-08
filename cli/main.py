import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import typer
from brain.scanner import analyze_project

print("AOIS CLI Started")

app = typer.Typer()

@app.command()
def analyze():
    result = analyze_project()
    print(result)

@app.command()
def init():
    print("CodeAOIS project initialized")

if __name__ == "__main__":
    app()