import requests
from colorama import Fore, Style

def brute_force_url(base_url, wordlist):
    if not base_url.startswith("https://"):
        if not base_url.startswith("http://"):
            base_url = "https://" + base_url
        elif base_url.startswith("http://"):
            print(f"{Fore.YELLOW}[WARNING]: Using 'http://' is not secure. Advised switching to 'https://'." + Style.RESET_ALL)
            switch = input("[USER] Do you still wish to continue with 'http://'? (y/n): ")
            if switch.lower() == "y":
                print(f"{Fore.GREEN}Continuing with 'http://'." + Style.RESET_ALL)
            elif switch.lower() == "n":
                print(f"{Fore.CYAN}[INFO] Switching to 'https://'." + Style.RESET_ALL)
                if base_url.startswith("http://"):
                    base_url = base_url.replace("http://","")
                base_url = "https://" + base_url
            else:
                print(f"{Fore.RED}Invalid input. Switching to 'https://'." + Style.RESET_ALL)
                base_url = "https://" + base_url

    try:
        with open(wordlist, 'r', encoding='latin-1') as f:
            paths = f.read().splitlines()
    except FileNotFoundError:
        print(f"{Fore.RED}{Style.BRIGHT}[ERROR] Wordlist file not found: {wordlist}{Style.RESET_ALL}")
        return

    for path in paths:
        url = base_url + '/' + path
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{Fore.GREEN}{Style.BRIGHT}[FOUND]{Style.RESET_ALL} {url}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}[NOT FOUND]{Style.RESET_ALL} {url}")

if __name__ == "__main__":
    base_url = input("[USER] Please enter the domain: ")
    wordlist = input("[INFO] Please enter the wordlist you wish to use: ")

    print(f"{Fore.YELLOW}*** Leave wordlist empty to use default wordlist ***")
    if wordlist == "":
        print(f"{Fore.CYAN}[INFO] Using Default wordlist")
        wordlist = "wordlist.txt"

    brute_force_url(base_url, wordlist)
