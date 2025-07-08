import os
def analizza_file_ip(nome_del_file):
    print(f"--- Inizio analisi del file: {nome_del_file} ---")
    try:
        with open(nome_del_file, 'r') as file:
            for riga in file:
               ip = riga.strip()
               if ip:
                     print(f"Simulazione ping per l'IP: {ip}... Risposta ricevuta!")

    except FileNotFoundError:
           print(f"ERRORE: Il file '{nome_del_file}' non è stato trovato.")
print("---Fine analisi ---")
analizza_file_ip("ips.txt")


