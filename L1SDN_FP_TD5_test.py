# Importer les fonctions du module à tester
from L1SDN_FP_TD5 import *

def test_shaker_2021_exo_1():
    assert shaker_2021_exo_1(3, 5) == 4
    assert shaker_2021_exo_1(10, 20) == 15
    assert shaker_2021_exo_1(7, 7) == 7
    
def test_shaker_2021_exo_2():
    livres = [("F", 120), ("P", 90), ("A", 150)]
    assert shaker_2021_exo_2(130, 100, 160, livres) == True
    assert shaker_2021_exo_2(100, 100, 160, livres) == False
    assert shaker_2021_exo_2(130, 80, 160, livres) == False

def test_entrelacement():
    assert entrelacement("abc", "123") == "a1b2c3"
    assert entrelacement("hello", "world") == "hweolrllod"
    assert entrelacement("aaa", "bbb") == "ababab"

def test_longueur_haie():
    assert longueur_haie([1, 2, 3]) == 21
    assert longueur_haie([4, 5, 6, 7]) == 73
    assert longueur_haie([2, 2, 2, 2]) == 26

def test_decollage():
    assert decollage(["A", "B", "A", "C", "D", "B"]) == "A"
    assert decollage(["A", "B", "C", "D", "B", "E", "F", "C"]) == "B"
    assert decollage(["A", "A", "B", "C", "D"]) == "A"