from .personnage import Personnage

class Magicien(Personnage):
    def __init__(self, nom, vie, vitesse, esquive, mana):
        super().__init__(nom, vie, vitesse, esquive)
        self.mana = mana

    def lancer_sort(self, cible):
        degats = self.mana * 2
        cible.recevoir_degats(degats)
        return f"{self.nom} lance un sort sur {cible.nom} et inflige {degats} points de dégâts."