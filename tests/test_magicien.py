import pytest
from classes.magicien import Magicien
from classes.personnage import Personnage

def test_lancer_sort():
    magicien = Magicien("MagicienTest", 100, 10, 5, 15)
    cible = Personnage("CibleTest", 100, 10, 5)
    magicien.lancer_sort(cible)
    assert cible.vie == 70