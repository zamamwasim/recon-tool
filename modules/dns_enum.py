import dns.resolver

def run(domain):
    record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'TXT']
    results = {}

    for record in record_types:
        try:
            answer = dns.resolver.resolve(domain, record)
            results[record] = [r.to_text() for r in answer]
        except:
            results[record] = ["No Answer"]
    return results

