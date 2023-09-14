"""
    Class pour gerer les sauts possibles d'un pion ou d'une
    solution de possibilités
"""

from fonctions import (
    saut_bas_d,
    saut_bas_g,
    saut_haut_d,
    saut_haut_g,
)


class Sauts:
    """Class pour gerer les sauts possibles d'un pion"""
    def __init__(self, pos_pion, color_pion, lst_case_vide, pos_pn, pos_pb):

        """Initialisation des attributs"""
        self.pos_pion = pos_pion
        self.color_pion = color_pion
        self.lst_case_vide = lst_case_vide
        self.pos_pn = pos_pn
        self.pos_pb = pos_pb
        
        """ Initialisation des variables pour les methodes """
        self.dict_saut = {}
        self.lst_pn_sup = []
        self.lst_pb_sup = []

        self.compteur = 0

        self.sol = "Solution_"

        """Initialisation de la méthode sauts"""
        self.sauts()

    """
    Fonction qui retourne un dictionnaire sur les possible sauts
    d'un pion noir ou blanc: N° de solution +
    liste [ position départ, position d'arrivée]
    """

    def saut_possible(
        self, pos_pion, oldpos, color_pion, lst_case_vide, pos_pn, pos_pb
    ):
        """Créer et retourne un dictionnaire des sauts possibles"""
        dict_saut = {}
        lst_pn_sup = []
        lst_pb_sup = []

        # On commance par la couleur du pion
        # color_pion = ident_pion_noir_blanc(id)

        # On définie les listes pour les pions a supprimer

        saut1, pnsup1, pbsup1 = saut_bas_g(
            pos_pion, color_pion, lst_case_vide, pos_pn, pos_pb
        )
        saut2, pnsup2, pbsup2 = saut_bas_d(
            pos_pion, color_pion, lst_case_vide, pos_pn, pos_pb
        )
        saut3, pnsup3, pbsup3 = saut_haut_d(
            pos_pion, color_pion, lst_case_vide, pos_pn, pos_pb
        )
        saut4, pnsup4, pbsup4 = saut_haut_g(
            pos_pion, color_pion, lst_case_vide, pos_pn, pos_pb
        )

        if len(saut1) > 0 and saut1 != oldpos:
            self.compteur += 1
            dict_saut[self.sol + str(self.compteur)] = [pos_pion, saut1]
            if color_pion == "noir":
                lst_pb_sup.append(pbsup1)
            else:
                lst_pn_sup.append(pnsup1)

        if len(saut2) > 0 and saut2 != oldpos:
            self.compteur += 1
            dict_saut[self.sol + str(self.compteur)] = [pos_pion, saut2]
            if color_pion == "noir":
                lst_pb_sup.append(pbsup2)
            else:
                lst_pn_sup.append(pnsup2)

        if len(saut3) > 0 and saut3 != oldpos:
            self.compteur += 1
            dict_saut[self.sol + str(self.compteur)] = [pos_pion, saut3]
            if color_pion == "noir":
                lst_pb_sup.append(pbsup3)
            else:
                lst_pn_sup.append(pnsup3)

        if len(saut4) > 0 and saut4 != oldpos:
            self.compteur += 1
            dict_saut[self.sol + str(self.compteur)] = [pos_pion, saut4]
            if color_pion == "noir":
                lst_pb_sup.append(pbsup4)
            else:
                lst_pn_sup.append(pnsup4)

        else:
            pass

        return dict_saut, lst_pn_sup, lst_pb_sup

    def find_last_pos_dict(self, dict_temp):
        """Trouver la derniere position dans un dictionnaire"""
        lst_last_pos = []

        # Récup des dernieres positions dans le dictionnaire
        lst_last_pos = [(val[-2], val[-1]) for val in dict_temp.values()]

        # Nettoyage des doublons dans la liste
        lst_temp1 = []
        lst_temp1 = [val for val in lst_last_pos if val not in lst_temp1]

        if len(lst_temp1) > 0:
            lst_last_pos = lst_temp1
        else:
            pass

        return lst_last_pos

    def maj_nb_solutions_dict(self, dict_1):
        """MAJ du dictionnaire pour N° des solutions"""
        dict_temp = {}
        compteur = 1

        for val in dict_1.values():
            dict_temp[self.sol + str(compteur)] = val
            compteur += 1

        return dict_temp

    def fusion_dict(self, dict_1, dict_2):
        """Fusion de 2 dictionnaires"""
        # Dict1 : self.dict_saut , dict2 : dict_saut
        lg1 = len(dict_1)
        lg2 = len(dict_2)
        dict_fusion = {}

        # On commence par re_numeroté les solutions de dict_saut
        dict_2 = self.maj_nb_solutions_dict(dict_2)

        if lg2 > 0 and lg2 > lg1:
            for key, val in dict_2.items():
                for val2 in dict_1.values():
                    if val[0] == val2[-1] and val[1] != val2[-2]:
                        dict_2[key].insert(0, val2[0])
                    else:
                        continue

            dict_fusion = dict_2

        elif lg1 >= lg2:
            for key, val in dict_1.items():
                for val2 in dict_2.values():
                    if val[-1] == val2[0] and val[-2] != val2[1]:
                        dict_1[key].append(val2[-1])
                    else:
                        continue

            dict_fusion = dict_1
        else:
            pass

        dict_fusion = self.maj_nb_solutions_dict(dict_fusion)

        return dict_fusion

    def sauts(self):
        """Méthode pour créer et retourner un dictionnaire des sauts
        possibles"""
        dict_temp = {}
        dict_saut = {}
        lst_last_pos = []
        pn_sup = []
        pb_sup = []

        # Initialisation de la liste des dernières positions
        lst_last_pos.append(((), self.pos_pion))

        while len(lst_last_pos) > 0:
            dict_saut = {}
            for pos in lst_last_pos:
                dict_temp, pn_sup, pb_sup = self.saut_possible(
                    # self.id,
                    pos[-1],
                    pos[-2],
                    self.color_pion,
                    self.lst_case_vide,
                    self.pos_pn,
                    self.pos_pb,
                )

                if len(dict_temp) > 0:
                    dict_saut.update(dict_temp)

                    if len(pn_sup) > 0:
                        for newpos in pn_sup:
                            self.lst_pn_sup.append(newpos)
                    elif len(pb_sup) > 0:
                        for newpos in pb_sup:
                            self.lst_pb_sup.append(newpos)
                    else:
                        pass
                else:
                    continue

            if len(dict_saut) > 0:
                self.dict_saut = self.fusion_dict(self.dict_saut, dict_saut)
                lst_last_pos = self.find_last_pos_dict(self.dict_saut)
            else:
                lst_last_pos = []
