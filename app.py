import streamlit as st
import random
from classes.guerrier import Guerrier
from classes.magicien import Magicien
from classes.archer import Archer

st.title("Jeu de Combat - POO avec Interface Streamlit")
st.write("Créez vos personnages et lancez des combats entre eux !")

# Création des personnages
if "personnages" not in st.session_state:
    st.session_state.personnages = []

type_personnage = st.selectbox("Type de personnage à créer", ["Guerrier", "Magicien", "Archer"])
nom = st.text_input("Nom du personnage:")
vie = st.number_input("Points de vie:", min_value=0, max_value=200, value=100)
vitesse = st.number_input("Vitesse:", min_value=0, max_value=100, value=10)
esquive = st.number_input("Esquive:", min_value=0, max_value=100, value=5)

if type_personnage == "Guerrier":
    force = st.number_input("Force:", min_value=0, max_value=100, value=20)
    if st.button("Créer le Guerrier"):
        guerrier = Guerrier(nom, vie, vitesse, esquive, force)
        st.session_state.personnages.append(guerrier)
        st.success(f"Guerrier {nom} créé avec succès !")

elif type_personnage == "Magicien":
    mana = st.number_input("Mana:", min_value=0, max_value=100, value=30)
    if st.button("Créer le Magicien"):
        magicien = Magicien(nom, vie, vitesse, esquive, mana)
        st.session_state.personnages.append(magicien)
        st.success(f"Magicien {nom} créé avec succès !")

elif type_personnage == "Archer":
    precision = st.number_input("Précision:", min_value=0, max_value=100, value=25)
    if st.button("Créer l'Archer"):
        archer = Archer(nom, vie, vitesse, esquive, precision)
        st.session_state.personnages.append(archer)
        st.success(f"Archer {nom} créé avec succès !")

# Affichage des personnages créés
if st.session_state.personnages:
    st.subheader("Personnages créés:")
    for personnage in st.session_state.personnages:
        st.write(personnage)

# Simulation de combat
st.subheader("Simulation de Combat")
if len(st.session_state.personnages) >= 2:
    perso1 = st.selectbox("Choisissez le premier personnage", st.session_state.personnages, format_func=lambda x: x.nom)
    perso2 = st.selectbox("Choisissez le deuxième personnage", [p for p in st.session_state.personnages if p != perso1], format_func=lambda x: x.nom)

    if st.button("Lancer le Combat"):
        tour = 1
        vainqueur = None
        while perso1.est_vivant() and perso2.est_vivant():
            st.write(f"### Tour {tour}")

            # Personnage 1 attaque personnage 2 avec des dégâts aléatoires
            degats_p1 = random.randint(5, 20)
            perso2.recevoir_degats(degats_p1)
            st.write(f"{perso1.nom} attaque {perso2.nom} et inflige {degats_p1} points de dégâts. {perso2.nom} a maintenant {perso2.vie} points de vie restants.")

            if not perso2.est_vivant():
                vainqueur = perso1
                break

            # Personnage 2 attaque personnage 1 avec des dégâts aléatoires
            degats_p2 = random.randint(5, 20)
            perso1.recevoir_degats(degats_p2)
            st.write(f"{perso2.nom} attaque {perso1.nom} et inflige {degats_p2} points de dégâts. {perso1.nom} a maintenant {perso1.vie} points de vie restants.")

            if not perso1.est_vivant():
                vainqueur = perso2
                break

            # Passer au tour suivant
            tour += 1

        # Affichage du vainqueur avec une "modale" simulée
        if vainqueur:
            st.markdown(f"## 🎉 Le combat est terminé ! 🎉")
            st.markdown(f"### **{vainqueur.nom} est le grand vainqueur !**")
            st.balloons()  # Animation de ballons pour célébrer la victoire
else:
    st.warning("Veuillez créer au moins deux personnages pour lancer un combat.")