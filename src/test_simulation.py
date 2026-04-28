import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from etrevivant import EtreVivant
from lapin import Lapin
from renard import Renard

# Test 1 : un lapin est vivant au départ
def test_lapin_vivant():
    lapin = Lapin(1, 1)
    assert lapin.est_vivant() == True

# Test 2 : un lapin mange et gagne de l'énergie
def test_lapin_mange():
    lapin = Lapin(1, 1)
    energie_avant = lapin.energie
    lapin.manger()
    assert lapin.energie > energie_avant

# Test 3 : un animal vieillit
def test_vieillir():
    lapin = Lapin(1, 1)
    lapin.vieillir()
    assert lapin.age == 1

# Test 4 : un renard chasse et le lapin meurt
def test_renard_chasse():
    renard = Renard(1, 1)
    lapin = Lapin(2, 2)
    renard.chasser(lapin)
    assert lapin.est_vivant() == False

# Test 5 : un lapin se reproduit
def test_lapin_reproduit():
    lapin = Lapin(1, 1)
    bebe = lapin.se_reproduire()
    assert bebe is not None