config_server = {
    "nome_host" : "server-web-01",
    "ip" : "10.0.0.5",
    "servizi_attivi": ["HTTP", "SSH"],
    "admin" : "tullio",
    "online" : True
}
print("--- Report di configurazione Server---")
print (f"Nome Host: {config_server['nome_host']}")
print(f"Indirizzo IP : {config_server['ip']}")
print(f"Servizi: {config_server['servizi_attivi']}")
if config_server['online']:
    print("Stato: Il server è attualmente online")
else:
    print("Stato: IL SERVER è OFFLINE.")
print("---Fine Report ---")

