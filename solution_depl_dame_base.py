"""
class pour trouver les solutions de deplacement des dames blanches
ou noires avec saut ou pas. Le calcul se fait sur les diagonales
suivant la position de la dame.
Solutions pour une dame :
dame depl_h_d et depl_b_g : depl_b_d et depl_h_g
dame depl_h_g et depl_b_d : depl_b_g et depl_h_d
"""

from fonctions import (
    depl_pion_bas_droit,
    depl_pion_bas_gauche,
    depl_pion_haut_droit,
    depl_pion_haut_gauche,
    saut_bas_g,
    saut_bas_d,
    saut_haut_g,
    saut_haut_d,
)


class SolDeplDames:
    """Class pour trouver les solutions de deplacement des dames"""
    def __init__(self, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb):
        self.color_dame = color_dame
        self.lst_case_vide = lst_case_vide
        self.lst_pos_pn = lst_pos_pn
        self.lst_pos_pb = lst_pos_pb

        self.lst_depl = []
        self.dict_saut = {}
        self.new_pos = {}

    def solution_depl_dame_b_gauche(self, position):
        """calcul deplacement diagonale bas gauche"""
        lst_depl = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []
        new_pos_saut = []

        new_pos = position

        while len(new_pos) > 0:
            depl_temp = ()

            depl_temp = depl_pion_bas_gauche(new_pos)

            if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                lst_depl.append(depl_temp)

                new_pos = depl_temp

            else:
                saut_temp, pn_sup, pb_sup = saut_bas_g(
                    new_pos,
                    self.color_dame,
                    self.lst_case_vide,
                    self.lst_pos_pn,
                    self.lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    new_pos_saut.append(saut_temp)
                    if len(pn_sup) > 0:
                        lst_pn_sup.append(pn_sup)
                        lst_depl.append(pn_sup)
                    elif len(pb_sup) > 0:
                        lst_pb_sup.append(pb_sup)
                        lst_depl.append(pb_sup)
                    else:
                        pass

                    lst_depl.append(saut_temp)
                    new_pos = saut_temp

                else:
                    new_pos = ()

        return lst_depl, lst_pn_sup, lst_pb_sup

    def solution_depl_dame_b_droit(self, position):
        """calcul deplacement diagonale bas droite"""
        lst_depl = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []
        new_pos_saut = []

        new_pos = position

        while len(new_pos) > 0:
            depl_temp = ()
            depl_temp = depl_pion_bas_droit(new_pos)

            if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                lst_depl.append(depl_temp)

                new_pos = depl_temp

            else:
                saut_temp, pn_sup, pb_sup = saut_bas_d(
                    new_pos,
                    self.color_dame,
                    self.lst_case_vide,
                    self.lst_pos_pn,
                    self.lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    new_pos_saut.append(saut_temp)

                    if len(pn_sup) > 0:
                        lst_pn_sup.append(pn_sup)
                        lst_depl.append(pn_sup)
                    if len(pb_sup) > 0:
                        lst_pb_sup.append(pb_sup)
                        lst_depl.append(pb_sup)
                    else:
                        pass

                    lst_depl.append(saut_temp)

                    new_pos = saut_temp

                else:
                    new_pos = ()

        return lst_depl, lst_pn_sup, lst_pb_sup

    def solution_depl_dame_h_gauche(self, position):
        """calcul deplacement diagonale haut gauche"""
        lst_depl = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []
        new_pos_saut = []

        new_pos = position

        while len(new_pos) > 0:
            depl_temp = ()
            depl_temp = depl_pion_haut_gauche(new_pos)

            if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                lst_depl.append(depl_temp)

                new_pos = depl_temp

            else:
                saut_temp, pn_sup, pb_sup = saut_haut_g(
                    new_pos,
                    self.color_dame,
                    self.lst_case_vide,
                    self.lst_pos_pn,
                    self.lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    new_pos_saut.append(saut_temp)

                    if len(pn_sup) > 0:
                        lst_pn_sup.append(pn_sup)
                        lst_depl.append(pn_sup)
                    if len(pb_sup) > 0:
                        lst_pb_sup.append(pb_sup)
                        lst_depl.append(pb_sup)
                    else:
                        pass

                    lst_depl.append(saut_temp)

                    new_pos = saut_temp

                else:
                    new_pos = ()

        return lst_depl, lst_pn_sup, lst_pb_sup

    def solution_depl_dame_h_droit(self, position):
        """calcul deplacement diagonale haut droite"""
        lst_depl = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []
        new_pos_saut = []

        new_pos = position

        while len(new_pos) > 0:
            depl_temp = ()
            depl_temp = depl_pion_haut_droit(new_pos)

            if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                lst_depl.append(depl_temp)

                new_pos = depl_temp

            else:
                saut_temp, pn_sup, pb_sup = saut_haut_d(
                    new_pos,
                    self.color_dame,
                    self.lst_case_vide,
                    self.lst_pos_pn,
                    self.lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    new_pos_saut.append(saut_temp)

                    if len(pn_sup) > 0:
                        lst_pn_sup.append(pn_sup)
                        lst_depl.append(pn_sup)
                    if len(pb_sup) > 0:
                        lst_pb_sup.append(pb_sup)
                        lst_depl.append(pb_sup)
                    else:
                        pass

                    lst_depl.append(saut_temp)

                    new_pos = saut_temp

                else:
                    new_pos = ()

        return lst_depl, lst_pn_sup, lst_pb_sup
