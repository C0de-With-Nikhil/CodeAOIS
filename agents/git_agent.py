import subprocess

class GitAgent:
    def execute(self, task):
        branch = task.get("branch", "ai-feature")
        message = task.get("message", "AI update")

        # run git commands while capturing their output to prevent
        # interleaving with the CLI's `Results:` section.  we don't
        # expose the raw git output in the return value because the
        # orchestrator only needs a simple summary.

        branches = subprocess.run(
            ["git", "branch", "--list", branch],
            capture_output=True,
            text=True,
        )
        if branch in branches.stdout:
            subprocess.run(
                ["git", "checkout", branch],
                capture_output=True,
                text=True,
            )
        else:
            subprocess.run(
                ["git", "checkout", "-b", branch],
                capture_output=True,
                text=True,
            )

        subprocess.run(
            ["git", "add", "."],
            capture_output=True,
            text=True,
        )

        subprocess.run(
            ["git", "commit", "-m", message],
            capture_output=True,
            text=True,
        )

        return f"Changes committed to {branch}"

