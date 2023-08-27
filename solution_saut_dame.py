"""

Class pour trouver les solutions de saut de dames

Besoins :
    - 1 Id de la dame
    - 2 Position de la dame
    - 3 Couleur de la dame
    - 4 Liste des cases vides sur lesquelles la dame peut sauter
    - 5 Liste des positions des pions noirs
    - 6 Liste des positions des pions blancs

    On considère que la dame est un pion avec des mouvements
    différents.

"""

from fonctions import (
    saut_bas_g,
)

from solution_depl_dame_simple import SolDeplDames


class SautDame:
    def __init__(self):
        self.dict_depl = {}

        self.lst_pn_sup = []
        self.lst_pb_sup = []

        self.sol_depl = SolDeplDames()

    def calcul_depl_dame_b_gauche(
        self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
    ):
        pn_sup, pb_sup = [], []
        lst_depl_b_g = []
        lst_pn_sup, lst_pb_sup = [], []

        while len(pos_dame) > 0:
            
            """ Vérif si pion adjacent de suite """
            saut_pos, pn_sup, pb_sup = saut_bas_g(
                pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
            )

            if len(saut_pos) > 0:

                if len(pn_sup) > 0:
                    lst_pn_sup.append(pn_sup)

                    pos_dame = pn_sup

                if len(pb_sup) > 0:
                    lst_pb_sup.append(pb_sup)

                    pos_dame = pb_sup

                else:

                    pass

                lst_depl_b_g.append(pos_dame)

            else:

                lst_depl_temp = []
                lst_depl_temp = self.sol_depl.solution_depl_dame_b_gauche(
                    pos_dame,
                    lst_case_vide
                ) 
                if len(lst_depl_temp) > 0:

                    """ on récupère la dernère pos dans la Liste
                    et on regarde si saut possible ou fin de tableau"""
                    last_pos = ()
                    last_pos = lst_depl_temp[-1]

                    lst_depl_b_g = [*lst_depl_temp]

                    pos_dame = last_pos

                else:
                    pos_dame = ()

        return lst_depl_b_g, lst_pn_sup, lst_pb_sup
