import requests
import json
import os
import time
import sys

class SubChecker:
    def __init__(self, domain):
        self.domain = domain
        self.subdomains = set()
        self.version = "2.1.0"  # Update version number

    def find_subdomains(self):
        url = f"https://api.hackertarget.com/hostsearch/?q={self.domain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.text.splitlines()
                for line in data:
                    parts = line.split(',')
                    subdomain = parts[0].strip()
                    if subdomain.endswith(self.domain):
                        self.subdomains.add(subdomain)
                return list(self.subdomains)
            else:
                print("😱 Error:", response.status_code)
                return []
        except requests.exceptions.RequestException as e:
            print("🚨 Network error:", e)
            return []
        except Exception as e:
            print("🚨 Unknown error:", e)
            return []

    def display_results(self):
        os.system('clear')  # Clear the terminal
        self.display_header()  # Display header
        self.typing_animation("👋 Welcome to Sub-Checker!", delay=0.02)
        self.typing_animation("🔍 Subdomains:")

        if self.subdomains:
            for sub in self.subdomains:
                self.typing_animation(f"🌐 {sub}", delay=0.02)
        else:
            self.typing_animation("🙅‍♂️ No subdomains found.", delay=0.02)

    def save_results(self, filename='subdomains.txt'):
        try:
            with open(filename, 'w') as file:
                for sub in self.subdomains:
                    file.write(sub + '\n')  # Each subdomain on a new line
            print(f"✅ Results saved: {filename}")
        except Exception as e:
            print("🚨 Error while saving file:", e)

    def typing_animation(self, text, delay=0.05):
        """Display text with a typing animation."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # Newline after text

    def display_header(self):
        banner_text = """\

███████╗██╗   ██╗██████╗        ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║   ██║██╔══██╗      ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████╗██║   ██║██████╔╝█████╗██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
╚════██║██║   ██║██╔══██╗╚════╝██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████║╚██████╔╝██████╔╝      ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═════╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                       

        """
        self.typing_animation(banner_text, delay=0.01)  # Faster typing effect

def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')

# Check Python version
if sys.version.startswith("3"):
    print("[!] Python 3 detected ...")
    time.sleep(1)
else:
    print("[x] You must run this using Python 3 ...")
    time.sleep(2)
    sys.exit(1)

# Print starting
print('[!] Starting ... ')
time.sleep(0.5)
clear()
time.sleep(1)

# Usage example
if __name__ == "__main__":
    banner_obj = SubChecker("")  # Temporary instance for displaying banner
    banner_obj.display_header()  # Display the banner with typing animation

    # Display information with animation
    info_lines = [
        "===============================================================================",
        "[*] Coded by root@hackinter                                                 [*]",
        "[*] Copyright 2024 HACKINTER                                                [*]",
        "[*] Just simple tools to make your life easier                              [*]",
        "[*] Thanks to Allah.                                                        [*]",
        "[*] https://github.com/hackinter (Hacking is Creative problem solving)      [*]",
        "===============================================================================",
    ]

    for line in info_lines:
        banner_obj.typing_animation(line, delay=0.02)  # Animate each line

    # User input
    domain = input("🔗 Enter your domain (e.g., example.com): ").strip()  # User input and trim

    if not domain:
        print("🚨 Please enter a valid domain!")
    else:
        checker = SubChecker(domain)  # Create object
        checker.typing_animation("🔍 Finding subdomains...", delay=0.02)
        checker.find_subdomains()  # Find subdomains
        checker.display_results()  # Display results
        checker.save_results()  # Save results to text file
