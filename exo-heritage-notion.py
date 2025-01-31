# déclaration de l'interface Vaisseaux
# définit les inputs et outputs:
class Vaisseaux_interface:
	def __init__(self, nom, type, taille):
		self.nom = str(nom)
		self.type = str(type)
		self.taille = float(taille)
		
		
	def __retournerParametres(self):
		pass


# déclaration class parent qui hérite de l'interface Vaisseaux
# définit les inputs et outputs et leurs implémentations !
# super() = fonction utilisée dans les class enfants ou dans les class héritant d'interface 
#  super() permet d'appeler les méthodes de la class parent/interface et d'étendre les fonctionnalités des méthodes héritées
class Vaisseaux(Vaisseaux_interface):
	def __init__(self, nom, type, taille):
		super().__init__(nom, type, taille)
		print(f'Le nom du vaisseau est : {nom}')
		print(f'Le vaisseau {nom} est de type {type}')
		print(f'La taille du vaisseau {nom} est : {taille}')
		
				
	def __retournerParametres(self):
		print("🔍 nom: ", self.nom, "type: ", self.type, "taille: ", self.taille)
		return self.nom, self.type, self.taille

	def parametresVaisseau(vaisseau):
		if isinstance(vaisseau, Vaisseaux):
			print(vaisseau.__retournerParametres())
		else:
			print("Ce n'est pas une instance de la classe Vaisseaux!")	


# déclaration de la class Croiseurs, qui hérite de la class Vaisseaux
class Croiseur(Vaisseaux):
	def __init__(self, nom, type, taille, capacite, maxCapacite):
		super().__init__(nom, type, taille)
		self.capacite = int(capacite)
		self.maxCapacite = int(maxCapacite)
		print(f'Le nombre d\'hommes sur le vaisseau est de {capacite}')
		print(f'Le nombre maximum d\'hommes sur le vaisseau est de {maxCapacite}')	

	def chargerTroupes(self, capacite, charge):
		if self.capacite + charge >= self.maxCapacite:
			print("Charge maximale dépassée") 
			self.capacite = 700
			print(f'la charge actuelle est de {self.capacite}')	
		else:	
			self.capacite = capacite + charge			
			print(f'Nouvelle charge de troupe après charge: {self.capacite}')
		return 	self.capacite

	def dechargerTroupes(self, capacite, decharge):
		self.capacite = capacite - decharge
		print(f'Nouvelle charge de troupe après décharge: {self.capacite}')
		return self.capacite
	

# déclaration de la class Intercepteurs, qui hérite de Vaisseaux
class Intercepteur(Vaisseaux):
	def __init__(self, nom, type, taille, canon, maxCanon):
		super().__init__(nom, type, taille)
		self.canon = int(canon)
		self.maxCanon = int(maxCanon)
		print(f'{nom} peut tirer {maxCanon} canons maximums et possède actuellement {canon} canons')

	def tirer(self, tirs):
		for tir in range(tirs):
			if self.canon == 0:	
				print("⛔️ Vous devez recharger avant de pouvoir tirer de nouveau!")	
			else:
				print("Tire!")
				self.canon -= 1
				print("nombre de canon restant: ", self.canon)
		if self.canon == 0:		
			print("⚠️ Rechargez avant de pouvoir tirer de nouveau!")		

	def recharger(self):
		print("Recharge")
		if self.canon == self.maxCanon:
			print("💣 Vous avez rechargé au maximum vos canons.")
		else:	
			self.canon += 1
			print("💣 "f'Canons disponibles: {self.canon}')	 	


# --------------------------------- UTILISATIONS DES CLASSES -----------------------------------------------------------------

# Intanciations de classe Croiseur()
acclamator = Croiseur("Acclamator", "croiseur", 752, 500, 700)
print(acclamator)
print()

corvette = Croiseur("Corvette", "croiseur", 150, 16, 165)
print(corvette)
print("🍎")
corvette.parametresVaisseau()

# appel des méthodes sur les deux instanciations de class Croiseur()
print(acclamator)
print("🚁")
acclamator.chargerTroupes(acclamator.capacite, 50)
print("🚢")
acclamator.dechargerTroupes(acclamator.capacite, 20)
print()
acclamator.chargerTroupes(acclamator.capacite, 100)
print()
acclamator.chargerTroupes(acclamator.capacite, 100)
print("🚢")
acclamator.dechargerTroupes(acclamator.capacite, 50)
print("🍎")
acclamator.parametresVaisseau()


# Intanciations de classe Intercepteur() et appels de méthodes
# Xwing = Intercepteur("X-wing", "intercepteur", 12.5, 2, 2)
# print(Xwing)
# print()
# Xwing.tirer(2)
# print()
# Xwing.recharger()
# Xwing.recharger()
# Xwing.recharger()



# Ywing = Intercepteur("Y-wing", "intercepteur", 23, 2, 2)
# print(Ywing)
# print()

# print("Fonction affichage des paramètres d'un vaisseau")
# parametresVaisseau(Xwing)
# print()
# Ywing.tirer(3)
# print()
# Ywing.recharger()
# Ywing.recharger()
# print(f'Canons à présents disponibles: {Ywing.canon}')
# print()
# Ywing.tirer(2)
# print()

