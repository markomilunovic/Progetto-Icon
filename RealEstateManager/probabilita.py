from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController

# Costruizione Rete Bayesiana

#stato della casa
statoCasa = BbnNode(Variable(0, 'stato', ['nuova costruzione', 'in buono stato', 'da ristrutturare']), [0.70, 0.25, 0.05])

#casa arredata
arredamento = BbnNode(Variable(1, 'arredato', ['si', 'no']), [0.85, 0.15])

#condizione della casa da vendere (0-1)
condizione = BbnNode(Variable(2, 'condizione casa', ['ottima', 'scarsa']),
                          [0.98, 0.02, 0.75, 0.25, 0.6, 0.4, 0.51, 0.49, 0.15, 0.85, 0.05, 0.95])

#in prossimita' dei servizi pubblici
prossimita= BbnNode(Variable(3, 'prossimita', ['si', 'no']), [0.85, 0.15])

#posizione della casa
locazione = BbnNode(Variable(4, 'locazione', ['centro', 'periferia']), [0.71, 0.29])

#nodo di facilita' spostamento a piedi(3-4)
facilitaSpostamento = BbnNode(Variable(5, 'spostamento', ['ottimo', 'scarso']), [0.99, 0.01, 0.72, 0.28,
                                                                         0.32, 0.68, 0.02, 0.98])

#nodo di qualita' della casa (2-5)
qualitaCasa = BbnNode(Variable(6, 'qualita', ['ottimo', 'scarso']), [0.93, 0.07, 0.83, 0.17,
                                                                        0.52, 0.48, 0.12, 0.88])

#presenza balcone in casa
presenzaBalcone = BbnNode(Variable(7, 'balcone', ['si', 'no']), [0.95, 0.05])

#posto per lasciare la macchina
postoAuto = BbnNode(Variable(8, 'garage', ['si', 'no']), [0.85, 0.15])

#nodo per le caratteristiche dello immobile(7-8)
caratteristiche = BbnNode(Variable(10, 'caratteristiche', ['ottimo', 'scarso']), [0.92, 0.08, 0.77, 0.23,
                                                                0.39, 0.61, 0.16, 0.84])

#previsione finale della % di poter vendere la casa sopra un certo prezzo (6-10)
previsionePrezzo = BbnNode(Variable(11, 'previsione vendita', ['si', 'no']), [0.95, 0.05, 0.68, 0.32, 
                                                                                             0.51, 0.49, 0.06, 0.94])

bbn = Bbn() \
    .add_node(statoCasa) \
    .add_node(arredamento) \
    .add_node(condizione) \
    .add_node(prossimita) \
    .add_node(locazione) \
    .add_node(facilitaSpostamento) \
    .add_node(qualitaCasa) \
    .add_node(presenzaBalcone) \
    .add_node(postoAuto) \
    .add_edge(Edge(statoCasa, condizione, EdgeType.DIRECTED)) \
    .add_edge(Edge(arredamento, condizione, EdgeType.DIRECTED)) \
    .add_edge(Edge(prossimita, facilitaSpostamento, EdgeType.DIRECTED)) \
    .add_edge(Edge(locazione, facilitaSpostamento, EdgeType.DIRECTED)) \
    .add_edge(Edge(condizione, qualitaCasa, EdgeType.DIRECTED)) \
    .add_edge(Edge(facilitaSpostamento, qualitaCasa, EdgeType.DIRECTED)) \
    .add_edge(Edge(presenzaBalcone, caratteristiche, EdgeType.DIRECTED)) \
    .add_edge(Edge(postoAuto, caratteristiche, EdgeType.DIRECTED)) \
    .add_edge(Edge(caratteristiche, previsionePrezzo, EdgeType.DIRECTED)) \
    .add_edge(Edge(qualitaCasa, previsionePrezzo, EdgeType.DIRECTED))

# Conversione da bbn ad albero
join_tree = InferenceController.apply(bbn)

#Setta il valore scelto in base alla risposta data
def insertDefinedValue(tree, nodeName, optionName, value):
    ev = EvidenceBuilder() \
        .with_node(tree.get_bbn_node_by_name(nodeName)) \
        .with_evidence(optionName, value) \
        .build()
    tree.set_observation(ev)

#domande da porre all'utente
def questionsForPrediction():
    tree = join_tree.__copy__()

    while True:
        value = input(
            "Indicare lo stato della casa:\n"
            "Risposte possibili: (nuova costruzione) (in buono stato) (da ristrutturare) (non so)\n").lower()
        if value in ["nuova costruzione", "in buono stato", "da ristrutturare"]:
            insertDefinedValue(tree, "stato", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(0)

    while True:
        value = input(
            "Indicare se la casa e' arredata:\n"
            "Risposte possibili: (si) (no) (non so)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "arredato", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(1)

    while True:
        value = input("Indicare se la casa si trova in prossimita' dei servizzi pubblici:\n"
                      "Risposte possibili: (si) (no) (non so)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "prossimita", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(2)

    while True:
        value = input("Dove si trova la casa?:\n"
                      "Risposte possibili: (centro) (periferia) (non so)\n").lower()
        if value in ["centro", "periferia"]:
            insertDefinedValue(tree, "locazione", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(3)
            
    while True:
        value = input("Indicare se la casa ha un balcone:?\n"
                      "Risposte possibili: (si) (no) (non so)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "balcone", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(4)

    while True:
        value = input("Indicare se la casa dispone di una garage?\n"
                      "Risposte possibili: (si) (no) (non so)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "garage", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(5)
            
    print("Stiamo analizzando le tue risposte...")
    outputPrediction(tree)



#stampa la probabilita' di vendita in base alla probabilita' ottenuta
def outputPrediction(tree):
    for node, posteriors in tree.get_posteriors().items():
        if node == 'previsione vendita':
            max, min = posteriors.items()
            print(f'[{node} : {max[1]*100:.0f}%]')
            if max[1] < 0.3:
                print("Probabilita' di vendita sopra 50 000 euro: bassa.\n")
            elif max[1] < 0.45:
                print("Probabilita' di vendita sopra 100 000 euro: medio-bassa.\n")
            elif max[1] < 0.6:
                print("Probabilita' di vendita sopra 200 000 euro: media.\n")
            elif max[1] < 0.8:
                print("Probabilita' di vendita sopra 300 000 euro: medio_alta\n")
            else:
                print("Probabilita' di vendita sopra 400 000 euro: alta\n")


def infoMessage(number):
    if number == 0:
        print("Devi inserire lo stato della casa, se non sei sicuro scegli uno stato approssimativo.\n")
    elif number == 1:
        print("Devi indicare se la casa e' arredata o meno.\n")
    elif number == 2:
        print("Devi indicare se la casa si trova in prossimita' dei servizi pubblici\n"
              "(es. supermercati, ospedali, campus univeristari).\n")
    elif number == 3:
        print("Devi indicare se la casa si trova in centro della citta' oppure in periferia.\n")
    elif number == 4:
        print("Devi indicare se la casa possiede un balcone o meno.\n")
    elif number == 5:
        print("Devi indicare se la casa possiede un posto per lasciare la macchina(es. garage).\n")
