import random

class Personnage:
    def __init__(self, hp, degats):
        self.hp = hp
        self._degats = degats  # Attribut protégé

    def get_hp(self):
        """Retourne les points de vie actuels du personnage."""
        return self.hp

    def get_degats(self):
        return self._degats  # Utilisez l'attribut protégé

    def recevoir_attaque(self, degats):
        """Méthode pour gérer les dégâts subis par le personnage lors d'une attaque."""
        self.hp -= degats
        if self.hp < 0:
            self.hp = 0

    def estMort(self):
        """Vérifie si le personnage est mort."""
        return self.hp == 0 

class Guerrier(Personnage):
    def __init__(self):
        super().__init__(hp=15, degats=[1, 3])

    def attaquer(self, cible):
        degats_infliges = random.randint(self.get_degats()[0], self.get_degats()[1]) 
        cible.recevoir_attaque(degats_infliges) 

class Mage(Personnage):
    def __init__(self):
        super().__init__(hp=8, degats=[2, 4])

    def attaquer(self, cible):
        degats_infliges = random.randint(self.get_degats()[0], self.get_degats()[1])
        cible.recevoir_attaque(degats_infliges) 

class Archer(Personnage):
    def __init__(self):
        super().__init__(hp=12, degats=[1, 2])

    def attaquer(self, cible):
        degats_infliges = random.randint(self.get_degats()[0], self.get_degats()[1])
        cible.recevoir_attaque(degats_infliges) 

class Nain(Personnage):
    def __init__(self):
        super().__init__(hp=14, degats=[2, 3])

    def attaquer(self, cible):
        degats_infliges = random.randint(self.get_degats()[0], self.get_degats()[1])
        cible.recevoir_attaque(degats_infliges) 
    

def choisir_classe():
    """Permet à l'utilisateur de choisir une classe de personnage."""
    classes_disponibles = {
        'guerrier': Guerrier,
        'mage': Mage,
        'archer': Archer,
        'nain': Nain,
    }

    choix = input("Choisissez votre classe (guerrier, mage, archer) : ").lower()

    if choix in classes_disponibles:
        return classes_disponibles[choix]() 
    else:
        raise ValueError("Classe non valide choisie.")