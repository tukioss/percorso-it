import re
import pandas as pd
import sys

# Funzione per leggere e analizzare il log
def analizza_log(nome_file):
    print(f"Analisi del file di log: {nome_file}")

    # Regex per estrarre: (Timestamp), (Status: Accepted o Failed), e (Indirizzo IP)
    # Le parentesi (...) creano "gruppi di cattura" per isolare le parti che ci interessano.
    pattern = re.compile(r"(\w+\s+\d+\s+\d{2}:\d{2}:\d{2}).*?(Accepted|Failed) password.*?from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

    dati_estratti = [] # Una lista vuota per contenere i nostri dizionari

    try:
        with open(nome_file, 'r') as file:
            for riga in file:
                corrispondenza = pattern.search(riga)
                if corrispondenza:
                    # Estraiamo i dati dai gruppi catturati dalla regex
                    timestamp = corrispondenza.group(1)
                    status = corrispondenza.group(2)
                    ip = corrispondenza.group(3)

                    # Creiamo un dizionario per questa riga e lo aggiungiamo alla lista
                    dati_estratti.append({
                        "timestamp": timestamp,
                        "status": status,
                        "ip_address": ip
                    })

        print(f"Trovate {len(dati_estratti)} voci di log pertinenti.")
        return dati_estratti # La funzione ora restituisce la lista di dati

    except FileNotFoundError:
        print(f"ERRORE: File '{nome_file}' non trovato.")
        return None # Restituiamo 'None' (niente) se c'è un errore


# Funzione per generare un report dai dati analizzati
def genera_report(dati):
    print("\n--- Generazione Report di Sicurezza ---")

    # Controlliamo se abbiamo dati da analizzare
    if not dati:
        print("Nessun dato pertinente trovato per generare il report.")
        return # Usciamo dalla funzione se la lista 'dati' è vuota

    # 1. Convertiamo la nostra lista di dizionari in un DataFrame Pandas
    df = pd.DataFrame(dati)

    # 2. Analisi: Contiamo gli accessi riusciti ("Accepted") e falliti ("Failed")
    conteggio_status = df['status'].value_counts()
    print("\n[1] Riepilogo Tentativi di Accesso:")
    print(conteggio_status)

    # 3. Analisi: Troviamo gli IP con più tentativi falliti
    # Prima filtriamo la tabella per avere solo gli accessi con stato 'Failed'
    accessi_falliti_df = df[df['status'] == 'Failed']
    # Poi contiamo le occorrenze di ogni IP in questa nuova tabella
    conteggio_ip_falliti = accessi_falliti_df['ip_address'].value_counts()

    print("\n[2] Top Indirizzi IP con Tentativi Falliti:")
    # .head(3) ci mostra solo i primi 3 risultati
    print(conteggio_ip_falliti.head(3))

    # 4. Salviamo il DataFrame completo in un nuovo file CSV
    nome_file_report = "report_sicurezza.csv"
    try:
        df.to_csv(nome_file_report, index=False) # index=False evita di scrivere l'indice numerico di Pandas
        print(f"\nReport dettagliato salvato con successo in: {nome_file_report}")
    except Exception as e:
        print(f"\nErrore durante il salvataggio del report: {e}")

# --- Blocco Principale del Programma ---
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_di_log = sys.argv[1]
        
        # 1. Esegui l'analisi e ottieni i dati
        dati_estratti = analizza_log(file_di_log)
        
        # 2. Passa i dati alla funzione di report
        genera_report(dati_estratti)
        
    else:
        print("Errore: Fornire il nome del file di log come argomento.")
        print("Esempio: python3 security_analyzer.py auth.log")

