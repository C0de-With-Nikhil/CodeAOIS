def create_plan(instruction):
    tasks = []
    instruction = instruction.lower()
    if "api" in instruction:
        tasks.append({"agent": "coder", "task": {"type": "edit_file", "file": "app.py", "instruction": "create Flask API"}})
        tasks.append({"agent": "tester", "task": "run tests"})
        tasks.append({"agent": "git", "task": {"branch": "api-feature", "message": "Add Flask API"}})
    else:
        tasks.append({"agent": "coder", "task": instruction})
    return tasks