def create_plan(instruction):

    instruction = instruction.lower()

    tasks = []

    if "api" in instruction:

        tasks.append({
            "agent": "coder",
            "task": "create_api"
        })

        tasks.append({
            "agent": "tester",
            "task": "test_api"
        })

        tasks.append({
            "agent": "git",
            "task": "auto commit api feature"
        })

    else:

        tasks.append({
            "agent": "coder",
            "task": instruction
        })

    return tasks