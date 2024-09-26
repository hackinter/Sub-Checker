```markdown
# Sub-Checker

Sub-Checker is a simple Python tool designed to discover active subdomains of a given domain using the HackerTarget API. This tool is particularly useful for security researchers, ethical hackers, and anyone interested in understanding the subdomain structure of a website.

## Features

- Fetches active subdomains from HackerTarget API.
- Displays results in a user-friendly ASCII art format.
- Shows the current version of the tool.
- Saves the discovered subdomains to a JSON file for later reference.

## Requirements

- Python 3.x
- `requests` library

## Installation

To install the necessary dependencies, run:

```bash
sudo apt-get install python3-requests
```

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/hackinter/Sub-Checker.git
   cd Sub-Checker
   ```

2. Run the tool:

   ```bash
   python3 sub_checker.py
   ```

3. Enter the domain you wish to check (e.g., `example.com`).

## Example

```
👋 Welcome to Sub-Checker!
🔗 Enter your domain (e.g., example.com): example.com
```

The tool will display the active subdomains along with the current version of the tool.

## Saving Results

The results will be saved to a JSON file named `subdomains.json` in the same directory.

## Versioning

The current version of Sub-Checker is `2.1.0`.

## Contributing

If you would like to contribute to Sub-Checker, please fork the repository and submit a pull request. Any contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **HACKINTER**

## Acknowledgments

- [HackerTarget](https://hackertarget.com/) for providing the API used in this tool.
```

Feel free to modify any sections as needed. If you need further adjustments or additions, just let me know!
