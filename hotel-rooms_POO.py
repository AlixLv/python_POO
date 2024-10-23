# collection de linge:  peignoirs, serviettes de bain, draps
collectionLinge = { 'peignoir': 1,
                        'servietteDeBain': 1,
                        'drap': 1
                        }

class Chambre():
    # constructeur avec propriétés privées: 
    def __init__(self, linge):
        self.__nombreDePersonnes = 0
        self.__linge = linge

    def getNombreDePersonne(self):
        return self.__nombreDePersonnes
    
    def setNombreDePersonne(self, capacite):
        self.__nombreDePersonnes = capacite

    def ajoutPersonne(self, pers):
        self.__nombreDePersonnes += pers

    def getLinge(self):
        return self.__linge

    def setLinge(self):
        newDico = {}
        for element, exemplaire in self.__linge.items():
            exemplaire = exemplaire * self.__nombreDePersonnes
            print(exemplaire)
            # créer un nouveau dico
            newDico.update({element : exemplaire})
            # puis attribuer nouveau dico à self.__linge 
            self.__linge = newDico  

    def getProprietes(self):
        print("👥 "f'{self.__nombreDePersonnes} logent dans la chambre')
        print("Le linge se compose de:")
        for element, exemplaire in self.__linge.items():
            print("🛀 "f'{element}, {exemplaire} exemplaires')

chambreUne = Chambre(collectionLinge)
chambreUne.setNombreDePersonne(3)
chambreUne.setLinge()
chambreUne.getProprietes()
             






# class ChambrePrete(Chambre):