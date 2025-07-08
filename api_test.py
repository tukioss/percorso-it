import requests

# L'URL dell'API che vogliamo chiamare
url = "https://jsonplaceholder.typicode.com/users/1"

print(f"Sto effettuando una richiesta all'URL: {url}")

try:
    # Eseguiamo la richiesta GET
    risposta = requests.get(url)

    # Controlliamo se la richiesta è andata a buon fine
    risposta.raise_for_status()

    # Convertiamo la risposta da JSON a dizionario Python
    dati_utente = risposta.json()

    # Stampiamo alcuni dati presi dal dizionario
    print("\n--- Dati Utente Ricevuti ---")
    print(f"Nome: {dati_utente['name']}")
    print(f"Email: {dati_utente['email']}")
    print(f"Città: {dati_utente['address']['city']}")
    print("---------------------------")

except requests.exceptions.RequestException as e:
    print(f"ERRORE: Impossibile completare la richiesta. Errore: {e}")
