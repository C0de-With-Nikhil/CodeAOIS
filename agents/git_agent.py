import subprocess

class GitAgent:
    def execute(self, task):
        branch = task.get("branch", "ai-feature")
        message = task.get("message", "AI update")

        # run git commands and capture output so they don't print to stdout
        outputs = []

        branches = subprocess.run(
            ["git", "branch", "--list", branch],
            capture_output=True,
            text=True,
        )
        outputs.append(branches.stdout.strip())
        if branch in branches.stdout:
            proc = subprocess.run(
                ["git", "checkout", branch],
                capture_output=True,
                text=True,
            )
        else:
            proc = subprocess.run(
                ["git", "checkout", "-b", branch],
                capture_output=True,
                text=True,
            )
        outputs.append(proc.stdout.strip())

        proc = subprocess.run(
            ["git", "add", "."],
            capture_output=True,
            text=True,
        )
        outputs.append(proc.stdout.strip())

        proc = subprocess.run(
            ["git", "commit", "-m", message],
            capture_output=True,
            text=True,
        )
        outputs.append(proc.stdout.strip())

        summary = f"Changes committed to {branch}"
        extra = "\n".join(filter(None, outputs))
        if extra:
            summary += f"\n{extra}"
        return summary

