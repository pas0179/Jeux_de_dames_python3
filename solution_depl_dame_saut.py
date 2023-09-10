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

        self.find_solution_saut_depl()

    def reverse_dict(self, dict_saut):
        """Création d'un dictionnaire inversé depuis dict_saut"""
        dict_temp = {}

        for key, val in dict_saut.items():
            val = val[1:]
            dict_temp[key] = val[::-1]

        return dict_temp

    def test_dict(self, dict_saut):
        """Création d'un dictionnaire sans la pos de départ depuis dict_saut"""
        dict_test = {}
        cpt = 0

        for val in dict_saut.values():
            cpt += 1
            dict_test[self.sol + str(cpt)] = val[1:]

        return dict_test

    def verif_recherche_solution(self, dict_saut, dict_t, dict_r):
        """Verif recherche solution de saut sans retourner en arrière"""
        dict_temp = {}

        if len(dict_saut) > 0:
            dict_temp = {
                key: val
                for key, val in dict_saut.items()
                if val not in dict_t.values() and val not in dict_r.values()
            }
        else:
            pass

        return dict_temp

    def fusion_dict(self, dict1, dict2):
        """Fusion de 2 dictionnaires: saut1 et saut2"""
        lst_temp = []
        lst_temp2 = []

        if len(dict2) > 0:
            for val in dict1.values():
                for element in val:
                    for val2 in dict2.values():
                        if element == val2[0]:
                            index_el = val.index(element)
                            lst_temp.append((val[:index_el] + val2))
                        else:
                            lst_temp2.append(val)

        else:
            dict_temp = dict1

        # Création d'un nouveau dictionnaire
        dict_temp = {}
        cpt = 0

        for val in lst_temp:
            cpt += 1
            dict_temp[self.sol + str(cpt)] = val
        for val in lst_temp2:
            dict_temp[str(cpt)] = val

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

    def find_lst_for_research(self, dict_saut, lst_saut):
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

    def find_solution_saut_depl(self):
        """Appel de la methode saut_depl_possible pour recupérer
        les possibilités saut ou deplacements"""

        lst_pn_sup = []
        lst_pb_sup = []
        lst_saut1 = []

        dict_reverse = {}
        dict_test = {}

        dict_saut1 = {}
        dict_saut = {}

        (
            dict_saut,
            lst_saut,
            depl,
            pn_sup,
            pb_sup,
        ) = self.depl.start_all_research(self.pos_dame)

        # print(f"dict_saut: {dict_saut}")

        if len(dict_saut) > 0:

            # Création de la liste des positions pour les nouvelles recherches
            lst_saut = self.find_lst_for_research(dict_saut, lst_saut)
            # print(f"lst_saut: {lst_saut}")

            if len(pn_sup) > 0:
                lst_pn_sup.extend(pn_sup)
            if len(pb_sup) > 0:
                lst_pb_sup.extend(pb_sup)
            else:
                pass

            dict_reverse = self.reverse_dict(dict_saut)
            dict_test = self.test_dict(dict_saut)
            cpt = 0

            for pos in lst_saut:
                (
                    dict_temp,
                    lst_temp,
                    _,
                    pn_sup1,
                    pb_sup1,
                ) = self.depl.start_all_research(pos)

                dict_temp = self.verif_recherche_solution(
                    dict_temp,
                    dict_test,
                    dict_reverse,
                )

                if len(dict_temp) > 0:

                    for val in dict_temp.values():
                        cpt += 1
                        dict_saut1[self.sol + str(cpt)] = val

                    if len(pn_sup1) > 0:
                        lst_pn_sup.extend(pn_sup1)
                    if len(pb_sup1) > 0:
                        lst_pb_sup.extend(pb_sup1)
                    else:
                        pass
                    if len(lst_temp) > 0:
                        lst_saut1.extend(lst_temp)
                    else:
                        pass

                else:
                    pass
            dict_saut = self.fusion_dict(dict_saut, dict_saut1)
            lst_saut = self.find_lst_for_research(dict_saut, lst_saut)

            lst_pn_sup = self.clean_lst(lst_pn_sup)
            lst_pb_sup = self.clean_lst(lst_pb_sup)
        else:
            pass

        # print(f"dict_saut1: {dict_saut1}")
        print(f"dict_saut: {dict_saut}")
        print(f"lst_saut: {lst_saut}")
        # print(f"lst_depl: {depl}")
        print(f"lst_pn_sup: {lst_pn_sup}")
        print(f"lst_pb_sup: {lst_pb_sup}")

        return depl, pn_sup, pb_sup
