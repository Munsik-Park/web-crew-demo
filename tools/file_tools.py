from crewai.tools import BaseTool
import os

class FileWriteTool(BaseTool):
    name: str = "File Write Tool"
    description: str = (
        "Write content to a file. Useful for saving code or documents. "
        "Input should be the filename and the content."
    )

    def _run(self, filename: str, content: str) -> str:
        try:
            # Ensure directory exists
            directory = os.path.dirname(filename)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"Successfully wrote to {filename}"
        except Exception as e:
            return f"Error writing to file: {str(e)}"
