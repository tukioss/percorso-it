import requests
import sys 
def recupera_dati_utente(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    print(f"--- Richiesta per l'utente con ID: {user_id} ---")
    try:
        risposta = requests.get(url)
        risposta.raise_for_status()
        utente = risposta.json()
        print(f" Nome: {utente['name']}")
        print(f" Email: {utente['email']}")
        print(f" Città: {utente['address']['city']}")
    except requests.exceptions.RequestException as e:
        print(f" --> Errore nel recuperare l'utente {user_id}: {e}")
if len(sys.argv) > 1:
    id_da_cercare = sys.argv[1]
    recupera_dati_utente(id_da_cercare)
else:
    print("Nessun ID utente specificato. Recupero i dati per i primi 3 utenti.")
    for i in range (1, 4):
        recupera_dati_utente(i)

