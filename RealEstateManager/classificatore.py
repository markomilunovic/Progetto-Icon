from sklearn.model_selection import train_test_split
from pandas import read_csv
from sklearn import svm
from sklearn.metrics import classification_report


casa_df = read_csv('domanda.csv')
X = casa_df.drop(columns=['domanda'])

y = casa_df['domanda']
# Divisione dei dataset in training set e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=0)
modello = svm.SVC(kernel='linear', C=1, random_state=0)
modello.fit(X_train.values, y_train.values)

def classifier():
    metriQuadri = 0
    locali = 0
    piano = 0
    #result = True
    while (metriQuadri < 20 or metriQuadri > 400):
        
        intInserted = False
        while(not intInserted):
            metriQuadri = input("Inserisci la superfice della casa in metri quadri: \n")
        
            intInserted = controlInput(metriQuadri)
        metriQuadri=int(metriQuadri)
        if(metriQuadri < 20 or metriQuadri > 400):
            print("Superficie inserita non valida. Inserire un valore compreso tra 20 e 400")
            
    while (locali < 1 or locali > 10):
        
        intInserted = False
        while(not intInserted):
            
            locali = input("Inserisci il numero di locali della casa: ")
        
            intInserted = controlInput(locali)
        locali=int(locali)
        
        if(locali < 1 or locali > 10):
            print("Numero locali inserito non valido. Inserire un valore tra 1 e 10")
            
    while (piano < 1 or piano >10 ):
        
        intInserted = False
        while(not intInserted):
            
            piano = input("Inserisci il piano della casa: ")
            
            intInserted = controlInput(piano)
        piano=int(piano)
        
        if(piano < 0 or piano > 10):
            print("Numero piano inserito non valido. Inserire un valore tra 1 e 10")
        
    domanda = modello.predict([[metriQuadri, locali, piano]])
    for elem in domanda:
        print("La domanda per questa casa e': " + str(elem) + "\n")
        

def valutazione():
    y_predict=modello.predict(X_test)
    print(classification_report(y_test, y_predict))   
    
    
def controlInput(user_input):

    try:
        int(user_input)
        it_is = True
        
    except ValueError:
        it_is = False
        print("Inserire solo valori numerici.\n")
        
    return it_is



