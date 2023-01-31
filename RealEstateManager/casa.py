from pyswip import Prolog
import zona as z
import funzionalita as f

prolog = Prolog()
prolog.consult("RealEstate.pl") 

#mostra la lista completa delle case
def houseList():
    
    myTrueQuery= "casa(ID,VENDITA,ZONA)"
    f.outputResult(myTrueQuery, True)

#mostra la lista delle case in vendita
def forSaleList():
    
    myTrueQuery= "casa(ID,si,ZONA)"
    f.outputResult(myTrueQuery, True)
    
#mostra la lista delle case non in vendita
def notForSaleList():
    
    myTrueQuery= "casa(ID,no,ZONA)"
    f.outputResult(myTrueQuery, True)
    
#dato l'ID, cerca una casa
def findHouse():
    
    houseID = ""

    #controllo numero caratteri dell'ID inserito
    while(houseID == "" ):
       
        houseID = input("Inserisci ID della casa che vuoi cercare:\n")
        
        if((not len(str(houseID)) == 5 ) or (not houseID.isdigit())):
            print("Valore inserito non valido. Max 5 caratteri e solo valori numerici!")
            houseID = ""    
            
    myTrueQuery= "casa("+str(houseID)+",VENDITA,ZONA)"
    f.outputResult(myTrueQuery, True)
    
#inserisce una casa
def addHouse():
    
    houseID = ""

    #controllo numero caratteri dell' inserito
    while(houseID == "" ):
       
        houseID = input("Inserisci ID nuova casa:\n")
        queryCheck = "casa("+str(houseID)+",VENDITA,ZONA)"
        
        if((not len(str(houseID)) == 5 ) or (not houseID.isdigit())):
            print("Valore inserito non valido. Max 5 caratteri e solo valori numerici!")
            houseID = ""    
  
    #controllo presenza id nel database
    if(not f.outputResult(queryCheck, False)):

        houseOnSale = ""
        
        #controllo inserimento 'si' o 'no'
        while(houseOnSale != 'si' and houseOnSale != 'no'):
            
            houseOnSale = input("Inserisci se e' in vendita o meno(si/no): ").lower()
            
            if(houseOnSale != 'si' and houseOnSale != 'no'):
                
                print("Valore inserito non valido, inserire \"si\" o \"no\".\n")
                
    
        #inserimento della zona solo in caso di vendita
        if(houseOnSale == 'si'): 
            
            #controllo presenza zona nel database
            zoneFound = False
            
            while(not zoneFound):
                
                houseZone = input("Inserisci l'ID della zona: ")
                checkZone = "zona("+str(houseZone)+",EDIFICIO,DISPONIBILITA)"
                zoneFound = f.outputResult(checkZone, False)
                
                if (not zoneFound):
                    print("Valore inserito non valido, inserire una zona presente nel database.\n") 
                else:
                        z.modifyAvailability(str(houseZone), 0)
                        queryCheck = "casa("+str(houseID)+","+houseOnSale+","+str(houseZone)+")"
                                     
        else:
            
            queryCheck = "casa("+str(houseID)+","+houseOnSale+", null)"
            
        prolog.assertz(queryCheck)
        
        print("Casa inserita nel database.")
        
    else:
        print("Casa gia' presente nel database.\n")
       
    
#modifica una casa esistente
def modifyHouse():
    
    houseID = input("Inserisci ID della casa da modificare:\n")
    queryCheck = "casa("+str(houseID)+",VENDITA,ZONA)"
    
    #controllo presenza id nel database
    if(f.outputResult(queryCheck, False)):
        
        lista=list(prolog.query(queryCheck))
        print(lista) 
        print('\n')
        ''' a'''
        oldZone = z.extractZone(lista, 2)
           
        prolog.retractall(queryCheck)
        
        houseOnSale = ""
        
        #controllo inserimento 'si' o 'no'
        while(houseOnSale != 'si' and houseOnSale != 'no'):
            
            houseOnSale = input("Inserisci se e' in vendita o meno(si/no): ").lower()
            
            if(houseOnSale != 'si' and houseOnSale != 'no'):
                
                print("Valore inserito non valido, inserire \"si\" o \"no\".\n")
                
        #inserimento della zona solo in caso di vendita
        if(houseOnSale == 'si'): 
            zoneFound = False
            #controllo presenza zona nel database
            while(not zoneFound):
                
                houseZone = input("Inserisci l'ID della zona: ")
                checkZone = "zona("+str(houseZone)+",EDIFICIO,DISPONIBILITA)"
                zoneFound = f.outputResult(checkZone, False)
                
                if (not zoneFound):
                    
                    print("Valore inserito non valido, inserire una zona presente nel database.\n") 
                else:
                    #aumento della disponibilità nuova zona
                    z.modifyAvailability(str(houseZone),0)
                    queryCheck = "casa("+str(houseID)+","+houseOnSale+","+str(houseZone)+")"
     
            
        else:
            
            queryCheck = "casa("+str(houseID)+","+houseOnSale+", null)"
         
        #diminuzione disponibilità vecchia zona
        z.modifyAvailability(str(oldZone), 1)       
        prolog.assertz(queryCheck)
        
        print("Casa modificata correttamente.")
        
    else:
        print("Casa non presente nel database.\n")
        
#rimuove una casa in seguito alla rimozione di una zona
def removeHouseForZone(zoneID):
    
    #controllo presenza casa in specifica zona
    queryCheck = "casa(ID,IDONEO,"+str(zoneID)+")"
    house=list(prolog.query(queryCheck))
    print(house)
    print('\n')
    ''''''
    
    for elem in house:
        
        if(f.outputResult(queryCheck, False)):
            prolog.retractall(queryCheck)
  
