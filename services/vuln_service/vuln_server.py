#!/usr/bin/env python3
"""
Serviço vulnerável educacional para prática de pentesting
USAR APENAS EM AMBIENTE CONTROLADO
"""
import socket
import threading
import subprocess
import base64
import os

HOST = '0.0.0.0'
PORT = 9999
ADMIN_PASSWORD = "admin123"  # senha fraca proposital

# Flag escondida para prática de CTF
FLAG = "FLAG{nmap_lab_pwned}"

def handle_client(conn, addr):
    """Manipula conexão do cliente com múltiplas vulnerabilidades"""
    authenticated = False
    
    try:
        # Banner com informações sensíveis (information disclosure)
        banner = b"""
========================================
VulnService v0.0.2 (Build 2025-12-07)
Running on: Alpine Linux 3.18
Python: 3.11.6
Admin Panel Access Available
========================================
Commands: help, login, ping, base64, exec, flag, exit
> """
        conn.sendall(banner)
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
                
            cmd = data.strip().decode('utf-8', errors='ignore')
            parts = cmd.split(maxsplit=1)
            command = parts[0].lower() if parts else ""
            args = parts[1] if len(parts) > 1 else ""
            
            # Comando HELP
            if command == 'help':
                help_text = b"""
Available commands:
  help          - Show this help
  login <pass>  - Admin authentication (required for some commands)
  ping <host>   - Ping a host (admin only)
  base64 <text> - Encode text to base64
  exec <cmd>    - Execute system command (admin only)
  flag          - Get the flag (admin only)
  exit          - Close connection
> """
                conn.sendall(help_text)
            
            # VULNERABILIDADE 1: Autenticação com senha fraca
            elif command == 'login':
                if args == ADMIN_PASSWORD:
                    authenticated = True
                    conn.sendall(b"[+] Authentication successful!\n> ")
                else:
                    conn.sendall(b"[-] Authentication failed!\n> ")
            
            # VULNERABILIDADE 2: Command Injection via ping
            elif command == 'ping':
                if not authenticated:
                    conn.sendall(b"[-] Admin authentication required\n> ")
                    continue
                    
                # Vulnerável a command injection (;, &&, ||)
                try:
                    result = subprocess.check_output(
                        f"ping -c 1 {args}",
                        shell=True,  # VULNERÁVEL!
                        stderr=subprocess.STDOUT,
                        timeout=5
                    )
                    conn.sendall(result)
                except subprocess.TimeoutExpired:
                    conn.sendall(b"[-] Timeout\n")
                except Exception as e:
                    conn.sendall(f"[-] Error: {str(e)}\n".encode())
                conn.sendall(b"> ")
            
            # VULNERABILIDADE 3: Base64 decode sem sanitização (path traversal potencial)
            elif command == 'base64':
                try:
                    encoded = base64.b64encode(args.encode()).decode()
                    conn.sendall(f"[+] Encoded: {encoded}\n> ".encode())
                except Exception as e:
                    conn.sendall(f"[-] Error: {str(e)}\n> ".encode())
            
            # VULNERABILIDADE 4: Execução arbitrária de comandos (backdoor)
            elif command == 'exec':
                if not authenticated:
                    conn.sendall(b"[-] Admin authentication required\n> ")
                    continue
                
                try:
                    result = subprocess.check_output(
                        args,
                        shell=True,
                        stderr=subprocess.STDOUT,
                        timeout=5
                    )
                    conn.sendall(result)
                except Exception as e:
                    conn.sendall(f"[-] Error: {str(e)}\n".encode())
                conn.sendall(b"> ")
            
            # FLAG para CTF
            elif command == 'flag':
                if authenticated:
                    conn.sendall(f"[+] {FLAG}\n> ".encode())
                else:
                    conn.sendall(b"[-] Admin authentication required\n> ")
            
            # EXIT
            elif command == 'exit':
                conn.sendall(b"[+] Goodbye!\n")
                break
            
            else:
                conn.sendall(b"[-] Unknown command. Type 'help' for available commands\n> ")
                
    except Exception as e:
        print(f"[!] Error handling client {addr}: {e}")
    finally:
        conn.close()
        print(f"[*] Client {addr} disconnected")

def main():
    """Inicia o servidor vulnerável"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    
    print(f"[*] VulnService listening on {HOST}:{PORT}")
    print(f"[*] Press Ctrl+C to stop")
    
    try:
        while True:
            conn, addr = server.accept()
            print(f"[+] New connection from {addr}")
            client_thread = threading.Thread(
                target=handle_client,
                args=(conn, addr),
                daemon=True
            )
            client_thread.start()
    except KeyboardInterrupt:
        print("\n[*] Shutting down server...")
    finally:
        server.close()

if __name__ == "__main__":
    main()