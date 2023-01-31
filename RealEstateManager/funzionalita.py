import casa as c
import zona as z
import citta as ci
import classificatore as cs
import probabilita as p
from tabulate import tabulate
from pyswip import Prolog

prolog = Prolog()
prolog.consult("RealEstate.pl") 

#funzioni dei vari comandi disponibili
def casa():
    print("\n-------------------------------LISTA CASE-------------------------------\n\n")
    c.houseList()
    chatBotHelp()

def in_vendita():
    print("\n-------------------------------LISTA CASE IN VENDITA-------------------------------\n\n")
    c.forSaleList()
    chatBotHelp()

def non_in_vendita():
    print("\n-------------------------------LISTA CASE NON IN VENDITA-------------------------------\n\n")
    c.notForSaleList()
    chatBotHelp()

def cerca_casa():
    print("\n-------------------------------RICERCA CASA-------------------------------\n\n")
    c.findHouse()
    chatBotHelp()

def aggiungi_casa():
    print("\n-------------------------------AGGIUNTA CASA-------------------------------\n\n")
    c.addHouse()
    chatBotHelp()

def modifica_casa():
    print("\n-------------------------------MODIFICA CASA-------------------------------\n\n")
    c.modifyHouse()
    chatBotHelp()

def zone():
    print("\n-------------------------------LISTA ZONE-------------------------------\n\n")
    z.zoneList()
    chatBotHelp()

def aggiungi_zona():
    print("\n-------------------------------AGGIUNTA ZONA-------------------------------\n\n")
    z.addZone()
    chatBotHelp()

def citta():
    print("\n-------------------------------LISTA CITTA-------------------------------\n\n")
    ci.cityList()
    chatBotHelp()


def aggiungi_citta():
    print("\n-------------------------------AGGIUNTA CITTA-------------------------------\n\n")
    ci.addCity()
    chatBotHelp()

def rimuovi_citta():
    print("\n-------------------------------RIMOZIONE CITTA-------------------------------\n\n")
    ci.removeCity()
    chatBotHelp()

def probabilita_vendita():
    print("\n-------------------------------PROBABILITA' VENDITA-------------------------------\n\n")
    p.questionsForPrediction()
    chatBotHelp()

def domanda():
    print("\n-------------------------------DOMANDA IMMOBILE-------------------------------\n\n")
    cs.classifier()
    chatBotHelp()

def valutazione_di_sistema():
    print("\n-------------------------------VALUTAZIONE DI SISTEMA-------------------------------\n\n")
    cs.valutazione()
    chatBotHelp()

def esci():
    print("\nGrazie per aver utilizzato il nostro servizio. Arrivederci!")

def chatBotHelp():
    print("\nBisogno di aiuto? Per visualizzare la lista dei comandi digita: -1 ")

def default():
    print("\nValore non valido. Inserire un numero corretto.")

#messaggio di benvenuto  
def firstMessage():
    print("Benvenuto nel portale Real Estate Manager.\n"
          "Grazie al nostro aiuto potrai consultare numerose informazioni riguardanti la vendita delle case.")
    
#menu per visualizzare i comandi disponibili
def mainMenu():
    table = [["COMANDO","DESCRIZIONE COMANDO"],
            ["",""],
            ["    ","CASE"],
            ["1","Mostra la lista di tutte le case (in vendita e non)"],
            ["2","Mostra la lista di tutte le case in vendita"],
            ["3","Mostra la lista di tutte le case non in vendita"],
            ["4","Mostra le informazioni della casa selezionata"],
            ["5","Aggiunge una nuova casa"],
            ["6","Modifica una casa esistente"],
            ["",""],
            ["    ","ZONE"],
            ["7","Mostra la lista delle zone"],
            ["8","Aggiunge una nuova zona"],
            ["",""],
            ["    ","CITTA'"],
            ["9","Mostra la lista delle citta'"],
            ["10","Aggiunge una nuova citta"],
            ["11","Rimuove una citta"],
            ["",""],
            ["    ","FUNZIONALITA'"],
            ["12","Mostra la probabilita' di vendita"],
            ["13","Mostra il prezzo spettante della casa"],
            ["14","Mostra la valutazione del sistema"],
            ["0","Terminare l'esecuzione del programma"]]
    
    print(tabulate(table, tablefmt="pretty", numalign="center"))
    
    print("\nDigita il numero del comando a cui sei interessato.              \n")
    

#restituisce risultati query    
def outputResult(myTrueQuery, printable):
    
    myList = list(prolog.query(myTrueQuery))
    
    if not myList:
        if printable:
            print("Nessun risultato trovato.\n") 
        return False
    
    else:
        if printable:
            print(tabulate(myList, headers='keys', tablefmt="pretty", numalign="center"))
        return True