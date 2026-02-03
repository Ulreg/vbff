Del 1: Basis – Tjek en liste af enheder
Her tjekker vi en fast liste af IP-adresser. Det er smart, hvis man vil holde øje med specifikke servere.
Koden forklares:
import os: Giver Python lov til at bruge Linux-kommandoer.
for ip in ...: En løkke der tager én IP ad gangen.
os.system(...): Udfører selve ping-kommandoen.
Skriv denne kode i en fil kaldet scanner.py:
Python

import os

# Liste over IP'er vi vil tjekke
ip_liste = ["192.168.1.1", "8.8.8.8", "10.0.0.1"]

print("--- Starter Scanning ---")

for ip in ip_liste:
    # Vi sender 1 ping-pakke. 
    # Vi sender resultatet ud i 'intetheden' (> /dev/null), så skærmen ikke fyldes med tekst.
    respons = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    
    if respons == 0:
        print(f"[+] {ip} er OPPE (Svarer)")
    else:
        print(f"[-] {ip} er NEDE (Svarer ikke)")


Udvidet – Scan hele netværket

Nu skal vi lave koden om, så den scanner alle adresser fra 1 til 254 automatisk. Det kaldes et "Sweep".
Sådan gør du:
Vi bruger range(1, 255) til at tælle fra 1 til 254.
Vi sætter tallet ind i IP-adressen med {i}.
Skriv denne kode:
Python
import os

netvaerk = "192.168.1"  # De første tre dele af IP'en
print(f"Scanner hele netværket: {netvaerk}.x ...")

# range(1, 255) giver os tallene 1, 2, 3 ... op til 254
for i in range(1, 255):
    ip = f"{netvaerk}.{i}" # Samler IP'en, f.eks. 192.168.1.55
    
    # Scanner kun hurtigt (timeout sat lavt med -W 1 for at spare tid)
    respons = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
    
    if respons == 0:
        print(f"[FUNDET!] Enhed aktiv på: {ip}")
