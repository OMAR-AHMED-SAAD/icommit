import os
import subprocess
import sys

COMMANDS = {"is_git_repo": ["git", "rev-parse", "--git-dir"],
            "clear_screen": ["cls" if os.name == "nt" else "clear"],
            "commit": ["git", "commit", "-m"],
            "get_stashed_changes": ["git", "diff", "--cached"]}


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
        print(f"📝 Staged changes:\n{staged_changes}")
    except KeyboardInterrupt:
        print("\n👋 Exiting...")
        sys.exit(0)


if __name__ == "__main__":
    run()
