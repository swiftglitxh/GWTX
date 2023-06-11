import paramiko
from time import sleep 
from colorama import Fore, Style
host = ""
def execute_ssh_command(ssh_client):
    sleep(1)
    print(f'{Fore.CYAN}{Style.BRIGHT}[sucess] Connected to {host} Successfully{Style.RESET_ALL}')
    sleep(1)
    # Execute SSH command
    while True:
        command = input("Enter a command to execute (or 'exit' to quit): ")
        if command == "exit":
            break
        else:
            try:
                stdin, stdout, stderr = ssh_client.exec_command(command)
                output = stdout.read().decode()
                error = stderr.read().decode()

                if output:
                    print(output)
                if error:
                    print(error)

            except paramiko.SSHException as ssh_ex:
                print(f"Error while executing SSH command: {str(ssh_ex)}")
def ssh():

    try:
        # Set SSH credentials
        host = input("HOST: ")
        port = 22
        username = input("USERNAME: ")
        password = input("PASSWORD: ")

        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SSH server
        ssh_client.connect(host, port=port, username=username, password=password)

        # Execute SSH command
        execute_ssh_command(ssh_client)

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your SSH credentials.")
        try_again = input("[+] Do you want to try again (y/n) > ")
        if try_again.lower() == "y":
            return ssh()
        else:
            pass
    except paramiko.SSHException as ssh_ex:
        print(f"Error while establishing SSH connection: {str(ssh_ex)}")
    except paramiko.ssh_exception.NoValidConnectionsError: 
        print(f"Error while establishing SSH connection")
    finally:
        # Close the SSH connection
        if ssh_client is not None:
            ssh_client.close()
