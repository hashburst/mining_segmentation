import socket
import hashlib
import json
import time

MASTER_HOST = '127.0.0.1'
MASTER_PORT = 5000

def sha256d(s):
    return hashlib.sha256(hashlib.sha256(s.encode()).digest()).hexdigest()

def mine(start_nonce, end_nonce, block_data):
    for nonce in range(start_nonce, end_nonce):
        raw = f"{block_data['previous_hash']}{nonce}"
        h = sha256d(raw)
        if h < block_data['target']:
            return nonce, h
    return None, None

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((MASTER_HOST, MASTER_PORT))

    data = s.recv(4096).decode()
    payload = json.loads(data)

    block_data = payload["block_data"]
    start_nonce = payload["start_nonce"]
    end_nonce = payload["end_nonce"]

    print(f"[WORKER] Mining range {start_nonce} - {end_nonce}")

    nonce, found_hash = mine(start_nonce, end_nonce, block_data)

    result = {
        "nonce": nonce,
        "hash": found_hash
    }

    s.sendall(json.dumps(result).encode())
    s.close()

if __name__ == "__main__":
    main()
