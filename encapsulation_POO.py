class Voiture :
    def __init__(self, im):
        self.__Compteur = 0
        self.__Immat = im
	
    def ChangerPneu(self):
        # retourne True si compteur >= 10000 et False si compteur < 10000
        return (self.__Compteur >= 10000) 
	
    def getCompteur(self) :
        # méthode n'affichera jamais la valeur de compteur !
        return self.__Compteur
	
    def setCompteur(self, km):
        self.__Compteur = km
            
    def getImmat(self):
      # méthode n'affichera jamais la valeur de immat !
        return self.__Immat
        
    def setImmat(self,im):
        self.__Immat = im

    def Choix_Rouler(self):
        d = int(input("Distance: "))
        if not self.ChangerPneu():
            self.setCompteur( self.getCompteur() + d ) 
        else:
            print("Vos pneus sont uses !") 

    def Choix_Afficher(self):
        print("La voiture : ")
        print("Immatriculation: ", self.getImmat()) 
        print("Kilometrage: ", self.getCompteur())     



maVoiture = Voiture("KZ 360 RR")
print()
maVoiture.ChangerPneu()
maVoiture.setCompteur(100)
maVoiture.setImmat("KZ 366 RR")
maVoiture.Choix_Rouler()
print()
maVoiture.Choix_Afficher()
print()
maVoiture.Choix_Rouler()
print()
maVoiture.Choix_Afficher()

