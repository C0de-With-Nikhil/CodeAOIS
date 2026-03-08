from models.llm_interface import ask_llm
from utils.file_writer import write_file
from brain.memory import ProjectMemory

memory = ProjectMemory()

class CoderAgent:
    def execute(self, task):
        """
        Task can now be like:
        {
            "type": "edit_file",
            "file": "auth.py",
            "instruction": "add login function preserving existing code"
        }
        """

        if isinstance(task, dict) and task.get("type") == "edit_file":
            file_path = task.get("file")
            instruction = task.get("instruction")
            prompt = f"Modify `{file_path}` with instruction: {instruction}, preserving style and existing code"
            code = ask_llm(prompt)

            write_file(file_path, code)
            memory.store(file_path, code)
            return f"File {file_path} updated"

        else:
            # Fallback for simple code generation
            prompt = f"Write Python code for: {task}"
            code = ask_llm(prompt)
            write_file("generated_code.py", code)
            memory.store("generated_code.py", code)
            return "Code generated successfully"