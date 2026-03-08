import os

def analyze_project():
    files = []

    for root, dirs, filenames in os.walk("."):
        for f in filenames:
            files.append(f)

    python_files = [f for f in files if f.endswith(".py")]
    js_files = [f for f in files if f.endswith(".js")]

    result = {
        "total_files": len(files),
        "python_files": len(python_files),
        "javascript_files": len(js_files)
    }

    return result