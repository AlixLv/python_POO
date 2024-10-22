# déclaration de l'interface Vaisseaux
# définit les inputs et outputs:
class Vaisseaux_interface:
	def __init__(self, nom, type, taille):
		self.nom = nom ; str
		self.type = type; str
		self.taille = taille ; float
		
		
	def retournerParametres(self):
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
		
				
	def retournerParametres(self):
		print("🔍 nom: ", self.nom, "type: ", self.type, "taille: ", self.taille)
		return self.nom, self.type, self.taille


# déclaration de la class Croiseurs, qui hérite de la class Vaisseaux
class Croiseur(Vaisseaux):
	def __init__(self, nom, type, taille, hommes):
		super().__init__(nom, type, taille)
		self.hommes = hommes; int
		print(f'Le nombre d\'hommes sur le vaisseau est de {hommes}')	

	def chargerTroupes(self, hommes, charge):
		if self.hommes + charge >= 700:
			print("Charge maximale dépassée") 
			self.hommes = 700
			print(f'la charge actuelle est de {self.hommes}')	
		else:	
			self.hommes = hommes + charge			
			print(f'Nouvelle charge de troupe après charge: {self.hommes}')
		return 	self.hommes

	def dechargerTroupes(self, hommes, decharge):
		self.hommes = hommes - decharge
		print(f'Nouvelle charge de troupe après décharge: {self.hommes}')
		return self.hommes
	

# déclaration de la class Intercepteurs, qui hérite de Vaisseaux
class Intercepteur(Vaisseaux):
	def __init__(self, nom, type, taille, canon):
		super().__init__(nom, type, taille)
		self.canon = canon; int
		print(f'{nom} tire {canon} canons')

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
		self.canon += 1
		print(f'Canons disponibles: {self.canon}')	 	


# Fonction affichant les paramètres par type de vaisseau:
def parametresVaisseau(vaisseau):
	if isinstance(vaisseau, Vaisseaux):
		print(vaisseau.retournerParametres())
	else:
		print("Ce n'est pas une instance de la classe Vaisseaux!")	

# --------------------------------- UTILISATIONS DES CLASSES -----------------------------------------------------------------

# Intanciations de classe Croiseur()
acclamator = Croiseur("Acclamator", "croiseur", 752, 600)
print(acclamator)
print()

corvette = Croiseur("Corvette", "croiseur", 150, 165)
print(corvette)
print()

# appel des méthodes sur les deux instanciations de class Croiseur()
print(acclamator)
print()
acclamator.retournerParametres()
print("🚁")
acclamator.chargerTroupes(acclamator.hommes, 50)
print("🚢")
acclamator.dechargerTroupes(acclamator.hommes, 20)


# Intanciations de classe Intercepteur() et appels de méthodes
Xwing = Intercepteur("X-wing", "intercepteur", 12.5, 2)
print(Xwing)
print()
print(Xwing.retournerParametres())
print()

Ywing = Intercepteur("Y-wing", "intercepteur", 23, 3)
print(Ywing)
print()
print(Ywing.retournerParametres())
print()

print("Fonction affichage des paramètres d'un vaisseau")
parametresVaisseau(Xwing)
print()
Ywing.tirer(3)
print()
Ywing.recharger()
Ywing.recharger()
print(f'Canons à présents disponibles: {Ywing.canon}')
print()
Ywing.tirer(2)
print()

