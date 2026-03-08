def create_plan(instruction):
    instruction = instruction.lower()
    tasks = []

    if "api" in instruction:
        tasks.append({"agent": "coder", "task": {"type": "edit_file", "file": "app.py", "instruction": "create Flask API"}})
        tasks.append({"agent": "tester", "task": "test API"})
        tasks.append({"agent": "git", "task": "Add API feature"})
    else:
        tasks.append({"agent": "coder", "task": instruction})

    return tasks