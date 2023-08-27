"""
    class pour trouver les solutions de deplacement des dames blanches ou noires

"""

from fonctions import (
    depl_pion_bas_droit,
    depl_pion_bas_gauche,
    depl_pion_haut_droit,
    depl_pion_haut_gauche,
    # ident_pion_noir_blanc,
)


class SolDeplDames:
    def __init__(self):
        self.sol = "solution_"
        self.compteur = 0

        self.dict_depl_b_droit = {}
        self.dict_depl_h_gauche = {}
        self.dict_depl_h_droit = {}

    def solution_depl_dame_b_gauche(self, pos_dame, lst_case_vide):
        lst_depl_b_gauche = []

        while len(pos_dame) > 0:
            depl_temp = ()
            depl_temp = depl_pion_bas_gauche(pos_dame)

            if len(depl_temp) > 0 and depl_temp in lst_case_vide:
                lst_depl_b_gauche.append(depl_temp)

                pos_dame = depl_temp

            else:
                pos_dame = ()

        return lst_depl_b_gauche

    def solution_depl_dame_b_droit(self, pos_dame, lst_case_vide):
        lst_depl_b_droit = []

        while len(pos_dame) > 0:
            depl_temp = ()
            depl_temp = depl_pion_bas_droit(pos_dame)

            if len(depl_temp) > 0 and depl_temp in lst_case_vide:
                lst_depl_b_droit.append(depl_temp)

                pos_dame = depl_temp

            else:
                pos_dame = ()

        return lst_depl_b_droit

    def solution_depl_dame_h_gauche(self, pos_dame, lst_case_vide):
        lst_depl_h_gauche = []

        while len(pos_dame) > 0:
            depl_temp = ()
            depl_temp = depl_pion_haut_gauche(pos_dame)

            if len(depl_temp) > 0 and depl_temp in lst_case_vide:
                lst_depl_h_gauche.append(depl_temp)

                pos_dame = depl_temp

            else:
                pos_dame = ()

        return lst_depl_h_gauche

    def solution_depl_dame_h_droit(self, pos_dame, lst_case_vide):
        lst_depl_h_droit = []

        while len(pos_dame) > 0:
            depl_temp = ()
            depl_temp = depl_pion_haut_droit(pos_dame)

            if len(depl_temp) > 0 and depl_temp in lst_case_vide:
                lst_depl_h_droit.append(depl_temp)

                pos_dame = depl_temp

            else:
                pos_dame = ()

        return lst_depl_h_droit

    """ Créer pour les tests dans main """
    def solution_depl_dame(self, pos_dame, lst_case_vide):
        lst_depl = []

        depl_b_g = self.solution_depl_dame_b_gauche(pos_dame, lst_case_vide)
        depl_b_d = self.solution_depl_dame_b_droit(pos_dame, lst_case_vide)
        depl_h_g = self.solution_depl_dame_h_gauche(pos_dame, lst_case_vide)
        depl_h_d = self.solution_depl_dame_h_droit(pos_dame, lst_case_vide)

        lst_depl = [*depl_b_g, *depl_b_d, *depl_h_g, *depl_h_d]

        return lst_depl
