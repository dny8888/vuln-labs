import socket
import threading

HOST = '0.0.0.0'
PORT = 9999

def handle(conn, addr):
    try:
        conn.sendall(b"Welcome to vuln service v0.1\\n")
        while True:
            conn.sendall(b"> ")
            data = conn.recv(1024)
            if not data:
                break
            cmd = data.strip().decode('utf-8', errors='ignore')
            if cmd.lower() == 'exit':
                conn.sendall(b"bye\\n")
                break
            # echo command back (vulnerable toy)
            conn.sendall(f"you said: {cmd}\\n".encode())
    except Exception as e:
        print("err", e)
    finally:
        conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print("vuln service listening on", PORT)
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=handle, args=(conn, addr), daemon=True)
        t.start()

if __name__ == "__main__":
    main()
