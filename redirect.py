import csv
import requests


def get_redirected_domain(url):
    try:
        response = requests.get(url, allow_redirects = True, timeout = 5)
        if response.history:
            return response.url  
        return url  
    except requests.RequestException:
        return 'Error!'


def process_domains(input_file, output_file):
    with open(input_file, 'r') as file, open(output_file, 'w', newline = '') as out_file:
        reader = file.readlines()
        writer = csv.writer(out_file)
        writer.writerow(["Original domain", "Redirected domain"])
        # Looping through the domains.
        for domain in reader:
            domain = domain.strip()
            if not domain.startswith('http'):
                domain = "https://" + domain  # Adding HTTPS if it's missing.
            redirected = get_redirected_domain(domain)
            writer.writerow([domain, redirected])
            print(f"{domain} -> {redirected}")


if __name__ == '__main__':
    process_domains("domains.txt", "redirected_domains.csv")
