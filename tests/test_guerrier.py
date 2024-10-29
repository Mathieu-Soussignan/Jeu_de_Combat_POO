import pytest
from classes.guerrier import Guerrier
from classes.personnage import Personnage

def test_attaquer():
    guerrier = Guerrier("GuerrierTest", 100, 10, 5, 20)
    cible = Personnage("CibleTest", 100, 10, 5)
    guerrier.attaquer(cible)
    assert cible.vie == 80