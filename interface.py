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
            self.__soldeCompte = float(soldeCompte) 
        else:
        #    si soldeCompte != d'un int ou float, alors on stoppe le programme
           raise TypeError("⛔️ "f'Le solde initial doit être un nombre! Type de solde proposé: {type(soldeCompte)}')
        # gestion des exceptions pour bien avoir un float en valeur
        try:
            self.__soldeCompte = float(soldeCompte)
        except ValueError:
            raise ValueError("⛔️ Le solde initial doit être un nombre valide")     

    def getSoldeCompte(self):
        print(f'Le montant actuel de votre compte est de: {self.__soldeCompte}')

    def deposer(self, montant):
        """fonction pour modifier variable soldeCompte
        Args:
            montant (_int_ / _float_): montant à additioner à  variable soldeCompte
        """
        self.__soldeCompte += montant
        print("🔄 " f'Vous avez ajouté {montant} € à votre compte. Montant actualisé: {self.__soldeCompte}')

    def retirer(self, montant):
        self.__soldeCompte -= montant
        print("🔄 " f'Vous avez retiré {montant} € à votre compte. Montant actualisé: {self.__soldeCompte}')
        return self.__soldeCompte
    
    def getBalance(self):
             print("➡️" f'Le solde actuel du compte est de: {self.__soldeCompte}')

    def listeOperations(self, liste):
        for operation in liste:
            if "-" in range(operation):
                self.retirer(operation)
                # print("🔃 " f'solde en cours d\'évolution: {self.soldeCompte}')
            else:
                 self.deposer(operation)
                #  print("🔃 " f'solde en cours d\'évolution: {self.soldeCompte}')
        return self.__soldeCompte


class epargne(Icompte):
    # déclaration du constructeur avec __init__
    def __init__(self, soldeEpargne):
         # vérifier que soldeCompte est bien de type int ou float
        if isinstance(soldeEpargne, (int, float)):
            self.__soldeEpargne = float(soldeEpargne) 
        else:
        #    si soldeCompte != d'un int ou float, alors on stoppe le programme
           raise TypeError("⛔️ "f'Le solde initial doit être un nombre! Type de solde proposé: {type(soldeEpargne)}')

    def getSoldeEpargne(self):
        print(f'Le solde de votre compte épargne est de: {self.__soldeEpargne}')

    def verifierDepot(self, montant):
        if montant > 200:
            self.__soldeEpargne += montant
            print("✅ " f'Vous avez ajouté {montant} € à votre épargne. Montant actualisé: {self.__soldeEpargne}')
        else:
            print("❌" f'Votre dépôt doit être supérieur à 200€ ! Dépôt actuel : {montant}')
        return self.__soldeEpargne    

    def autoriserRetrait(self, montant):
        if self.__soldeEpargne < 1000:
            print("🚫 " f'Retrait autorisé à partir de 1000€ d\'épargne disponible. Montant épargné actuel: {self.__soldeEpargne}') 
        else:
            self.__soldeEpargne -= montant
            print("✅ " f'Retrait effectué: {montant}. Epargne actualisée: {self.__soldeEpargne}')
            return self.__soldeEpargne           

#  instanciation de la class compteEnLigne:
monCompte = compteEnLigne(100)
print(monCompte)
print()
monCompte.getSoldeCompte()
print()
print(monCompte.deposer.__doc__)
print()
monCompte.listeOperations(operations)
print()
monCompte.retirer(100)


# instanciation de la class epargne:
print()
print()
monEpargne = epargne(100)
monEpargne.getSoldeEpargne()
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
       