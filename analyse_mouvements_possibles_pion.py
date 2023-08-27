"""
Class pour l'analyse des coups possible pour chaque pions blancs 
et noirs.
L'analyse doit se faire a chaque fois que c'est le tour du joueur
qui joue.

"""


class AnalyseCoupsPossible:

    def __init__(self, id, color_pion, pos_pion, lst_case_vide, lst_pos_pn, lst_pos_pb):

        self.id = id
        self.color_pion = color_pion
        self.pos_pion = pos_pion
        self.lst_case_vide = lst_case_vide
        self.lst_pos_pn = lst_pos_pn
        self.lst_pos_pb = lst_pos_pb


    def analyse_coups_possible_pionb(self):
        pass


