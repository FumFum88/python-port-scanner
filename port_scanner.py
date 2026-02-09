# Python Port Scanner
# Author: FumFum88
import socket

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((ip, port))

    if result == 0:
        print("[+] Port", port, "OPEN")

    s.close()


def main():
    ip = input("Enter target IP: ")

    print("\nStarting scan on", ip)
    print("-" * 30)

    for port in range(1, 101):
        scan_port(ip, port)

    print("\nScan completed")


if __name__ == "__main__":
    main()
