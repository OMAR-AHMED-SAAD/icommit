from .llm import LLM
from groq import Groq
from .system_prompt import COMMIT_PROMPT
from .groq_api_key import get_api_key
from colorama import Fore, Style, init

init(autoreset=True)

class GroqGenerator(LLM):
    """Generates commit messages using Groq API."""

    def __init__(self):
        self.MODEL = "llama3-8b-8192"   
        self.client = Groq(api_key=get_api_key())

    def generate_commit_message(self, type: str,staged_changes: str) -> str:
        stream = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": COMMIT_PROMPT},
                {"role": "user", "content": f"Here is the diff for the staged changes:\n{staged_changes}"}
            ],
            model= self.MODEL,
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=True,
        )
        print(Fore.BLUE + Style.BRIGHT + f"{type} commit message with Groq...")
        print(Fore.BLUE + Style.BRIGHT + "-" * 50 + "\n")

        return self.stream_print(stream)
    
    def get_chunk_content(self, chunk) -> str:
        return chunk.choices[0].delta.content