from models.llm_interface import ask_llm
from utils.file_writer import write_file


class CoderAgent:

    def execute(self, task):

        prompt = f"Write Python code for {task}"

        code = ask_llm(prompt)

        write_file("generated_code.py", code)

        return "Code generated successfully"