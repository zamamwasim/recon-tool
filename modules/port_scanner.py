import socket

def run(domain, ports=range(1, 1025)):
    open_ports = []

    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        return [f"Unable to resolve domain: {domain}"]

    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(f"Port {port} is open")
            s.close()
        except Exception as e:
            continue

    return open_ports if open_ports else ["No open ports found"]

