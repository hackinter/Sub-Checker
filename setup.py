import requests
import json
import os

class SubChecker:
    def __init__(self, domain):
        self.domain = domain
        self.subdomains = set()
        self.version = "2.1.0"  # সংস্করণ নম্বর আপডেট

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
                print("😱 ত্রুটি:", response.status_code)
                return []
        except requests.exceptions.RequestException as e:
            print("🚨 নেটওয়ার্ক ত্রুটি:", e)
            return []
        except Exception as e:
            print("🚨 অজানা ত্রুটি:", e)
            return []

    def display_results(self):
        ascii_art = r"""
███████ ██    ██ ██████         ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
██      ██    ██ ██   ██       ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
███████ ██    ██ ██████  █████ ██      ███████ █████   ██      █████   █████   ██████  
     ██ ██    ██ ██   ██       ██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
███████  ██████  ██████         ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
        """
        os.system('clear')  # টার্মিনাল পরিষ্কার করুন
        print(ascii_art)  # ASCII শিল্প প্রদর্শন
        print(f"✨ ভার্সন: {self.version}")  # সংস্করণ প্রদর্শন
        print("🔍 সাবডোমেইনগুলো:")
        if self.subdomains:
            for sub in self.subdomains:
                print(f"🌐 {sub}")
        else:
            print("🙅‍♂️ কোন সাবডোমেইন পাওয়া যায়নি।")

    def save_results(self, filename='subdomains.json'):
        try:
            with open(filename, 'w') as file:
                json.dump(list(self.subdomains), file)
            print(f"✅ ফলাফল সংরক্ষিত হয়েছে: {filename}")
        except Exception as e:
            print("🚨 ফাইল সংরক্ষণের সময় ত্রুটি:", e)

# ব্যবহার উদাহরণ
if __name__ == "__main__":
    print("👋 স্বাগতম Sub-Checker এ!")
    domain = input("🔗 আপনার ডোমেন দিন (যেমন: example.com): ").strip()  # ব্যবহারকারী ইনপুট এবং ট্রিম করা
    if not domain:
        print("🚨 দয়া করে একটি বৈধ ডোমেন দিন!")
    else:
        checker = SubChecker(domain)  # অবজেক্ট তৈরি
        checker.find_subdomains()
        checker.display_results()
        checker.save_results()  # ফলাফল JSON ফাইলে সংরক্ষণ
