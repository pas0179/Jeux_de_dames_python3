"""

Class pour trouver les solutions de saut de dames

Besoins :
    - 1 Id de la dame
    - 2 Position de la dame
    - 3 Couleur de la dame
    - 4 Liste des cases vides sur lesquelles la dame peut sauter
    - 5 Liste des positions des pions noirs
    - 6 Liste des positions des pions blancs
    - 7 Liste des positions des dames noirs
    - 8 Liste des positions des dames blancs

"""


class SautDame:
    def __init__(
        self,
        id_dame,
        position,
        couleur,
        cases_vides,
        pions_noirs,
        pions_blancs,
        dames_noirs,
        dames_blancs,
    ):
        self.id_dame = id_dame
        self.position = position
        self.couleur = couleur
        self.cases_vides = cases_vides
        self.pions_noirs = pions_noirs
        self.pions_blancs = pions_blancs
        self.dames_noirs = dames_noirs
        self.dames_blancs = dames_blancs
