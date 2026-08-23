import hashlib
import json
import socket

MASTER_HOST = "127.0.0.1"
MASTER_PORT = 5000


def sha256d(value):
    return hashlib.sha256(hashlib.sha256(value.encode()).digest()).hexdigest()


def mine(start_nonce, end_nonce, block_data):
    for nonce in range(start_nonce, end_nonce):
        raw = f"{block_data['previous_hash']}{nonce}"
        current_hash = sha256d(raw)
        if current_hash < block_data["target"]:
            return nonce, current_hash
    return None, None


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((MASTER_HOST, MASTER_PORT))

    data = sock.recv(4096).decode()
    payload = json.loads(data)

    block_data = payload["block_data"]
    start_nonce = payload["start_nonce"]
    end_nonce = payload["end_nonce"]

    print(f"Worker mining range: {start_nonce} - {end_nonce}")

    nonce, found_hash = mine(start_nonce, end_nonce, block_data)

    result = {
        "nonce": nonce,
        "hash": found_hash,
    }

    sock.sendall(json.dumps(result).encode())
    sock.close()


if __name__ == "__main__":
    main()
