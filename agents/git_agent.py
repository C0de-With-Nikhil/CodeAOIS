import subprocess

class GitAgent:
    def execute(self, task):
        branch = task.get("branch", "ai-feature")
        message = task.get("message", "AI update")
        
        # Create branch
        subprocess.run(["git", "checkout", "-b", branch])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", message])
        
        return f"Changes committed to {branch}"