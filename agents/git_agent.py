import subprocess

class GitAgent:
    def execute(self, task):
        branch = task.get("branch", "ai-feature")
        message = task.get("message", "AI update")

        # Check if branch exists
        branches = subprocess.run(["git", "branch", "--list", branch], capture_output=True, text=True)
        if branch in branches.stdout:
            subprocess.run(["git", "checkout", branch])
        else:
            subprocess.run(["git", "checkout", "-b", branch])

        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", message])

        return f"Changes committed to {branch}"