class Personnage:
    """Classe de base pour les personnages."""
    def __init__(self, nom, vie, vitesse, esquive):
        self.nom = nom
        self.vie = vie
        self.vitesse = vitesse
        self.esquive = esquive

    def est_vivant(self):
        return self.vie > 0

    def recevoir_degats(self, degats):
        self.vie = max(0, self.vie - degats)

    def __str__(self):
        return f"{self.nom} - Vie: {self.vie}, Vitesse: {self.vitesse}, Esquive: {self.esquive}"