import requests
import subprocess
from concurrent.futures import ThreadPoolExecutor

def portscanner(r1, site, r):
     print(f"[+] Rodando nmap no subdomínio >> {r1}")
     try:
        results = subprocess.run(
            ["nmap", "-Pn", "-T4", r1],
            capture_output=True,
            text=True
        )
        print(results.stdout)
     except Exception as e:
        print(f"Erro ao rodar nmap em {r1}: {e}")
def check_subdomain(sub, site):
    url = f"https://{sub}.{site}"
    r1 = f"{sub}.{site}"
    try:
        r = requests.get(url, timeout=5)
        portscanner(r1, site, r)
    except requests.RequestException:
        pass

def main():
    site = input("Qual o host? (example.com)\n> ").strip()

    with open("textosub.txt", "r") as f:
        subs = f.read().splitlines()

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(lambda sub: check_subdomain(sub, site), subs)

if __name__ == "__main__":
    main()
