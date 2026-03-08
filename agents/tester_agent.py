import subprocess

class TesterAgent:
    def execute(self, task):
        # Simple test runner + linting
        lint_result = subprocess.run(["flake8", "."], capture_output=True, text=True)
        test_result = subprocess.run(["pytest"], capture_output=True, text=True)
        return f"Lint:\n{lint_result.stdout}\nTests:\n{test_result.stdout}"