# Sub-Checker (Subdomain Enumeration Tool)

[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge&logo=github)](https://github.com/hackinter/Sub-Checker)  
**Author:** HACKINTER  
**Created Date:** 2024

<p align="center">
<a href="https://github.com/hackinter"><img title="Github" src="https://img.shields.io/badge/hackinter-grey?style=for-the-badge&logo=github"></a>
</p>
<p align="center"> 
<a href="https://x.com/_anonix_z"><img title="Twitter" src="https://img.shields.io/badge/Twitter-HACKINTER-lightgrey?style=for-the-badge&logo=twitter"></a>
</p>

---

## DESCRIPTION:
**Sub-Checker** is a Python-based subdomain enumeration tool designed to help penetration testers and security researchers identify subdomains for any given domain. This tool automates subdomain discovery by using a variety of search engines and APIs to gather results efficiently.

---

## FEATURES:
- Subdomain enumeration using multiple search engines.
- Supports subdomain discovery via various APIs for better results.
- Results can be saved in text or PDF format.
- User-friendly graphical interface with a clean design.
- Optimized for both beginners and professionals.

---

## REQUIREMENTS:
Before using **Sub-Checker**, ensure the following dependencies are installed on your system:

- **Python 3.x**: Check if Python 3.x is installed using `python3 --version`.
- **Git**: Clone the repository with `git --version`.
- **Pip**: Install dependencies via pip. It should come with Python 3.x.
- **APIs**: Some APIs might require free registration for API keys.

---

## INSTALLATION:

### For Linux:
To install and run **Sub-Checker**, execute the following commands in your terminal:

```bash
sudo apt-get update -y
sudo apt-get install python3 git -y
sudo apt-get install python3-pip -y
git clone https://github.com/hackinter/Sub-Checker.git
cd Sub-Checker
pip install -r requirements.txt
```

### For Termux:
For Termux users, you can follow these steps:

```bash
pkg update -y
pkg upgrade -y
pkg install python git -y
pip install -r requirements.txt
git clone https://github.com/hackinter/Sub-Checker.git
cd Sub-Checker
```

---

## USAGE:
To use **Sub-Checker**, run the following command:

```bash
python3 sub_checker.py
```

You will be prompted to enter a domain name (e.g., `example.com`). The tool will enumerate subdomains and display the results.

### Options:
- **Save Results**: After subdomain enumeration, the tool allows you to save results in text or PDF format.
- **Multiple Search Engines**: Subdomains are discovered through a variety of search engines, ensuring comprehensive results.

---

## ONE-CLICK INSTALLATION:

For quick installation, use this one-liner command for **Linux**:

```bash
sudo apt-get update -y && sudo apt-get install python3 git -y && sudo apt-get install python3-pip -y && git clone https://github.com/hackinter/Sub-Checker.git && cd Sub-Checker && pip install -r requirements.txt
```

---

## CONTRIBUTIONS:
We welcome contributions! Feel free to fork this repository, submit issues, or send pull requests to improve **Sub-Checker**.

---

## CREDITS:
Special thanks to all contributors and open-source tools that helped build this project. Contributions from the security community are always appreciated.

---

### © 2024 HACKINTER. All rights reserved.
