import requests
import datetime

# Definiamo i nomi dei file all'inizio per pulizia
FILE_SITI = "siti_da_controllare.txt"
FILE_LOG = "health_check.log"

# Funzione che controlla un singolo sito
def controlla_sito(url):
    try:
        # Aggiungiamo un timeout per non aspettare all'infinito
        risposta = requests.get(url, timeout=5)
        
        # Invece di raise_for_status, controlliamo il codice di stato
        if risposta.status_code == 200:
            return "ONLINE"
        else:
            # Restituisce lo stato esatto se non è 200 OK
            return f"ERRORE ({risposta.status_code})"
            
    except requests.exceptions.RequestException:
        # Se il sito non è raggiungibile (es. non esiste)
        return "IRRAGGIUNGIBILE"

# --- Programma Principale ---

# Otteniamo data e ora attuali per il log
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Apriamo il file di log in modalità 'a' (append) per aggiungere senza cancellare
with open(FILE_LOG, 'a') as log_file:
    log_file.write(f"\n--- Controllo eseguito il: {timestamp} ---\n")
    
    print(f"Leggo i siti da {FILE_SITI}...")
    with open(FILE_SITI, 'r') as siti_file:
        for sito in siti_file:
            url_pulito = sito.strip()
            if url_pulito:
                stato = controlla_sito(url_pulito)
                print(f"Controllo {url_pulito}... Stato: {stato}")
                # Scriviamo il risultato nel file di log
                log_file.write(f"{url_pulito}: {stato}\n")

print(f"\nControllo completato. Risultati aggiunti a {FILE_LOG}")
