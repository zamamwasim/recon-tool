#!/usr/bin/env python3

import argparse
from datetime import datetime
from modules import whois, dns_enum, subdomain_enum

def save_report(domain, report_data):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/{domain.replace('.', '_')}_report_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(report_data)
    print(f"\n[+] Report saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Custom Reconnaissance Tool")
    parser.add_argument("target", help="Target domain or IP")
    parser.add_argument("--whois", action="store_true", help="Perform WHOIS lookup")
    parser.add_argument("--dns", action="store_true", help="DNS Enumeration")
    parser.add_argument("--subdomains", action="store_true", help="Subdomain Enumeration")
    parser.add_argument("--ports", action="store_true", help="Port Scanning")
    parser.add_argument("--banner", action="store_true", help="Banner Grabbing")
    parser.add_argument("--report", action="store_true", help="Save output to report")

    args = parser.parse_args()
    domain = args.target
    output = f"Recon Report for: {domain}\nGenerated on: {datetime.now()}\n\n"

    if args.whois:
        print("[*] Running WHOIS Lookup...")
        result = whois.run(domain)
        output += "[WHOIS Lookup]\n" + result + "\n\n"

    if args.dns:
        print("[*] Running DNS Enumeration...")
        result = dns_enum.run(domain)
        output += "[DNS Enumeration]\n"
        for rtype, records in result.items():
            output += f"{rtype} Records: {records}\n"
        output += "\n"

    if args.subdomains:
        print("[*] Running Subdomain Enumeration...")
        result = subdomain_enum.run(domain)
        output += "[Subdomain Enumeration]\n" + "\n".join(result) + "\n\n"

    if args.ports:
        from modules import port_scanner
        print("[*] Running Port Scanner...")
        result = port_scanner.run(domain)
        output += "[Open Ports]\n" + "\n".join(result) + "\n\n"

    if args.banner:
        from modules import banner_grab
        print("[*] Running Banner Grabbing...")
        banners = banner_grab.run(domain)
        output += "[Banners]\n" + "\n".join(banners) + "\n\n"

    if args.report:
        save_report(domain, output)
    else:
        print("\n--- Recon Output ---\n")
        print(output)

if __name__ == "__main__":
    main()
