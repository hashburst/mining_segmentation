import hashlib
import json
import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

block_data = {
    "previous_hash": "0000000000000000abc123...",
    "target": "00000fffffffffffffffffffffffffffffffffffffff",
    "difficulty": 5,
}

TOTAL_NONCE = 100_000
SEGMENT_SIZE = 20_000
worker_id = 0


def sha256d(value):
    return hashlib.sha256(hashlib.sha256(value.encode()).digest()).hexdigest()


def handle_worker(conn, addr, start_nonce, end_nonce):
    print(f"Worker connected: {addr}. Assigned range: {start_nonce} - {end_nonce}")

    payload = {
        "block_data": block_data,
        "start_nonce": start_nonce,
        "end_nonce": end_nonce,
    }
    conn.sendall(json.dumps(payload).encode())

    result = conn.recv(1024).decode()
    if result:
        data = json.loads(result)
        nonce = data.get("nonce")
        found_hash = data.get("hash")
        print(f"Worker result: {addr}. Hash: {found_hash}. Nonce: {nonce}")

    conn.close()


def main():
    global worker_id
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Master listening on port {PORT}")

    current_nonce = 0

    while current_nonce < TOTAL_NONCE:
        conn, addr = server.accept()
        start_nonce = current_nonce
        end_nonce = min(current_nonce + SEGMENT_SIZE, TOTAL_NONCE)
        current_nonce = end_nonce

        thread = threading.Thread(
            target=handle_worker,
            args=(conn, addr, start_nonce, end_nonce),
        )
        thread.start()


if __name__ == "__main__":
    main()
