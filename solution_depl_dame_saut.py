"""
Class pour gerer les sauts possibles d'une dame
noir ou blanc

"""

from solution_depl_dame_base import SolDeplDames


class SautDames:
    """Class pour gerer les sauts possibles d'une dame"""

    def __init__(
        self,
        pos_dame,
        color_dame,
        lst_case_vide,
        lst_pos_pn,
        lst_pos_pb,
    ):
        """Initialisation des attributs"""
        self.pos_dame = pos_dame
        self.color_dame = color_dame
        self.lst_case_vide = lst_case_vide
        self.lst_pos_pn = lst_pos_pn
        self.lst_pos_pb = lst_pos_pb

        """ Initialisation des variables pour les methodes """
        self.dict_saut = {}
        self.dict_saut2 = {}

        self.dict_other = {}
        self.new_pos = []
        self.new_pos2 = []

        self.lst_depl = []

        self.lst_pn_sup = []
        self.lst_pb_sup = []

        """ Initialisation des compteurs et clé du dictionnaire """
        self.cpt = 0
        self.sol = "Solution_"

        """Initialisation de l'Objet SolDeplDames"""
        self.depl = SolDeplDames(
            self.color_dame,
            self.lst_case_vide,
            self.lst_pos_pn,
            self.lst_pos_pb,
        )

        # self.find_solution_saut_depl()
        self.find_solution_depl()

    def reverse_old_dict_saut(self, dict_old):
        """Inverse le dictionnaire des sauts"""
        dict_temp = {}
        cpt = 0

        for val in dict_old.values():
            cpt += 1
            val_temp = val[1:]
            val = val_temp[::-1]
            dict_temp[str(cpt)] = val

        return dict_temp

    def verif_recherche_solution(self, dict_temp, dict_old):
        """Verif recherche solution de saut sans retourner en arrière"""
        dict_saut = {}
        cpt = 0

        if len(dict_temp) > 0 and len(dict_old) > 0:
            for val in dict_temp.values():
                for val2 in dict_old.values():
                    val2 = val2[1:]
                    if (
                        val[0] in val2
                        and val[1] not in val2
                    ):
                        cpt += 1
                        dict_saut[str(cpt)] = val
                    else:
                        pass
        else:
            pass

        return dict_saut

    def calcul_nb_saut_dict(self, dict_saut):
        """Calcul du nombre de saut"""
        cpt = 0
        lst_temp = []

        for val in dict_saut.values():
            old_x = val[0][0]
            cpt = 0
            for element in val:
                new_x = element[0]
                if new_x - old_x == 120 or new_x - old_x == -120:
                    cpt += 1
                else:
                    pass
                old_x = new_x
            lst_temp.append(cpt)

        return lst_temp

    def nettoyage_dict_saut(self, dict_saut, lst_nb_saut):
        """Nettoyage du dictionnaire des sauts"""
        dict_temp = dict_saut
        cpt = 0

        # Analyse de la liste pour avoir le chiffre le plus élevé
        min_val = min(lst_nb_saut)
        max_val = max(lst_nb_saut)

        if max_val - min_val > 0:
            for val in lst_nb_saut:
                cpt += 1
                if val <= min_val:
                    self.cpt += 1
                    element = dict_saut[str(cpt)]
                    self.dict_other[str(self.cpt)] = element
                    del dict_temp[str(cpt)]
                else:
                    pass
        else:
            pass

        return dict_temp

    def fusion_dict(self, dict1, dict2):
        """Fusion de 2 dictionnaires: saut1 et saut2"""
        # dict1 : self.dict_saut , dict2 : dict_saut
        lst_temp = []
        dict_temp = {}
        cpt = 0

        if len(dict2) > 0:
            for val in dict1.values():
                for element in val:
                    for val2 in dict2.values():
                        if element == val2[0] and val2[1] not in val:
                            index_el = val.index(element)
                            lst_temp.append((val[:index_el] + val2))
                        else:
                            lst_temp.append(val)

        else:
            dict_temp = dict1

        cpt = 0
        if len(lst_temp) > 0:
            lst_temp = self.clean_lst(lst_temp)
            for val in lst_temp:
                cpt += 1
                dict_temp[str(cpt)] = val
        else:
            pass

        return dict_temp

    def clean_lst(self, lst_1):
        """Suppression des doublons"""
        lst_temp = []

        for val in lst_1:
            if val not in lst_temp:
                lst_temp.append(val)
            else:
                pass

        return lst_temp

    def lst_for_research(self, dict_saut, lst_saut):
        """Création de la liste des possibilités de depl
        pour faire les nouvelles recherches de saut"""
        lst_temp = []
        lst_temp2 = []

        if len(lst_saut) > 0:
            for element in lst_saut:
                for val in dict_saut.values():
                    if element in val:
                        index_saut1 = val.index(element)
                        lst_temp.append(val[index_saut1:])
                    else:
                        pass

            # Modif de la liste de liste pour en faire une liste simple
            if len(lst_temp) > 0:
                for val in lst_temp:
                    for element in val:
                        lst_temp2.append(element)
            else:
                pass

            lst_temp2 = self.clean_lst(lst_temp2)
        else:
            pass

        return lst_temp2

    def find_solution_depl(self):
        """Appel de la methode saut_depl_possible pour recupérer
        les possibilités de depl ou saut"""

        lst_saut = []
        lst_saut1 = []
        lst_temp = []
        old_dict_saut = {}

        lst_saut.append(self.pos_dame)

        if len(self.pos_dame) > 0:
            cpt = 0
            dict_saut = {}
            (
                dict_temp,
                lst_temp,
                depl_temp,
                pn_sup,
                pb_sup,
            ) = self.depl.start_all_research(self.pos_dame)

            if len(dict_temp) > 0:
                lst_saut1.extend(lst_temp)

                for val in dict_temp.values():
                    cpt += 1
                    dict_saut[str(cpt)] = val

                if len(pn_sup) > 0:
                    self.lst_pn_sup.extend(pn_sup)
                if len(pb_sup) > 0:
                    self.lst_pb_sup.extend(pb_sup)
                else:
                    pass
            else:
                pass

            if len(depl_temp) > 0:
                self.lst_depl.extend(depl_temp)

            if len(dict_saut) > 0:
                self.dict_saut = dict_saut
                lst_saut = self.lst_for_research(dict_saut, lst_saut1)

                self.lst_pn_sup = self.clean_lst(self.lst_pn_sup)
                self.lst_pb_sup = self.clean_lst(self.lst_pb_sup)

            else:
                lst_saut = []
        else:
            lst_saut = []

        while len(lst_saut) > 0:
            cpt = 0
            dict_saut = {}
            lst_saut1 = []
            old_dict_saut = self.dict_saut

            for pos in lst_saut:
                (
                    dict_temp,
                    lst_temp,
                    _,
                    pn_sup,
                    pb_sup,
                ) = self.depl.start_all_research(pos)

                dict_temp = self.verif_recherche_solution(
                    dict_temp,
                    old_dict_saut,
                )

                if len(dict_temp) > 0:
                    lst_saut1.extend(lst_temp)

                    for val in dict_temp.values():
                        cpt += 1
                        dict_saut[str(cpt)] = val

                    if len(pn_sup) > 0:
                        self.lst_pn_sup.extend(pn_sup)
                    if len(pb_sup) > 0:
                        self.lst_pb_sup.extend(pb_sup)
                    else:
                        pass
                else:
                    pass

            if len(dict_saut) > 0:
                self.dict_saut = self.fusion_dict(self.dict_saut, dict_saut)

                lst_nb_saut = self.calcul_nb_saut_dict(self.dict_saut)

                self.dict_saut = self.nettoyage_dict_saut(
                    self.dict_saut,
                    lst_nb_saut,
                )
                lst_saut = self.lst_for_research(dict_saut, lst_saut1)

                self.lst_pn_sup = self.clean_lst(self.lst_pn_sup)
                self.lst_pb_sup = self.clean_lst(self.lst_pb_sup)

            else:
                lst_saut = []
