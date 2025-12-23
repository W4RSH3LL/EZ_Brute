# EZ_Brute

**EZ_Brute** is a simple Python-based authentication testing tool designed to perform basic brute-force login checks against web applications.

> ⚠️ **Authorized Use Only**  
> This tool is intended **strictly for educational purposes and authorized security testing** (e.g., your own applications or systems you have explicit permission to test).  
> Unauthorized use against systems you do not own or have permission to test is illegal and unethical.

![EZ Brute Logo](/assets/screenshot_1.png)

---

## Features

- Single target support atm
- Username and password wordlist support
- Custom success/login indicator string
- Colored terminal output for clarity
- Progress tracking with attempt counter
- Session-based requests using `requests.Session`

---

## Installation

```bash
git clone https://github.com/W4RSH3LL/EZ_Brute.git
cd EZ_Brute/
pip3 install -r requirements
```

---

## Usage

```bash
python tool.py -t <target_url> -u <usernames.txt> -p <passwords.txt> -l "<success_string>"
```

**Example:**
```bash
python tool.py \
  -t http://example.com/login.php \
  -u users.txt \
  -p passwords.txt \
  -l "Welcome"
```

---

## Command-Line Arguments

- `-t`,	`--target` :	Target login URL(s). Supports multiple or comma-separated values
- `u`,	`--usernames` :	Path to username wordlist file
- `p` ,	`--passwords` :	Path to password wordlist file
- `l`, `--login` :	String that appears in the response when login is successful

---

## How It Works
1. Loads usernames and passwords from wordlist files
2. Iterates through each target URL
3. Sends POST requests with credentials (uname and pass)
4. Checks server response for a success indicator string
5. Stops when valid credentials are found or when testing completes

---

## Project Structure
```
EZ_Brute/
├── tool.py
├── my_banner.py
├── assets/
│   └── screenshot_1.png
│   └── screenshot_2.png
├── users.txt
├── passwords.txt
└── README.md
```

---

## Notes
The POST parameters are hardcoded as:

```python
data={"uname": user, "pass": pwd}
```

Modify these if your target application uses different field names.
Network timeouts and failed requests are safely handled.
The tool stops once valid credentials are found.

---

## Disclaimer

This software is provided for educational and defensive security purposes only.
The author assumes no liability for misuse or damage caused by this tool.

Always follow local laws and obtain explicit written permission before testing any system.

