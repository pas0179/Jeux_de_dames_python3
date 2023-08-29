"""
Class pour l'analyse des coups possible pour chaque pions blancs 
et noirs.
L'analyse doit se faire a chaque fois que c'est le tour du joueur
qui joue.

"""



class AnalyseCoupsPossible:
    def __init__(
        self, lst_id_dame, color_pion, pos_pion, lst_case_vide, lst_pos_pn, lst_pos_pb
    ):
        self.id = lst_id_dame
        self.color_pion = color_pion
        self.pos_pion = pos_pion
        self.lst_case_vide = lst_case_vide
        self.lst_pos_pn = lst_pos_pn
        self.lst_pos_pb = lst_pos_pb

        """ J'ai considéré les dames comme des pions et j'ai inserer
        ces coordonnées dans les listes des positions pions noirs 
        et blancs.
        - A faire - Récupérer les coordonnées des dames avec leurs IDs, 
            leurs couleurs et les positions des pions noirs et blancs

        - A faire - Faire l'analyse des meilleurs coups possible 
            pour chaque dame de la couleur du pion qui joue

        """

