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
    def __init__(self):
        self.lst_depl = []

    def solution_depl_dame_b_gauche(
        self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
    ):
        """dame depl_b_g : depl_b_d et depl_h_g"""

        lst_depl_b_gauche = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []

        while len(pos_dame) > 0:
            depl_temp = ()

            """ Methode pour le deplacement simple de la dame """
            depl_temp = depl_pion_bas_gauche(pos_dame)

            if len(depl_temp) > 0 and depl_temp in lst_case_vide:
                lst_depl_b_gauche.append(depl_temp)

                pos_dame = depl_temp

            else:
                """Methode pour le saut sur la même diagonale"""
                saut_temp, pn_sup, pb_sup = saut_bas_g(
                    pos_dame,
                    color_dame,
                    lst_case_vide,
                    lst_pos_pn,
                    lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    """Saut sur la meme diagonale"""
                    if len(pn_sup) > 0:
                        lst_depl_b_gauche.append(pn_sup)
                        lst_pn_sup.append(pn_sup)
                    if len(pb_sup) > 0:
                        lst_depl_b_gauche.append(pb_sup)
                        lst_pb_sup.append(pb_sup)
                    else:
                        pass

                    lst_depl_b_gauche.append(saut_temp)

                    pos_dame = saut_temp

                else:
                    pos_dame = ()

        return lst_depl_b_gauche, lst_pn_sup, lst_pb_sup

    def solution_depl_dame_b_droit(
        self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
    ):
        lst_depl_b_droit = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []

        while len(pos_dame) > 0:
            depl_temp = ()
            depl_temp = depl_pion_bas_droit(pos_dame)

            if len(depl_temp) > 0 and depl_temp in lst_case_vide:
                lst_depl_b_droit.append(depl_temp)

                pos_dame = depl_temp

            else:
                saut_temp, pn_sup, pb_sup = saut_bas_d(
                    pos_dame,
                    color_dame,
                    lst_case_vide,
                    lst_pos_pn,
                    lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    if len(pn_sup) > 0:
                        lst_depl_b_droit.append(pn_sup)
                        lst_pn_sup.append(pn_sup)
                    if len(pb_sup) > 0:
                        lst_depl_b_droit.append(pb_sup)
                        lst_pb_sup.append(pb_sup)
                    else:
                        pass

                    lst_depl_b_droit.append(saut_temp)

                    pos_dame = saut_temp

                else:
                    pos_dame = ()

        return lst_depl_b_droit, lst_pn_sup, lst_pb_sup

    def solution_depl_dame_h_gauche(
        self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
    ):
        lst_depl_h_gauche = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []

        while len(pos_dame) > 0:
            depl_temp = ()
            depl_temp = depl_pion_haut_gauche(pos_dame)

            if len(depl_temp) > 0 and depl_temp in lst_case_vide:
                lst_depl_h_gauche.append(depl_temp)

                pos_dame = depl_temp

            else:
                saut_temp, pn_sup, pb_sup = saut_haut_g(
                    pos_dame,
                    color_dame,
                    lst_case_vide,
                    lst_pos_pn,
                    lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    if len(pn_sup) > 0:
                        lst_depl_h_gauche.append(pn_sup)
                        lst_pn_sup.append(pn_sup)
                    if len(pb_sup) > 0:
                        lst_depl_h_gauche.append(pb_sup)
                        lst_pb_sup.append(pb_sup)
                    else:
                        pass

                    lst_depl_h_gauche.append(saut_temp)

                    pos_dame = saut_temp

                else:
                    pos_dame = ()

        return lst_depl_h_gauche, lst_pn_sup, lst_pb_sup

    def solution_depl_dame_h_droit(
        self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
    ):
        lst_depl_h_droit = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []

        while len(pos_dame) > 0:
            depl_temp = ()
            depl_temp = depl_pion_haut_droit(pos_dame)

            if len(depl_temp) > 0 and depl_temp in lst_case_vide:
                lst_depl_h_droit.append(depl_temp)

                pos_dame = depl_temp

            else:
                saut_temp, pn_sup, pb_sup = saut_haut_d(
                    pos_dame,
                    color_dame,
                    lst_case_vide,
                    lst_pos_pn,
                    lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    if len(pn_sup) > 0:
                        lst_depl_h_droit.append(pn_sup)
                        lst_pn_sup.append(pn_sup)
                    if len(pb_sup) > 0:
                        lst_depl_h_droit.append(pb_sup)
                        lst_pb_sup.append(pb_sup)
                    else:
                        pass

                    lst_depl_h_droit.append(saut_temp)

                    pos_dame = saut_temp

                else:
                    pos_dame = ()

        return lst_depl_h_droit, lst_pn_sup, lst_pb_sup
