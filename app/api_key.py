import os
import sys

CONFIG_PATH = os.path.expanduser("~/.icommit_config")

def set_api_key():
    if len(sys.argv) != 2:
        print("Usage: icommit-key <api_key>")
        sys.exit(1)
    api_key = sys.argv[1]
    with open(CONFIG_PATH, "w") as f:
        f.write(api_key)
    print("API key saved successfully!")


def get_api_key():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return f.read().strip()
    else:
        print("API key not set \n 1.Signup at https://console.groq.com/ to get your API key, \n 2.Run icommit-key <API_KEY> to save it.")
        sys.exit(1)