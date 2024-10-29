from .personnage import Personnage

class Guerrier(Personnage):
    def __init__(self, nom, vie, vitesse, esquive, force):
        super().__init__(nom, vie, vitesse, esquive)
        self.force = force

    def attaquer(self, cible):
        cible.recevoir_degats(self.force)
        return f"{self.nom} attaque {cible.nom} et inflige {self.force} points de dégâts."