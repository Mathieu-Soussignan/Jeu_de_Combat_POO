from .personnage import Personnage

class Archer(Personnage):
    def __init__(self, nom, vie, vitesse, esquive, precision):
        super().__init__(nom, vie, vitesse, esquive)
        self.precision = precision

    def tirer(self, cible):
        degats = self.precision * 1.5
        cible.recevoir_degats(degats)
        return f"{self.nom} tire une flèche sur {cible.nom} et inflige {degats} points de dégâts."