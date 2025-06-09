import socket

def run(ip):
    common_ports = [21, 22, 23, 25, 80, 110, 143, 443, 8080]
    results = []

    for port in common_ports:
        try:
            s = socket.socket()
            s.settimeout(2)
            s.connect((ip, port))
            banner = s.recv(1024).decode().strip()
            results.append(f"[{port}] {banner}")
            s.close()
        except:
            continue
    return results
