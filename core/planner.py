def create_plan(instruction: str):

    instruction = instruction.lower()

    tasks = []

    if "api" in instruction:
        tasks.append({
            "agent": "coder",
            "task": "create_api"
        })

    elif "function" in instruction:
        tasks.append({
            "agent": "coder",
            "task": "create_function"
        })

    else:
        tasks.append({
            "agent": "coder",
            "task": instruction
        })

    return tasks