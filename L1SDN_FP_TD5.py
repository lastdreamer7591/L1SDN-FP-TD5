# Exercice 1 - Le Shaker (2021) - Une histoire de couleur

from math import ceil # ceil est une fonction qui permet d'arronde à l'entier supérieur
def shaker_2021_exo_1(c1, c2):
    """Retourne la couleur moyenne entre c1 et c2
    :param c1: (int)
    :param c2: (int)
    :return: (int) la couleur moyenne
    """
    return ceil((c1 + c2) / 2)

# Exercice 2 - Le Shaker (2021) - Gros tas de bouquins

def genre(livre):
    """
    Récupère le genre du livre.
    :param livre: (tuple) Un tuple représentant un livre. Le premier élément du tuple est supposé être le genre du livre.
    :return: (str) Le genre du livre.
    """
    return livre[0]

def temps_lecture(livre):
    """
    Récupère le temps de lecture estimé du livre.
    :param livre: (tuple) Un tuple représentant un livre. Le deuxième élément du tuple est supposé être le temps de lecture du livre.
    ;return: (int) Le temps de lecture estimé du livre en minutes.
    """
    return livre[1]

def shaker_2021_exo_2(TF, TP, TA, livres):
    """Test si le jury aura le temps de lire tous les livres de leur catégorie
    :param TF: (int) Temps pour le jury Fantastique
    :param TP: (int) Temps pour le jury Policier
    :param TA: (int) Temps pour le jury Autre
    :param livre: (list) Liste des livres
    :return: (bool) True si le jury a le temps de lire tous les livres, False sinon"""
    for livre in livres:
        if livre[0] == "F":
            TF -= livre[1]
            if TF < 0:
                return False
        elif livre[0] == "P":
            TP -= livre[1]
            if TP < 0:
                return False
        else:
            TA -= livre[1]
            if TA < 0:
                return False
    return True

# Exercice 3 - Orange (2021) - La ferme familiale

def entrelacement(mot_1, mot_2):
    """Retourne une chaîne de caractère qui correspond à l'entrelacement des chaînes <mot_1> et <mot_2>
    :param mot_1: (str)
    :param mot_2: (str)
    :return: (str) l'entrelacement des chaînes <mot_1> et <mot_2>
    """
    nv_mot = ""
    for i in range(len(mot_1)):
        nv_mot += mot_1[i] + mot_2[i]
    return nv_mot

# Exercice 4 - Orange (2021) - Pré carré

def longueur_haie(parcelles):
    """Retourne la longueur totale de haie à planter pour délimiter les parcelles.
    :param parcelles: (list)
    :return: (int) la longueur totale de haie à planter pour délimiter les parcelles.
    """
    total = 2 * sum(parcelles) + parcelles[0] + parcelles[-1]
    for i in range(1, len(parcelles)):
        total += max(parcelles[i], parcelles[i-1])
    return total

# Exercice 5 - Battle Dev (2021) - Décollage !

def decollage(boutons):
    """Retourne l'élément qui apparait EXACTEMENT 2 fois dans la liste
    :param boutons: (list)
    :return: (str) l'élément qui apparait EXACTEMENT 2 fois dans la liste"""
    for i in range(len(boutons)):
        cpt = 1
        for j in range(0, len(boutons)):
            if boutons[i] == boutons[j] and j != i:
                cpt += 1
        if cpt == 2:
            return boutons[i]
    return None

