import platform
import os
import urllib.request
import subprocess


class ChromeInstaller:
    def __init__(self):
        self.chrome_url = ""
        self.chrome_file = ""
        self.chrome_path = "./"
        
    def download_chrome(self):
        """Download chrome from the given URL"""
        fullfilename = os.path.join(self.chrome_path, self.chrome_file)
        urllib.request.urlretrieve(self.chrome_url, fullfilename)

    def run_installer(self):
        """Run the chrome installer"""
        if platform.system() == 'Darwin':
            subprocess.call(['open', self.chrome_file])
        elif platform.system() == 'Windows':
            subprocess.run([self.chrome_file], check=True)
        elif platform.system() == 'Linux':
            subprocess.run(["sudo", "dpkg", "-i", self.chrome_file], check=True)
        else:
            raise ValueError('Unsupported platform')

    def install_chrome(self):
        """Install Chrome based on the user's operating system"""
        if platform.system() == 'Darwin':
            self.chrome_url = "https://dl.google.com/chrome/mac/universal/stable/GGRO/googlechrome.dmg"
            self.chrome_file = "googlechrome.dmg"
        elif platform.system() == 'Windows':
            self.chrome_url = "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BE2A6BC48-C42E-9767-4472-252CF88743FB%7D%26lang%3Den%26browser%3D3%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe"
            self.chrome_file = "ChromeSetup.exe"
        elif platform.system() == "Linux":
            self.chrome_url = "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
            self.chrome_file = "google-chrome-stable_current_amd64.deb"
        else:
            raise ValueError('Unsupported platform')

        self.download_chrome()
        self.run_installer()
