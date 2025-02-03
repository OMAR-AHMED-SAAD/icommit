import os
import sys
import subprocess
import pyperclip
from groq import Groq
from .system_prompt import COMMIT_PROMPT
from .api_key import get_api_key

COMMANDS = {"is_git_repo": ["git", "rev-parse", "--git-dir"],
            "clear_screen": ["cls" if os.name == "nt" else "clear"],
            "commit": ["git", "commit", "-m"],
            "get_stashed_changes": ["git", "diff", "--cached"]}

MODEL = "llama3-8b-8192"

def clean_commit_message(commit_message: str) -> str:
    """
    Clean the commit message by removing any trailing whitespace and newlines or invalid ai generated text
    Parameters:
        commit_message (str): The commit message to clean
    Returns:
        str: The cleaned commit message
    """
    commit_message = commit_message.replace("Here is the generated commit message:", " ")
    return commit_message.strip()

def generate_commit_message(staged_changes: str) -> str:
    """
    Generate a commit message based on the staged changes using the Groq API and copy the diff to clipboard on failure
    Parameters:
        staged_changes (str): The staged changes to commit
    Returns:
        str: The generated commit message
    """
    try:
        client = Groq(api_key=get_api_key())
        stream = client.chat.completions.create(

            messages=[
                {
                    "role": "system",
                    "content": COMMIT_PROMPT
                },
                {
                    "role": "user",
                    "content": f"Here is the diff for the staged changes:\n{staged_changes}"
                }
            ],

            model=MODEL,
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=True,
        )
        print("🤖 Generating commit message...")
        print("-" * 50 + "\n")
        commit_msg = ""
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
                commit_msg += content
        commit_msg = clean_commit_message(commit_msg)
        return commit_msg
    except Exception as e:
        # print("❗️ Error generating commit message check api logs for rate limiting or token limit exception")
        print(f"❗️ Error generating commit message \n${e}")
        pyperclip.copy(staged_changes)
        print("📋 Staged changes copied to clipboard instead to use with external hosted models")
        sys.exit(1)


def interaction_loop(staged_changes: str):
    """
    Loop to interact with the user to confirm the commit message
    Parameters:
        staged_changes (str): The staged changes to commit
    """
    while True:
        commit_msg = generate_commit_message(staged_changes)
        action = input(
            "\n\nProceed with commit? [y(yes) | n(no) | r(regenerate)]: ").lower()
        match action:
            case "y":
                print("\n🚀 Committing changes...")
                run_command(COMMANDS["commit"] + [commit_msg])
                break
            case "n":
                print("\n👋 Exiting...")
                sys.exit(0)
            case "r":
                subprocess.run(COMMANDS["clear_screen"])
                continue
            case _:
                print("\n❗️ Invalid input. Exiting...")
                break


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
        print(f"❗️ Error: \n {e.stderr}")
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
        print("\n👋 Exiting...")
        sys.exit(0)


if __name__ == "__main__":
    run()
