"""
    class pour supprimer les pions noirs ou blanc
    pendant le jeu

"""
from fonctions import ident_pion_noir_blanc


class SuppPion:
    """Class pour supprimer les pions noirs ou blancs"""
    def __init__(
        self,
        id_pion,
        oldpos,
        newpos,
        lst_coord,
        lst_case_poss,
        lst_pn_sup,
        lst_pb_sup,
    ):
        """Initialisation des attributs"""
        self.id_pion = id_pion
        self.pos_dep = oldpos
        self.pos_arr = newpos
        self.lst_coord = lst_coord
        self.lst_case_possible = lst_case_poss
        self.lst_pn_sup = lst_pn_sup
        self.lst_pb_sup = lst_pb_sup

        """ Initialisation des variables pour les methodes """
        self.coord_pion_sup = []

        self.color_pion = ident_pion_noir_blanc(self.id_pion)

    def nettoyage_lst_coord(self):
        """Nettoie et renvoie une liste de coordonnées"""
        lst_temp1 = []
        lst_temp2 = []
        lst_temp = []

        for val in self.lst_coord:
            if val not in lst_temp1 and val != ():
                lst_temp1.append(val)
            else:
                pass

        for val in lst_temp1:
            if val not in self.pos_dep and val not in self.pos_arr:
                lst_temp2.append(val)
            else:
                pass

        lst_temp = lst_temp2.copy()
        for val in lst_temp:
            if val in self.lst_case_possible:
                lst_temp2.remove(val)
            else:
                pass

        return lst_temp2

    def sup_pion(self):
        """Fonction qui supprime les pions noirs ou blancs"""
        if self.pos_arr in self.lst_case_possible:
            lst_pion_sup = self.nettoyage_lst_coord()

            for val in lst_pion_sup:
                if val in self.lst_pn_sup or val in self.lst_pb_sup:
                    self.coord_pion_sup.append(val)
                else:
                    pass
        else:
            pass

        return self.coord_pion_sup
