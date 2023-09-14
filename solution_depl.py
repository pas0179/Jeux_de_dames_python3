"""
    Class pour gerer les possibilités de déplacement simple
    de sauts complexe. On se sert de 2 Class:
    1er : depl_simple.py    2eme : sauts.py 

"""

from solution_depl_simple import Deplacement
from solution_depl_saut import Sauts


class Move:
    """Class pour gerer les possibilités de déplacement simple"""
    def __init__(self, pos_pion, color_pion, lst_case_vide, pos_pn, pos_pb):
        """Initialisation des attributs de class"""
        self.pos_pion = pos_pion
        self.color_pion = color_pion
        self.lst_case_vide = lst_case_vide
        self.pos_pn = pos_pn
        self.pos_pb = pos_pb

        """Initialisation des variables pour les méthodes"""
        self.dict_solution = {}
        self.lst_pn_sup = []
        self.lst_pb_sup = []

        """Initialisation des calculs"""
        self.start_calcul_possibilite()

    def start_calcul_possibilite(self):
        """Initialisation des calculs"""
        sol = Sauts(
            # self.id,
            self.pos_pion,
            self.color_pion,
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
                # self.id,
                self.pos_pion,
                self.color_pion,
                self.lst_case_vide,
                self.pos_pn,
                self.pos_pb,
            )
            self.dict_solution = sol2.dict_depl
