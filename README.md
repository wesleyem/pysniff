# Keylogger

This script is a keylogger that listens to keyboard events and logs all keystrokes to a file. Once the file size reaches a certain limit, it commits the changes to a GitHub repository using the GitHub API. It requires a configuration file `config.json` that contains the following information:

## Configuration

### GitHub Repository Details

- `gh.user`: Your GitHub username
- `gh.repo`: The name of the repository you want to commit to
- `gh.api_token`: Your GitHub personal access token with repo scope
- `gh.file_path`: The path to the file in the repository where you want to store the keystrokes

### Keylogger Details

- `keylogger.log_file`: The path to the file where the keystrokes will be logged
- `keylogger.log_size_limit`: The maximum size of the log file in bytes

### Options

`- options.datetime_format`: The format of the timestamp to be appended to the file path when committing changes to GitHub. It follows the strftime() format.

## Usage

### Requirements

`pynput`

### Install

Install the required packages by running

```bash
pip install -r requirements.txt
```

### Execution

Create a config.json file with your GitHub repository details and keylogger options.
Run the script using

```bash
python keylogger.py
```

The script will start logging your keystrokes to the specified file path.
Once the file size limit is reached, the script will commit the changes to the specified GitHub repository using the GitHub API.

# License

This project is licensed under the MIT License. See LICENSE for more information.
