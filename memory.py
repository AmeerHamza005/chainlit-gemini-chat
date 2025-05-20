import json
import os

MEMORY_FILE = "chat_history.json"

def load_history():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
