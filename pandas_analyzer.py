# Si importa pandas usando l'alias 'pd'. È una convenzione standard mondiale.
import pandas as pd

NOME_FILE = "vendite.csv"

try:
    # 1. Carichiamo i dati dal file CSV in un DataFrame Pandas
    df = pd.read_csv(NOME_FILE)

    print("--- Analisi Dati di Vendita con Pandas ---")
    
    # 2. Mostriamo le prime 5 righe della nostra tabella per un'anteprima
    print("\n[1] Prime 5 righe del file:")
    print(df.head())

    # 3. Creiamo una nuova colonna 'Fatturato' calcolandola dalle altre
    df['Fatturato'] = df['Quantita'] * df['Prezzo']

    # 4. Filtriamo la tabella per vedere solo le vendite dei 'Laptop'
    laptop_df = df[df['Prodotto'] == 'Laptop']
    print("\n[2] Dati filtrati solo per 'Laptop':")
    print(laptop_df)

    # 5. Calcoliamo il fatturato totale di tutti i prodotti
    fatturato_totale = df['Fatturato'].sum()
    print(f"\n[3] Fatturato Totale di tutti i prodotti: {fatturato_totale} EUR")

except FileNotFoundError:
    print(f"ERRORE: File '{NOME_FILE}' non trovato.")
except Exception as e:
    # Un gestore di errori generico per altri problemi con Pandas
    print(f"Si è verificato un errore inaspettato: {e}")

