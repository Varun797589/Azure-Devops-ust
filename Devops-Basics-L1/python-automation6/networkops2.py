
import socket

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=3):
            print(f"{host}:{port} is OPEN")
    except:
        print(f"{host}:{port} is CLOSED")

check_port("google.com", 80)
check_port("google.com", 443)

