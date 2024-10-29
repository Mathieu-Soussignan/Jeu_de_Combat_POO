# Jeu de Combat avec Streamlit

## Description
Ce projet est une application web interactive développée en **Python** et **Streamlit** qui permet aux utilisateurs de créer des personnages de différents types et de les faire s'affronter dans des combats. L'objectif est d'apprendre les concepts de la **Programmation Orientée Objet (POO)**, de pratiquer l'**héritage**, et d'intégrer une interface interactive avec Streamlit.

## Fonctionnalités
- **Création de Personnages** : Les utilisateurs peuvent créer trois types de personnages – **Guerrier**, **Magicien**, et **Archer** – avec des caractéristiques personnalisées telles que les points de vie, la vitesse, l'esquive, et des attributs spécifiques à chaque type.
- **Combat Interactif** : Deux personnages peuvent s'affronter dans un combat où ils attaquent tour à tour, avec des dégâts aléatoires pour ajouter de la variété.
- **Animations de Fin de Combat** : Des animations telles que des ballons sont utilisées pour célébrer le vainqueur.

## Installation
1. **Cloner le Répertoire** :
   ```bash
   git clone <url-du-repository>
   cd jeu_combat_streamlit
   ```

2. **Installer les Dépendances** :
   - Assurez-vous d'avoir Python 3.7+ installé.
   - Installez les dépendances listées dans le fichier `requirements.txt` :
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'Application** :
   ```bash
   streamlit run app.py
   ```
   Cela ouvrira l'application dans votre navigateur par défaut.

## Arborescence du Projet
```
jeu_combat_streamlit/
|
|-- app.py                     # Fichier principal contenant le code Streamlit
|-- requirements.txt           # Liste des bibliothèques nécessaires pour exécuter le projet
|-- README.md                  # Documentation du projet
|-- assets/                    # Répertoire pour les fichiers médias et ressources
|   |-- logo.png               # Logo ou images pour l'interface Streamlit
|
|-- classes/                   # Répertoire contenant les classes du projet
|   |-- personnage.py          # Classe de base Personnage
|   |-- guerrier.py            # Classe Guerrier qui hérite de Personnage
|   |-- magicien.py            # Classe Magicien qui hérite de Personnage
|   |-- archer.py              # Classe Archer qui hérite de Personnage
|
|-- utils/                     # Répertoire pour les fonctions utilitaires
|   |-- combat.py              # Fonctions pour gérer la logique de combat
|
|-- tests/                     # Répertoire pour les tests unitaires
|   |-- test_personnage.py     # Tests pour la classe Personnage
|   |-- test_guerrier.py       # Tests pour la classe Guerrier
|   |-- test_magicien.py       # Tests pour la classe Magicien
|   |-- test_archer.py         # Tests pour la classe Archer
```

## Types de Personnages
- **Guerrier** : Possède une force élevée et peut infliger des dégâts importants à l'adversaire.
- **Magicien** : Utilise du mana pour lancer des sorts puissants qui infligent des dégâts proportionnels au mana.
- **Archer** : Tire des flèches avec une précision accrue, infligeant des dégâts basés sur cette précision.

## Utilisation
1. **Créer des Personnages** :
   - Choisissez le type de personnage (Guerrier, Magicien, Archer).
   - Saisissez les caractéristiques telles que le nom, les points de vie, la vitesse, l'esquive, et les attributs spécifiques.
2. **Lancer un Combat** :
   - Sélectionnez deux personnages créés.
   - Lancez le combat pour voir les personnages s'affronter tour à tour jusqu'à ce qu'il y ait un vainqueur.
3. **Animations** :
   - Des ballons apparaissent lorsque le vainqueur est annoncé.

## Tests Unitaires
Les tests unitaires utilisent **pytest** pour vérifier le bon fonctionnement des classes et des méthodes :
- `test_personnage.py` : Vérifie la méthode `recevoir_degats()` et la gestion des points de vie.
- `test_guerrier.py`, `test_magicien.py`, `test_archer.py` : Vérifient les attaques spécifiques à chaque personnage.

Pour exécuter les tests unitaires :
```bash
pytest tests/
```

## Dépendances
Les dépendances principales de ce projet sont :
- **Streamlit** : Pour créer l'interface utilisateur interactive.
- **pytest** : Pour les tests unitaires.

Toutes les dépendances sont listées dans `requirements.txt`.

## Améliorations Possibles
- **Ajouter de Nouveaux Types de Personnages** : Par exemple, un **Assassin** avec une haute vitesse et une capacité d'esquive accrue.
- **Ajouter des Compétences Spéciales** : Chaque personnage pourrait avoir une compétence spéciale utilisable une fois par combat.
- **Animations Plus Complexes** : Utiliser des GIFs ou intégrer des animations plus dynamiques pour enrichir l'expérience utilisateur.

## Contribution
Les contributions sont les bienvenues. Pour contribuer :
1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b nouvelle-fonctionnalite`).
3. Commitez vos modifications (`git commit -am 'Ajoute une nouvelle fonctionnalité'`).
4. Poussez la branche (`git push origin nouvelle-fonctionnalite`).
5. Créez une Pull Request.

## Licence
Ce projet est sous licence MIT.

## Auteurs
- **Mathieu Soussignan** : Créateur de l'application et développeur principal.

