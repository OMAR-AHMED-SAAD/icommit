import os
import sys
import subprocess
import pyperclip
from .groq_generator import GroqGenerator
from .ollama_generator import OllamaGenerator
from colorama import Fore, Style, init

init(autoreset=True)

COMMANDS = {"is_git_repo": ["git", "rev-parse", "--git-dir"],
            "clear_screen": ["cls" if os.name == "nt" else "clear"],
            "commit": ["git", "commit", "-m"],
            "get_stashed_changes": ["git", "diff", "--cached"]}


def generate_commit_message(staged_changes: str) -> str:
    """
    Generate a commit message based on the staged changes using the Groq API or Ollama.
    Parameters:
        staged_changes (str): The staged changes to commit
    """
    try:
        llm = None
        action = input(
            "\nChoose the model to generate the commit message [o(ollama local) | g(groq online)]: "
        ).lower()
        match action.lower():
            case "o" | "ollama":
                llm = OllamaGenerator()
                llm.set_model()
            case "g" | "groq":
                llm = GroqGenerator()
            case _:
                print(Fore.RED + Style.BRIGHT + "\n Invalid input. Exiting...")
                sys.exit(1)
        return llm.generate_commit_message("Generating", staged_changes), llm
    except Exception as e:
        print(Fore.RED + Style.BRIGHT +
              f" Error generating commit message \n${e}")
        pyperclip.copy(staged_changes)
        print(
            "📋 Staged changes copied to clipboard instead to use with external hosted models"
        )
        sys.exit(1)


def interaction_loop(staged_changes: str):
    """
    Loop to interact with the user to confirm the commit message
    Parameters:
        staged_changes (str): The staged changes to commit
    """
    commit_msg,llm = generate_commit_message(staged_changes)
    action = input(
            "\n\nProceed with commit? [y(yes) | n(no) | r(regenerate)]: ").lower()
    while True:
        match action.lower():
            case "y" | "yes":
                print("\n🚀 Committing changes...")
                run_command(COMMANDS["commit"] + [commit_msg])
                break
            case "n" | "no":
                print("\n👋 Exiting...")
                sys.exit(0)
            case "r" | "regenerate":
                pass
            case _:
                print(Fore.RED + Style.BRIGHT +"\n Invalid input. Exiting...")
                break
        commit_msg = llm.generate_commit_message("Regenerating", staged_changes)
        action = input(
            "\n\nProceed with commit? [y(yes) | n(no) | r(regenerate)]: ").lower()


def run_command(command: list[str] | str):
    """
    Run a command in the terminal and return the output
    Parameters:
        command (list[str] | str): The command to run in the terminal
    """
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(Fore.RED + Style.BRIGHT + f" Error: \n {e.stderr}")
        sys.exit(1)


def run():
    try:
        # Check if the current directory is a git repository
        run_command(COMMANDS["is_git_repo"])
        staged_changes = run_command(COMMANDS["get_stashed_changes"])
        if not staged_changes:
            print("👍 No staged changes found.")
            sys.exit(0)

        interaction_loop(staged_changes)

    except KeyboardInterrupt:
        print("\n Exiting...")
        sys.exit(0)


if __name__ == "__main__":
    run()
