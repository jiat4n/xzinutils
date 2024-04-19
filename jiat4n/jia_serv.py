import socket

def main():
    host = '0.0.0.0'  # Listen on all interfaces
    port = 8080  # Choose your desired port
    response = b'Author: Jia T4n\n'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Listening on {host}:{port}...")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            conn.sendall(response)

if __name__ == "__main__":
    main()
