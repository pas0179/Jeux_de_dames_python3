"""
    class pour les deplacements des dames blanches ou noires

"""

from fonctions import (
    depl_pion_bas_droit,
    depl_pion_bas_gauche,
    depl_pion_haut_droit,
    depl_pion_haut_gauche,
    # ident_pion_noir_blanc,
)


class DeplDames:
    def __init__(
        self,
        dame_select,
        lst_case_vide,
    ):
        self.id = id  # id de la dame
        self.dame_select = dame_select  # Pos de la dame_select
        self.lst_case_vide = lst_case_vide  # liste des cases vides

        self.sol = "solution_"
        self.compteur = 0

        self.dict_depl = {}

        self.solution_depl_dame()

    def solution_depl_dame(self):
        self.dict_depl = {}

        # color_dame_select = ident_pion_noir_blanc(self.id)

        depl_b_g = depl_pion_bas_gauche(self.dame_select)
        depl_b_d = depl_pion_bas_droit(self.dame_select)
        depl_h_g = depl_pion_haut_gauche(self.dame_select)
        depl_h_d = depl_pion_haut_droit(self.dame_select)

        if depl_b_g in self.lst_case_vide:
            self.compteur += 1
            self.dict_depl[self.sol + str(self.compteur)] = [self.dame_select, depl_b_g]

            # while True:
            #     if depl_b_g in self.lst_case_vide:
            #         self.dict_depl[self.sol + str(self.compteur)].append(depl_b_g)
            #     else:
            #         break

        elif depl_b_d in self.lst_case_vide:
            self.compteur += 1
            self.dict_depl[self.sol + str(self.compteur)] = [self.dame_select, depl_b_d]

            # while True:
            #     if depl_b_d in self.lst_case_vide:
            #         self.dict_depl[self.sol + str(self.compteur)].append(depl_b_d)
            #     else:
            #         break

        elif depl_h_g in self.lst_case_vide:
            self.compteur += 1
            self.dict_depl[self.sol + str(self.compteur)] = [self.dame_select, depl_h_g]

            # while True:
            #     if depl_h_g in self.lst_case_vide:
            #         self.dict_depl[self.sol + str(self.compteur)].append(depl_h_g)
            #     else:
            #         break

        elif depl_h_d in self.lst_case_vide:
            self.compteur += 1
            self.dict_depl[self.sol + str(self.compteur)] = [self.dame_select, depl_h_d]

            # while True:
            #     if depl_h_d in self.lst_case_vide:
            #         self.dict_depl[self.sol + str(self.compteur)].append(depl_h_d)
            #     else:
            #         break
        
        else:
            pass


