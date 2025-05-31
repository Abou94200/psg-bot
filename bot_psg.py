import requests
from bs4 import BeautifulSoup

URL = 'https://billetterie.psg.fr/fr/abonnements'

def check_abonnements():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    if "Abonnements 2025/2026" in soup.text:
        print("🎉 Les abonnements PSG 2025/2026 sont ouverts !")
    else:
        print("❌ Pas encore ouverts.")

check_abonnements()
