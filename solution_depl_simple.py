# Dictionnaires des solutions de saut
from fonctions import (
    depl_pion_bas_droit,
    depl_pion_bas_gauche,
    depl_pion_haut_droit,
    depl_pion_haut_gauche,
    # ident_pion_noir_blanc,
)


class Deplacement:
    def __init__(self, pion_select, color_pion, lst_case_vide, pos_pn, pos_pb):
        self.pion = pion_select
        self.color_pion = color_pion
        self.lst_casevide = lst_case_vide
        self.pos_pn = pos_pn
        self.pos_pb = pos_pb

        self.dict_depl = {}

        self.compteur = 0

        self.sol = "solution_"

        self.solution_deplacement()

    """
    Fonction qui retourne un dictionnaire avec la position de départ
     et la position possible d'arrivée pour pion noir et blanc
    """

    def solution_deplacement(self):
        self.dict_depl = {}

        # On récupère par rapport a l'id la couleur du pion selectionné
        # color_pion_select = ident_pion_noir_blanc(self.id)

        # On récupère les nouvelles valeurs de déplacement d'une case
        # pour le pion noir
        depl_b_g = depl_pion_bas_gauche(self.pion)
        depl_b_d = depl_pion_bas_droit(self.pion)

        # On récupère les nouvelles valeurs de déplacement d'une case
        # pour le pion blanc
        depl_h_g = depl_pion_haut_gauche(self.pion)
        depl_h_d = depl_pion_haut_droit(self.pion)

        # Si le pion est noir il ne peut que descendre +y
        if self.color_pion == "noir":
            self.compteur += 1
            if depl_b_g in self.lst_casevide:
                self.dict_depl[self.sol + str(self.compteur)] = [self.pion, depl_b_g]

            if depl_b_d in self.lst_casevide:
                self.compteur += 1
                self.dict_depl[self.sol + str(self.compteur)] = [self.pion, depl_b_d]
            else:
                pass

        elif self.color_pion == "blanc":
            if depl_h_g in self.lst_casevide:
                self.compteur += 1
                self.dict_depl[self.sol + str(self.compteur)] = [self.pion, depl_h_g]

            if depl_h_d in self.lst_casevide:
                self.compteur += 1
                self.dict_depl[self.sol + str(self.compteur)] = [self.pion, depl_h_d]
            else:
                pass

        else:
            pass

        # print(f"deplacement simple: {self.dict_depl}")
