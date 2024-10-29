import pytest
from classes.archer import Archer
from classes.personnage import Personnage

def test_tirer():
    archer = Archer("ArcherTest", 100, 10, 5, 20)
    cible = Personnage("CibleTest", 100, 10, 5)
    archer.tirer(cible)
    assert cible.vie == 70