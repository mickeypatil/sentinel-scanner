# scanner/port_scanner.py

import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        
        # Try to grab banner
        try:
            sock.sendall(b"Hello\r\n")
            banner = sock.recv(1024).decode().strip()
        except:
            banner = "Unknown Service"

        print(f"{Fore.GREEN}[+] Port {port} is open | Service: {banner}{Style.RESET_ALL}")
        sock.close()
    except:
        pass


def main():
    print("=== Sentinel Port Scanner ===")
    target = input("Enter IP address or domain: ").strip()
    
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{Fore.RED}[-] Invalid domain or IP{Style.RESET_ALL}")
        return

    ports = range(1, 1025)  # Scans first 1024 ports (common range)
    print(f"Scanning {ip} ...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, ip, port)

if __name__ == "__main__":
    main()
