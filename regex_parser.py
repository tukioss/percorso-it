import re
def trova_ip_nel_log(nome_file):
    pattern_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    print(f"--- Inizio ricerca IP nel file: {nome_file} ---\n")
    try:
        with open(nome_file, 'r') as file:
            for numero_riga, riga in enumerate(file,1):
                corrispondenza = re.search(pattern_ip, riga)
                if corrispondenza:
                    ip_trovato = corrispondenza.group (0)
                    print(f"Riga {numero_riga}: Trovato IP -> {ip_trovato}")
    except FileNotFoundError:
        print(f"ERRORE: file '{nome_file}' non trovato.")
trova_ip_nel_log("sample_log.txt")
