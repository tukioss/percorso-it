def saluta_utente(nome):
    if nome == "Tullio":
       print(f"-> Ciao {nome}! Il creatore dello script.")
    elif nome == "Marco":
       print(f"-> Ciao {nome}! Il nome utente del server.")
    else:
       print(f"-> Ciao {nome}! Un nome nuovo, benvenuto!")
print ("Sto per eseguire la mia funzione più volte...")
saluta_utente ("Tullio")
saluta_utente("Marco")
saluta_utente("Anna")
saluta_utente("Mario")

print("Esecuzione terminata")

