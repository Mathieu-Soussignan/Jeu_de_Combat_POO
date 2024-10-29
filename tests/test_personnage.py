import pytest
from classes.personnage import Personnage

def test_recevoir_degats():
    perso = Personnage("Test", 100, 10, 5)
    perso.recevoir_degats(50)
    assert perso.vie == 50
    perso.recevoir_degats(60)
    assert perso.vie == 0