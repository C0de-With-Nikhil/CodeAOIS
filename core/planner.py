def create_plan(instruction):
    instruction = instruction.lower()
    tasks = []

    # The AI team will now execute these 3 steps for EVERY instruction
    tasks.append({"agent": "coder", "task": {"type": "edit_file", "file": "generated_code.py", "instruction": instruction}})
    tasks.append({"agent": "tester", "task": "run tests"})
    tasks.append({"agent": "git", "task": {"branch": "ai-feature", "message": f"AI Update: {instruction}"}})

    return tasks