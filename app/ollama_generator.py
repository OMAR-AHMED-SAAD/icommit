import sys
import ollama
from .llm import LLM
from .system_prompt import COMMIT_PROMPT
from colorama import Fore, Style, init

init(autoreset=True)

class OllamaGenerator(LLM):
    """Generates commit messages using Ollama."""

    def __init__(self):
        self.model = None

    def set_model(self):
        """Prompt the user to select an Ollama model with retries on invalid input."""
        models = ollama.list().models
        if not models:
            print(
                Fore.RED + "No ollama models found. Please add a model using 'ollama pull <model-name>'.")
            sys.exit(1)

        while True:
            try:
                print("\nAvailable Ollama models:")
                for i, model in enumerate(models):
                    print(f"{i+1}. {model.model}")
                choice = int(
                    input("Enter the number of the model you want to use: ")) - 1
                if 0 <= choice < len(models):
                    self.model = models[choice]["model"]
                    print(f"✅ Selected model: {self.model}")
                    break  # Exit loop after valid selection
                else:
                    print(Fore.RED + "Invalid model number. Please try again.")

            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")

    def generate_commit_message(self, type: str, staged_changes: str) -> str:
        stream = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": COMMIT_PROMPT},
                {"role": "user", "content": f"Here is the diff for the staged changes:\n{staged_changes}"}
            ],
            stream=True
        )
        print(Fore.BLUE + Style.BRIGHT +
              f"{type} commit message with Ollama {self.model}...")
        print(Fore.BLUE + Style.BRIGHT + "-" * 50 + "\n")

        return self.stream_print(stream)

    def get_chunk_content(self, chunk) -> str:
        return chunk.get("message", {}).get("content", "")
