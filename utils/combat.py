# Ce fichier peut contenir des fonctions utilitaires pour la logique de combat
def determiner_vainqueur(perso1, perso2):
    """Détermine le vainqueur du combat entre deux personnages."""
    if perso1.est_vivant() and not perso2.est_vivant():
        return perso1.nom
    elif perso2.est_vivant() and not perso1.est_vivant():
        return perso2.nom
    else:
        return "Aucun vainqueur, c'est une égalité !"