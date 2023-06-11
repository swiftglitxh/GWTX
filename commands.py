import os
import subprocess
import cmd
from colorama import Fore, Style
from time import sleep
import importlib
from tools.locate import get_ip_location
from tools.brutefinder import brute_force_url
from tools.ssh import ssh

# List of required packages
required_packages = ["colorama"]

print(f"{Fore.CYAN}{Style.BRIGHT}[packages] Checking for packages.{Style.RESET_ALL}")
sleep(1)

# Check if each package is installed
for package in required_packages:
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL} Package '{package}' is not installed.")
        install = input(f"Would you like to install {package}? (y/n) ")
        if install.lower() == "y":
            subprocess.call(['pip', 'install', package])

print(f"{Fore.GREEN}{Style.BRIGHT}[packages] All required packages are installed.{Style.RESET_ALL}")
sleep(1)

class MyConsole(cmd.Cmd):
    prompt = f"{Fore.CYAN}{Style.BRIGHT}gwtx > {Style.RESET_ALL}"
    ip_address = ""
    payload = ""

    def banner(self):
        print(f'''
        \t\t        _,.-------.,_
        \t\t     ,;~'             '~;,
        \t\t   ,;                     ;,
        \t\t  ;                         ;
        \t\t ,'                         ',
        \t\t,;                           ;,
        \t\t; ;      .           .      ; ;
        \t\t| ;   ______       ______   ; |
        \t\t|  `/~"     ~" . "~     "~\'  |
        \t\t|  ~  ,-~~~^~, | ,~^~~~-,  ~  |
        \t\t |   |        ):(        |   |
        \t\t |   l       / | \       !   |
        \t\t .~  (__,.--" .^. "--.,__)  ~.
        \t\t |     ---;' / | \ `;---     |
        \t\t  \__.       \/^\/       .__/
        \t\t   V| \                 / |V
        \t\t    | |T~\___!___!___/~T| |
        \t\t    | |`IIII_I_I_I_IIII'| |
        \t\t    |  \,III I I I III,/  |
        \t\t     \   `~~~~~~~~~~'    /
        \t\t       \   .       .   /
        \t\t         \.    ^    ./
        \t\t           ^~~~^~~~^      {Fore.RED}
                      .Gt
                     j#W:           ;        GEEEEEEEL
                   ;K#f           .DL        ,;;L#K;;.:KW,      L
                 .G#D.    f.     :K#L     LWL   t#E    ,#W:   ,KG
                j#K;      EW:   ;W##L   .E#f    t#E     ;#W. jWi
              ,K#f   ,GD; E#t  t#KE#L  ,W#;     t#E      i#KED.
               j#Wi   E#t E#t f#D.L#L t#K:      t#E       L#W.
                .G#D: E#t E#jG#f  L#LL#G        t#E     .GKj#K.
                  ,K#fK#t E###;   L###j         t#E    iWf  i#K.
                    j###t E#K:    L#W;          t#E   LK:    t#E
                     .G#t EG      LE.            fE   i       tDj
                       ;; ;       ;@              :              \n
{Fore.YELLOW}{Style.BRIGHT}    *** Welcome to the GWTX console! Type 'help' for available commands ***{Style.RESET_ALL}\n
[\tThis tool is a custom console designed for exploiting targets \t\t]\n[    and performing various network-related tasks.It provides a command-line\t]\n[\t  interface for executing commands and managing options.\t\t]\n''')
 # If all packages are installed
    def do_help(self, args):
        """Show available commands"""
        print('''
    Commands                   Description
    ========                   ===========
    help                    Show available commands
    exploit <target>        Exploit a target
    set ip <value>          Set the IP address
    set payload <value>     Set payload
    show payloads           Show payloads available
    scan                    Scan IP for open ports
    ssh                     Connect to machine with SSH
    clear                   Clear the screen
    exit                    Exit the console
________________________________________________________\n
The 'use' command is used to set an option.

Usage:
use <option>

Options:
- ssh: Use SSH force mode

Example:
gwtx > use ssh''')

    def do_exploit(self, args):
        """Exploit a target"""
        if not self.ip_address:
            pass 
        else:
            print(f"{Fore.YELLOW}{Style.BRIGHT}[info] Starting Exploit On  {Style.RESET_ALL}{self.ip_address}")
            sleep(1)
        
        if self.payload == "":
            print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL} Payload not set. Please use 'set payload <value>' command to set the payload.")
        else:
            if not os.path.exists(self.payload):
                print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL} Payload file '{self.payload}' does not exist.")
            else:
                print(f"{Fore.YELLOW}{Style.BRIGHT}[info] Running payload '{Fore.RED}{Style.NORMAL}{self.payload}{Fore.YELLOW}{Style.BRIGHT}' against target: {Style.RESET_ALL}{self.ip_address}")
                # Execute the payload Python script
                if self.payload == "tools/locate.py":
                    get_ip_location(self.ip_address)
                elif self.payload == "tools/ssh.py":
                    ssh()

    def do_set(self, args):
        """Set an option"""
        parts = args.split()
        if len(parts) != 2:
            print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL} Invalid arguments for 'set' command. Usage: set <option> <value>")
        else:
            option, value = parts
            if option == "ip":
                self.ip_address = value
                print(f"{Fore.YELLOW}{Style.BRIGHT}[info]{Style.RESET_ALL} --> Set {option} to {value}")
            elif option == "payload":
                self.payload = "tools/" + value + ".py"
                print(f"{Fore.YELLOW}{Style.BRIGHT}[info]{Style.RESET_ALL} --> Set {option} to {value}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL} Unknown option '{option}'")

    def do_use(self, args):
        """Set an option"""
        use = ['ssh','dictFinder']
        parts = args.split()
        if len(parts) != 1:
            print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL} Invalid arguments for 'use' command. Usage: use <option>")
        else:
            option = parts[0]
            if option == "ssh":
                print(f"{Fore.YELLOW}{Style.BRIGHT}[info]{Style.RESET_ALL} --> Now using {option}")
                print(f"{Fore.YELLOW}{Style.BRIGHT}*** Now using SSH.{Style.RESET_ALL}")
                ssh()
            if option == "-h":
                print(f"\n{Fore.YELLOW}{Style.BRIGHT}Available Options:{Style.RESET_ALL}")
                print(f"{'-' * 65}\n {'Options Available':<30}\n{'-' * 65}")
                for count, value in enumerate(use,start=1):
                    print(count, value)
                print('\nExample:\n gwtx > use dictFinder\n')

            elif option == "dictFinder":
                base_url = input(f"{Fore.CYAN}{Style.BRIGHT}[user]{Style.RESET_ALL}  Please enter the domain: ")
                wordlist = input(f"{Fore.YELLOW}{Style.BRIGHT}[info]{Style.RESET_ALL}  Please enter the wordlist you wish to use: ")
                brute_force_url(base_url, wordlist)
            else:
                print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL} {option} is not an option. Please type 'use -h' for options.")
    def do_ssh(self, args):
        ip = args.strip()

        if not ip:
            print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL}  IP address is required")
            return

        hostkey_algorithms = "ssh-rsa,ssh-dss"  # Add the supported algorithms here
        command = ['ssh', '-o', f'HostKeyAlgorithms={hostkey_algorithms}', ip]

        try:
            subprocess.call(command)
        except subprocess.CalledProcessError as e:
            error_output = e.output.decode().strip()
            if "no matching host key type found" in error_output:
                print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL}  {error_output}")
                # Perform actions specific to the error
            else:
                print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL} {error_output}")

    def do_run(self, args):
        """Run the exploit"""
        if self.ip_address == "":
            print(f"{Fore.RED}{Style.BRIGHT}[Error]{Style.RESET_ALL} No IP address was provided. Type 'help' for available commands.")
        else:
            print("Running exploit with options:", args)

    def do_sniff(self, args):
        """Run the sniff command"""
        print("Running the sniff command")

    def do_ping(self, args):
        parts = args.split()
        if len(parts) != 1:
            print(f"{Fore.RED}{Style.BRIGHT}[error] {Style.RESET_ALL} Invalid arguments for 'ping' command. Usage: ping <ip>")
        else:
            ip = parts[0]
            print(f"{Fore.YELLOW}{Style.BRIGHT}[info]{Style.RESET_ALL}  pinging {ip}")
            subprocess.call(['ping', '-c', '4', ip])
            print(f"{Fore.CYAN}{Style.BRIGHT}[success]{Style.RESET_ALL} complete pinging {ip}")

    def do_scan(self, args):
        if self.ip_address == "":
            print(f"{Fore.RED}{Style.BRIGHT}[error]IP address not set. Please use 'set ip <value>' command to set the IP address.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}{Style.BRIGHT}[info] Scanning {Style.RESET_ALL}{self.ip_address}{Fore.YELLOW}{Style.BRIGHT} ports{Style.RESET_ALL}")
            subprocess.call(['nmap', self.ip_address])
            print(f"{Fore.CYAN}{Style.BRIGHT}[complete]{Style.RESET_ALL} Scan complete")

    def do_lookup(self, args):
        """Perform DNS lookup"""
        if self.ip_address == "":
            print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL}  IP address not set. Please use 'set ip <value>' command to set the IP address.")
        else:
            print(f"{Fore.YELLOW}{Style.BRIGHT}[info] Performing DNS lookup for IP: {Style.RESET_ALL}{self.ip_address}")
            subprocess.call(['nslookup', self.ip_address])

    def do_show(self, args):
        """Show current option values"""
        if args == "options":
            self.show_options(args)
        elif args == "payloads":
            self.show_payloads(args)
        else:
            print(f"{Fore.RED}{Style.BRIGHT}[error]{Style.RESET_ALL}  Unknown command 'show {args}'")

    def show_options(self, args):
        print(f'''
IP       : {self.ip_address}
Payload  : {self.payload}''')

    def show_payloads(self, args):
        directory = "tools/"  # Assuming the directory path is passed as an argument
        # Check if the directory exists
        if os.path.isdir(directory):
            # List all files in the directory
            files = os.listdir(directory)

            # Payload descriptions
            payload_descriptions = {
                "locate": "Locate IP location",
                "ssh": "SSH to another machine"
            }

            # Print the payloads in a formatted table
            print(f"\n{Fore.YELLOW}{Style.BRIGHT}Available Payloads:{Style.RESET_ALL}")
            print(f"{'-' * 65}\n{'Payload':<30}{'Description':<35}\n{'-' * 65}")
            for file in files:
                if file.endswith(".py"):
                    payload_name = file[:-3]
                    payload_description = payload_descriptions.get(payload_name, "No description available")
                    print(f"{payload_name:<30}{payload_description:<35}")

            print(f"\n{Fore.YELLOW}{Style.BRIGHT}Use 'set payload <payload_name>' to set the payload{Style.RESET_ALL}")
        else:
            print("Invalid directory path.")

    def do_exit(self, args):
        """Exit the console"""
        print("Exiting...")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_clear(self, args):
        """Clear the console"""
        os.system("clear")
        self.banner()

