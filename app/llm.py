import abc
from colorama import Fore, Style, init
from .commit_msg import CommitMsg

init(autoreset=True)

class LLM(abc.ABC):
    """Interface for commit message generation."""

    @abc.abstractmethod
    def generate_commit_message(self, staged_changes: str) -> str:
        """Generate a commit message from staged changes.
        Args:
            staged_changes: The changes to commit.
        Returns:
            The generated commit message.
        """
        pass

    @abc.abstractmethod
    def get_chunk_content(self, chunk) -> str:
        """Get the content of a chunk according to the choosen model.
        Args:
            chunk: The chunk to get the content from.
        Returns:
            The content of the chunk.
        """
        pass

    def stream_print(self, stream):
        """Print the stream of chunks and return the commit message.
        Args:
            stream: The stream of chunks to print.
        Returns:
            The commit message.
        """
        commit_msg = ""
        for chunk in stream:
            content = self.get_chunk_content(chunk)
            if content:
                print(Fore.GREEN + Style.BRIGHT + content, end="", flush=True)
                commit_msg += content
        commit_msg = CommitMsg.clean_commit_message(commit_msg)
        return commit_msg