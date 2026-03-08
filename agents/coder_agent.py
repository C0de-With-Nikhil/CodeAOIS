from models.llm_interface import ask_llm
from utils.file_writer import write_file

class CoderAgent:
    def execute(self, task):
        if isinstance(task, dict):
            task_type = task.get("type")
            instruction = task.get("instruction")
            
            # If it's just a conversation, return the AI's response directly
            if task_type == "chat":
                return ask_llm(instruction)
                
            # If it's a coding task, generate the code and write the file
            elif task_type == "edit_file":
                file_path = task.get("file")
                prompt = f"Modify or create `{file_path}` based on this instruction: {instruction}. Remember, ONLY output raw code."
                code = ask_llm(prompt)
                write_file(file_path, code)
                return f"File {file_path} updated with AI code."

        return "Task failed: Unknown task format."