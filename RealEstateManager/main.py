import funzionalita as f
     
#dizionario per definire i comandi disponibili
switcher = {
    "1": f.casa,
    "2": f.in_vendita,
    "3": f.non_in_vendita,
    "4": f.cerca_casa,
    "5": f.aggiungi_casa,
    "6": f.modifica_casa,
    "7": f.zone,
    "8": f.aggiungi_zona,
    "9": f.citta,
    "10": f.aggiungi_citta,
    "11": f.rimuovi_citta,
    "12": f.probabilita_vendita,
    "13": f.domanda,
    "14": f.valutazione_di_sistema,
    "-1": f.mainMenu
    }

#funzione per accedere al dizionario
def switch(command):
    return switcher.get(command, f.default)()

#funzione iniziale main
if __name__ == '__main__':
    f.firstMessage()
    f.chatBotHelp()
    command = "1"
    
    while (command != "0"):
        command = input("Comando inserito -> ")
        
        if(command != "0"):
            switch(command)
    
    f.esci()
        