from pyswip import Prolog
import zona as z
import funzionalita as f

prolog = Prolog()
prolog.consult("RealEstate.pl") 

#mostra la lista completa delle citta'
def cityList():
    
    myTrueQuery= "citta(NOME,PAESE,REGIONE)"
    f.outputResult(myTrueQuery, True)

#aggiunge una citta'
def addCity():
     
    city = ""
    
    #messaggio errore nel caso sono presenti dei numeri nella citta' inserita
    while(city == ""):
       
        city = input("Inserisci il nome di una citta':\n").lower()
        queryCheck = "citta("+str(city)+",PAESE,REGIONE)"
            
        if(any(chr.isdigit() for chr in str(city))): 
            city=""
            print("Valore inserito non valido. Inserire solo lettere!\n")
    
   
    #controllo presenza citta' nel database
    if(not f.outputResult(queryCheck, False)):
        
        country = input("Inserisci il paese in cui si trova la citta': ").lower()

        
        region = input("Inserisci la regione in cui si trova la citta: ").lower()
        
        
        queryCheck = "citta("+str(city)+","+str(country)+","+str(region)+")"

        prolog.assertz(queryCheck)
        
        print("Citta' inserita nel database.")
        
    else:
        print("Citta' gia' presente nel database.\n")
        
#rimuove una citta' esistente
def removeCity():
    
    city = input("Inserisci la citta' da eliminare:\n").lower()
    queryCheck = "citta("+str(city)+",PAESE,REGIONE)"
    
    #controllo presenza citta' nel database
    if(f.outputResult(queryCheck, False)):
        prolog.retractall(queryCheck)
        print("La citta' e' stata eliminata correttamente.\n")
        
        z.removeZone(city)
    else:
        print("Citta' non presente nel database.\n")
        