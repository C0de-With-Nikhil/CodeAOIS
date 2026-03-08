import os

IGNORE_FOLDERS = {
    "aois_env",
    "__pycache__",
    ".git",
    "node_modules"
}

def analyze_project():

    files = []

    for root, dirs, filenames in os.walk("."):

        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]

        for f in filenames:
            files.append(os.path.join(root, f))

    python_files = [f for f in files if f.endswith(".py")]

    return {
        "total_files": len(files),
        "python_files": len(python_files)
    }