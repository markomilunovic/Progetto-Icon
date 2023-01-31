
from pyswip import Prolog
import casa as c
import funzionalita as f

prolog = Prolog()
prolog.consult("RealEstate.pl") 

#mostra la lista completa delle zone 
def zoneList():
    
    myTrueQuery= "zona(ID,CITTA,DISPONIBILITA)"
    f.outputResult(myTrueQuery, True)
    
#inserisce una zona    
def addZone():
    
    zoneID = ""
    
    #controllo numero caratteri della zona inserita
    while(not 1 <= len(str(zoneID)) <= 3):
       
        zoneID = input("Inserisci codice zona:\n").lower()
            
        queryCheck = "zona("+str(zoneID)+",CITTA,DISPONIBILITA)"
       
        #messaggio errore nel caso la lunghezza dell'ID non dovesse rientrare nel range (1-3)   
        if(not 1 <= len(str(zoneID)) <= 3):
            print("Valore inserito non valido. Max 3 caratteri!\n")
         
        #messaggio errore nel caso sono presenti dei numeri nell'ID inserito   
        if(any(chr.isdigit() for chr in str(zoneID))): 
            zoneID=""
            print("Valore inserito non valido. Inserire solo lettere!\n")
            
    #controllo presenza id nel database
    if(not f.outputResult(queryCheck, False)):
        cityFound = False
            #controllo presenza citta nel database
        while(not cityFound):
                
            city = input("Inserisci il nome della citta': ").lower()
            checkCity = "citta("+str(city)+",PAESE,REGIONE)"
            cityFound = f.outputResult(checkCity, False)
                
            if (not cityFound):
                    
                print("Valore inserito non valido, inserire una citta' presente nel database.\n") 
         
         
        #controllo inserimento disponibilità
        availability = 0
       
        queryCheck = "zona("+str(zoneID)+","+city+","+str(availability)+")"
        prolog.assertz(queryCheck)
        
        print("Zona inserita nel database.")
        
    else:
        print("Zona gia' presente nel database.\n")
        
#rimuove una zona in seguito alla rimozione di una citta
def removeZone(city):
    zoneID=""
    queryCheck = "zona(ID,"+str(city)+",DISPONIBILITA)"
    
    #controllo presenza zona nella citta nel database
    if(f.outputResult(queryCheck, False)):
        
        zone=list(prolog.query("zona(ID,"+str(city)+",_)"))
        print(zone)
        print('\n')
        ''''''
       
        f.outputResult(queryCheck, True)
        
        for elem in zone:
            zoneID = str(zone[0]).split("'")
            print(zoneID)
            print('\n')
            ''''''
            c.removeHouseForZone(zoneID[3])
            prolog.retractall(queryCheck)

def modifyAvailability(ID,operation):
    
    queryCheck = "zona("+str(ID)+",CITTA,DISPONIBILITA)"
    zone=list(prolog.query(queryCheck))
    print(zone)
    print('\n')
    ''''''
    #salvataggio occorrenze di CITTA' e DISPONIBILITA'
    for elem in zone:
        infoZone = extractZone(zone, operation)
        print(infoZone)
        print('\n')
        ''''''
        prolog.retractall(queryCheck)
        prolog.assertz("zona("+str(ID)+","+str(infoZone[0])+","+str(infoZone[1])+")")
            
    
def extractZone(list, operation):
        listInfo=[]
        zoneID = str(list[0]).split("'")
        print(zoneID)
        print('\n')
        '''a'''
        listInfo.append(zoneID[3])
        print(listInfo)
        print('\n')
        ''''''
        
        if(operation == 0):
            listInfo.append(int(zoneID[6][zoneID[6].find(' ')+1:zoneID[6].find('}')]) + 1)
            print(listInfo)
            print('\n')
            ''''''
            return listInfo

        elif(operation == 1):
            listInfo.append(int(zoneID[6][zoneID[6].find(' ')+1:zoneID[6].find('}')]) - 1)
            print(listInfo)
            print('\n')
            ''''''
            return listInfo
        
        else:
            return zoneID[7]
        