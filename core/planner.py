def create_plan(instruction):
    instruction_lower = instruction.lower()
    tasks = []

    # 1. Check if the user is just chatting (e.g., "hi", "hello", "how are you?")
    chat_words = ["hi", "hello", "hey", "who are you"]
    if instruction_lower in chat_words or len(instruction_lower.split()) <= 2:
        # Just use the Coder agent to chat, don't run tests, don't use Git!
        tasks.append({"agent": "coder", "task": {"type": "chat", "instruction": instruction}})
        return tasks

    # 2. Otherwise, treat it as a coding task!
    if "api" in instruction_lower or "app" in instruction_lower:
        tasks.append({"agent": "coder", "task": {"type": "edit_file", "file": "app.py", "instruction": instruction}})
    else:
        tasks.append({"agent": "coder", "task": {"type": "edit_file", "file": "generated_code.py", "instruction": instruction}})
        
    tasks.append({"agent": "tester", "task": "run tests"})
    tasks.append({"agent": "git", "task": {"branch": "ai-feature", "message": f"AI Update: {instruction}"}})

    return tasks