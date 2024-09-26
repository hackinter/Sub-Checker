import requests
import json
import os

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
        ascii_art = r"""
        ███████ ██    ██ ██████         ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
        ██      ██    ██ ██   ██       ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
        ███████ ██    ██ ██████  █████ ██      ███████ █████   ██      █████   █████   ██████  
             ██ ██    ██ ██   ██       ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
        ███████  ██████  ██████         ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
        """
        
        os.system('clear')  # Clear the terminal
        print(ascii_art)  # Display ASCII art
        print(f"✨ Version: {self.version}")  # Display version
        print("🔍 Subdomains:")
        if self.subdomains:
            for sub in self.subdomains:
                print(f"🌐 {sub}")
        else:
            print("🙅‍♂️ No subdomains found.")

    def save_results(self, filename='subdomains.json'):
        try:
            with open(filename, 'w') as file:
                json.dump(list(self.subdomains), file)
            print(f"✅ Results saved: {filename}")
        except Exception as e:
            print("🚨 Error while saving file:", e)

# Usage example
if __name__ == "__main__":
    print("👋 Welcome to Sub-Checker!")
    domain = input("🔗 Enter your domain (e.g., example.com): ").strip()  # User input and trim
    if not domain:
        print("🚨 Please enter a valid domain!")
    else:
        checker = SubChecker(domain)  # Create object
        checker.find_subdomains()
        checker.display_results()
        checker.save_results()  # Save results to JSON file
