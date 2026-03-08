import subprocess

class GitAgent:
    def execute(self, task):
        branch = task.get("branch", "api-feature")
        message = task.get("message", "AI update")
        
        # Try to checkout the branch. If it fails (doesn't exist), create it.
        checkout_process = subprocess.run(["git", "checkout", branch], capture_output=True)
        if checkout_process.returncode != 0:
            subprocess.run(["git", "checkout", "-b", branch])
            
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", message])
        
        return f"Changes committed safely to branch: {branch}"