import subprocess


class GitAgent:

    def execute(self, message):

        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", message])

        return "Changes committed"