import socket
import json
import time
import random

host = "logstash"
port = 5000

# Retry loop for socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        sock.connect((host, port))
        break
    except ConnectionRefusedError:
        print("Waiting for Logstash to be ready...")
        time.sleep(2)

levels = ["INFO", "WARN", "DEBUG", "ERROR"]
messages = ["User login", "File not found", "DB connection failed", "Data saved"]

while True:
    log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "level": random.choice(levels),
        "message": random.choice(messages),
        "user": f"user{random.randint(1,5)}"
    }
    sock.send((json.dumps(log) + "\n").encode())
    time.sleep(1)
