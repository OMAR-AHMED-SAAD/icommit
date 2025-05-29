import os
import sys
from colorama import Fore, Style, init

CONFIG_PATH = os.path.expanduser("~/.icommit_config")
init(autoreset=True)


def set_api_key():
    """
    A function to set the API key for the Groq API from the command line
    """
    if len(sys.argv) != 2:
        print("Usage: icommit-key <api_key>")
        sys.exit(1)
    api_key = sys.argv[1]
    with open(CONFIG_PATH, "w") as f:
        f.write(api_key)
    print(Fore.GREEN + Style.BRIGHT + "API key saved successfully")


def get_api_key():
    """
    A function to get the API key for the Groq API from the configuration file
    """
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return f.read().strip()
    else:
        print("API key not set \n 1.Signup at https://console.groq.com/ to get your API key, \n 2.Run icommit-key <API_KEY> to save it.")
        sys.exit(1)
