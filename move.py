"""
    Class pour gerer les possibilités de déplacement simple
    de sauts complexe. On se sert de 2 Class:
    1er : depl_simple.py    2eme : sauts.py 

"""

from depl_simple import Deplacement
from sauts import Sauts


class Move:
    def __init__(self, id, pos_pion, lst_case_vide, pos_pn, pos_pb):
        self.id = id
        self.pos_pion = pos_pion
        self.lst_case_vide = lst_case_vide
        self.pos_pn = pos_pn
        self.pos_pb = pos_pb

        self.dict_solution = {}
        self.lst_pn_sup = []
        self.lst_pb_sup = []

        self.start_calcul_possibilite()

    def start_calcul_possibilite(self):
        sol = Sauts(
            self.id,
            self.pos_pion,
            self.lst_case_vide,
            self.pos_pn,
            self.pos_pb,
        )

        sol1 = sol.dict_saut
        pnsup = sol.lst_pn_sup
        pbsup = sol.lst_pb_sup

        if len(sol1) > 0:
            self.dict_solution = sol1
            self.lst_pn_sup = pnsup
            self.lst_pb_sup = pbsup

        else:
            sol2 = Deplacement(
                self.id, self.pos_pion, self.lst_case_vide, self.pos_pn, self.pos_pb
            )
            self.dict_solution = sol2.dict_depl
