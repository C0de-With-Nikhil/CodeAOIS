import subprocess

class GitAgent:
    def execute(self, task):
        """
        Task is commit message
        """
        # Stage all changes
        subprocess.run(["git", "add", "."])

        # Commit
        commit_msg = task if isinstance(task, str) else "AI update"
        subprocess.run(["git", "commit", "-m", commit_msg])

        return "Changes committed successfully"