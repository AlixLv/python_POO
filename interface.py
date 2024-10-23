# déclaration de la simili-interface compteInterface:
operations = [100, 2000, 5000, -100, -1000, 0, -300]
 

class Icompte:
    def deposer(self, montant):
        pass
    def retirer(self, montant):
        pass
    def getBalance(self):
        pass


# déclaration de la class parent compteEnLigne:

class compteEnLigne(Icompte):
     # déclaration du constructeur avec __init__
    def __init__(self, soldeCompte):
        # vérifier que soldeCompte est bien de type int ou float
        if isinstance(soldeCompte, (int, float)):
            self.soldeCompte = float(soldeCompte) 
        else:
        #    si soldeCompte != d'un int ou float, alors on stoppe le programme
           raise TypeError("⛔️ "f'Le solde initial doit être un nombre! Type de solde proposé: {type(soldeCompte)}')
        # gestion des exceptions pour bien avoir un float en valeur
        try:
            self.soldeCompte = float(soldeCompte)
        except ValueError:
            raise ValueError("⛔️ Le solde initial doit être un nombre valide")     

    def deposer(self, montant):
        """fonction pour modifier variable soldeCompte
        Args:
            montant (_int_ / _float_): montant à additioner à  variable soldeCompte
        """
        self.soldeCompte += montant
        print("🔄 " f'Vous avez ajouté {montant} € à votre compte. Montant actualisé: {self.soldeCompte}')

    def retirer(self, montant):
        self.soldeCompte -= montant
        print("🔄 " f'Vous avez retiré {montant} € à votre compte. Montant actualisé: {self.soldeCompte}')
        return self.soldeCompte
    
    def getBalance(self):
             print("➡️" f'Le solde actuel du compte est de: {self.soldeCompte}')

    def listeOperations(self, liste):
        for operation in liste:
            if "-" in range(operation):
                self.retirer(operation)
                # print("🔃 " f'solde en cours d\'évolution: {self.soldeCompte}')
            else:
                 self.deposer(operation)
                #  print("🔃 " f'solde en cours d\'évolution: {self.soldeCompte}')
        return self.soldeCompte


class epargne(Icompte):
    # déclaration du constructeur avec __init__
    def __init__(self, soldeEpargne):
         # vérifier que soldeCompte est bien de type int ou float
        if isinstance(soldeEpargne, (int, float)):
            self.soldeEpargne = float(soldeEpargne) 
        else:
        #    si soldeCompte != d'un int ou float, alors on stoppe le programme
           raise TypeError("⛔️ "f'Le solde initial doit être un nombre! Type de solde proposé: {type(soldeEpargne)}')
        

    def verifierDepot(self, montant):
        if montant > 200:
            self.soldeEpargne += montant
            print("✅ " f'Vous avez ajouté {montant} € à votre épargne. Montant actualisé: {self.soldeEpargne}')
        else:
            print("❌" f'Votre dépôt doit être supérieur à 200€ ! Dépôt actuel : {montant}')
        return self.soldeEpargne    

    def autoriserRetrait(self, montant):
        if self.soldeEpargne < 1000:
            print("🚫 " f'Retrait autorisé à partir de 1000€ d\'épargne disponible. Montant épargné actuel: {self.soldeEpargne}') 
        else:
            self.soldeEpargne -= montant
            print("✅ " f'Retrait effectué: {montant}. Epargne actualisée: {self.soldeEpargne}')
            return self.soldeEpargne           

#  instanciation de la class compteEnLigne:

monCompte = compteEnLigne(100)
print(monCompte)
print()
print(monCompte.soldeCompte)
print()
print(monCompte.deposer.__doc__)
print()
monCompte.listeOperations(operations)
print()
monCompte.retirer(100)


# instanciation de la class epargne:

monEpargne = epargne(100)
print(monEpargne.soldeEpargne)
monEpargne.verifierDepot(100)
print()
monEpargne.verifierDepot(230)
print()
monEpargne.autoriserRetrait(10)
print()
monEpargne.verifierDepot(800)
print()
monEpargne.autoriserRetrait(10)
print()
       