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

        """ Initialisation de la class SolDeplDames """
        self.depl = SolDeplDames(
            self.color_dame,
            self.lst_case_vide,
            self.lst_pos_pn,
            self.lst_pos_pb,
        )

        self.find_solution_saut_depl()

    def maj_dict_saut(self, dict_saut):
        """Mise a jour des compteur et clé du dictionnaire"""
        compteur = 0
        dict_temp = {}

        for val in dict_saut.values():
            compteur += 1
            dict_temp[self.sol + str(compteur)] = val

        return dict_temp

    def nettoyage_depl(self, depl, pn_sup, pb_sup):
        """Nettoyage de la liste des deplacements et suppression
        des positions des pions sautés"""
        if len(pn_sup) > 0:
            for val in pn_sup:
                if val in depl:
                    depl.remove(val)
                else:
                    pass
        if len(pb_sup) > 0:
            for val in pb_sup:
                if val in depl:
                    depl.remove(val)
                else:
                    pass

        return depl

    def find_saut(self, lst_depl, lst_pn_sup, lst_pb_sup):
        """
        Methode:
        - Si saut possible -> création d'une liste pour itérer
        sur les diagonales adjacentes et trouver si autre saut
        possible.
        de 1er case après saut -> fin de la liste des deplacements
        possibles"""

        lst_temp = []
        new_pos_saut = ()

        if len(lst_pn_sup) > 0:
            new_pos_saut = lst_pn_sup[0]
        elif len(lst_pb_sup) > 0:
            new_pos_saut = lst_pb_sup[0]
        else:
            pass

        if new_pos_saut != ():
            index_pos_saut = lst_depl.index(new_pos_saut)

            lst_temp = lst_depl[index_pos_saut + 1:]

            lst_temp = self.nettoyage_depl(lst_temp, lst_pn_sup, lst_pb_sup)

        else:
            pass

        return lst_temp

    def find_sol_saut_b_gauche(self, position):
        """Recherche si saut possible de diagonale bas gauche"""
        dict_saut = {}
        lst_new_pos = []
        lst_depl = []
        lst_pn_sup = []
        lst_pb_sup = []

        depl, pn_sup, pb_sup = self.depl.solution_depl_dame_b_gauche(position)

        if len(depl) > 0:
            new_pos = self.find_saut(depl, pn_sup, pb_sup)
            depl_temp = self.nettoyage_depl(depl, pn_sup, pb_sup)

            if len(new_pos) > 0:
                self.cpt += 1
                dict_saut[self.sol + str(self.cpt)] = [position, *depl_temp]
                lst_new_pos.extend(new_pos)

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_sup)
                else:
                    lst_pn_sup.extend(pn_sup)
            else:
                lst_depl = depl
        else:
            pass

        return dict_saut, lst_new_pos, lst_depl, lst_pn_sup, lst_pb_sup

    def find_sol_saut_b_droit(self, position):
        """Recherche si saut possible de diagonale bas droite"""
        dict_saut = {}
        lst_new_pos = []
        lst_depl = []
        lst_pn_sup = []
        lst_pb_sup = []

        depl, pn_sup, pb_sup = self.depl.solution_depl_dame_b_droit(position)

        if len(depl) > 0:
            new_pos = self.find_saut(depl, pn_sup, pb_sup)
            depl_temp = self.nettoyage_depl(depl, pn_sup, pb_sup)

            if len(new_pos) > 0:
                self.cpt += 1
                dict_saut[self.sol + str(self.cpt)] = [position, *depl_temp]
                lst_new_pos.extend(new_pos)

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_sup)
                else:
                    lst_pn_sup.extend(pn_sup)
            else:
                lst_depl = depl
        else:
            pass

        return dict_saut, lst_new_pos, lst_depl, lst_pn_sup, lst_pb_sup

    def find_sol_saut_h_gauche(self, position):
        """Recherche si saut possible de diagonale haut gauche"""
        dict_saut = {}
        lst_new_pos = []
        lst_depl = []
        lst_pn_sup = []
        lst_pb_sup = []

        depl, pn_sup, pb_sup = self.depl.solution_depl_dame_h_gauche(position)

        if len(depl) > 0:
            new_pos = self.find_saut(depl, pn_sup, pb_sup)
            depl_temp = self.nettoyage_depl(depl, pn_sup, pb_sup)

            if len(new_pos) > 0:
                self.cpt += 1
                dict_saut[self.sol + str(self.cpt)] = [position, *depl_temp]
                lst_new_pos.extend(new_pos)

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_sup)
                else:
                    lst_pn_sup.extend(pn_sup)
            else:
                lst_depl = depl
        else:
            pass

        return dict_saut, lst_new_pos, lst_depl, lst_pn_sup, lst_pb_sup

    def find_sol_saut_h_droit(self, position):
        """Recherche si saut possible de diagonale haut droite"""
        dict_saut = {}
        lst_new_pos = []
        lst_depl = []
        lst_pn_sup = []
        lst_pb_sup = []

        depl, pn_sup, pb_sup = self.depl.solution_depl_dame_h_droit(position)

        if len(depl) > 0:
            new_pos = self.find_saut(depl, pn_sup, pb_sup)
            depl_temp = self.nettoyage_depl(depl, pn_sup, pb_sup)

            if len(new_pos) > 0:
                self.cpt += 1
                dict_saut[self.sol + str(self.cpt)] = [position, *depl_temp]
                lst_new_pos.extend(new_pos)

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_sup)
                else:
                    lst_pn_sup.extend(pn_sup)
            else:
                lst_depl = depl
        else:
            pass

        return dict_saut, lst_new_pos, lst_depl, lst_pn_sup, lst_pb_sup

    def fusion_dict_saut(self, dict_saut, dict_saut2):
        """Fusion de 2 dictionnaires en un seul dictionnaires"""
        cpt = 0
        lg_dict = len(dict_saut)

        for val in dict_saut2.values():
            cpt += 1
            dict_saut[self.sol + str(cpt+lg_dict)] = val

        return dict_saut

    def fusion_lst(self, lst_new_pos, lst_new_pos2):
        """Fusion de 2 listes de nouvelles positions"""
        lst_new_pos.extend(lst_new_pos2)
        return lst_new_pos

    def find_sol_saut_bas(self, position):
        """Appel des 2 methodes diagonales bas gauche et droite
        pour recherche des saut possibles"""
        dict_saut = {}
        lst_new_pos = []
        lst_depl = []
        lst_pn_sup = []
        lst_pb_sup = []

        (
            dict_saut,
            lst_new_pos,
            lst_depl,
            lst_pn_sup,
            lst_pb_sup,
        ) = self.find_sol_saut_b_gauche(
            position,
        )

        (
            dict_saut2,
            lst_new_pos2,
            lst_depl2,
            lst_pn_sup2,
            lst_pb_sup2,
        ) = self.find_sol_saut_b_droit(
            position,
        )

        dict_saut = self.fusion_dict_saut(dict_saut, dict_saut2)
        lst_new_pos = self.fusion_lst(
            lst_new_pos, lst_new_pos2,
        )
        lst_depl = self.fusion_lst(lst_depl, lst_depl2)
        lst_pn_sup = self.fusion_lst(
            lst_pn_sup, lst_pn_sup2
        )
        lst_pb_sup = self.fusion_lst(
            lst_pb_sup, lst_pb_sup2,
        )

        return dict_saut, lst_new_pos, lst_depl, lst_pn_sup, lst_pb_sup

    def find_sol_saut_haut(self, position):
        """Appel des 2 methodes diagonales haut gauche et droite
        pour recherche des saut possibles"""
        dict_saut = {}
        lst_new_pos = []
        lst_depl = []
        lst_pn_sup = []
        lst_pb_sup = []

        (
            dict_saut,
            lst_new_pos,
            lst_depl,
            lst_pn_sup,
            lst_pb_sup,
        ) = self.find_sol_saut_h_gauche(
            position,
        )

        (
            dict_saut2,
            lst_new_pos2,
            lst_depl2,
            lst_pn_sup2,
            lst_pb_sup2,
        ) = self.find_sol_saut_h_droit(
            position,
        )

        dict_saut = self.fusion_dict_saut(dict_saut, dict_saut2)
        lst_new_pos = self.fusion_lst(
            lst_new_pos, lst_new_pos2,
        )
        lst_depl = self.fusion_lst(lst_depl, lst_depl2)
        lst_pn_sup = self.fusion_lst(
            lst_pn_sup, lst_pn_sup2
        )
        lst_pb_sup = self.fusion_lst(
            lst_pb_sup, lst_pb_sup2,
        )

        return dict_saut, lst_new_pos, lst_depl, lst_pn_sup, lst_pb_sup

    def find_depl_saut(self, position):
        """Methode pour trouver les sauts possibles
        sur les 4 diagonales"""

        dict_saut = {}
        lst_new_pos = []
        lst_depl = []
        lst_pn_sup = []
        lst_pb_sup = []

        (
            dict_saut,
            lst_new_pos,
            lst_depl,
            lst_pn_sup,
            lst_pb_sup,
        ) = self.find_sol_saut_bas(position)

        (
            dict_saut2,
            lst_new_pos2,
            lst_depl2,
            lst_pn_sup2,
            lst_pb_sup2,
        ) = self.find_sol_saut_haut(position)

        dict_saut = self.fusion_dict_saut(dict_saut, dict_saut2)
        lst_new_pos = self.fusion_lst(
            lst_new_pos, lst_new_pos2,
        )
        lst_depl = self.fusion_lst(lst_depl, lst_depl2)
        lst_pn_sup = self.fusion_lst(
            lst_pn_sup, lst_pn_sup2,
        )
        lst_pb_sup = self.fusion_lst(
            lst_pb_sup, lst_pb_sup2,
        )

        return dict_saut, lst_new_pos, lst_depl, lst_pn_sup, lst_pb_sup

    # def saut_depl_possible(self, position):
    #     """Methode:
    #     - Création dictionnaire si saut
    #     - Création liste si deplacement simple en diagonale"""
    #
    #     dict_saut = {}
    #     lst_depl = []
    #
    #     lst_new_pos_saut = []
    #
    #     lst_pn_sup = []
    #     lst_pb_sup = []
    #
    #     (
    #         deplbg,
    #         pn_supbg,
    #         pb_supbg,
    #     ) = self.depl.solution_depl_dame_b_gauche(position)
    #
    #     (
    #         deplbd,
    #         pn_supbd,
    #         pb_supbd,
    #     ) = self.depl.solution_depl_dame_b_droit(position)
    #
    #     (
    #         deplhg,
    #         pn_suphg,
    #         pb_suphg,
    #     ) = self.depl.solution_depl_dame_h_gauche(position)
    #
    #     (
    #         deplhd,
    #         pn_suphd,
    #         pb_suphd,
    #     ) = self.depl.solution_depl_dame_h_droit(position)
    #
    #     if len(deplbg) > 0:
    #         lst_new_pos = self.find_saut(deplbg, pn_supbg, pb_supbg)
    #         depl = self.nettoyage_depl(deplbg, pn_supbg, pb_supbg)
    #
    #         if len(lst_new_pos) > 0:
    #             self.cpt += 1
    #             dict_saut[self.sol + str(self.cpt)] = [position, *depl]
    #             lst_new_pos_saut.extend(lst_new_pos)
    #
    #             if self.color_dame == "noir":
    #                 lst_pb_sup.extend(pb_supbg)
    #             else:
    #                 lst_pn_sup.extend(pn_supbg)
    #         else:
    #             lst_depl.extend(depl)
    #
    #     if len(deplbd) > 0:
    #         lst_new_pos = self.find_saut(deplbd, pn_supbd, pb_supbd)
    #         depl = self.nettoyage_depl(deplbd, pn_supbd, pb_supbd)
    #
    #         if len(lst_new_pos) > 0:
    #             self.cpt += 1
    #             dict_saut[self.sol + str(self.cpt)] = [position, *depl]
    #             lst_new_pos_saut.extend(lst_new_pos)
    #
    #             if self.color_dame == "noir":
    #                 lst_pb_sup.extend(pb_supbd)
    #             else:
    #                 lst_pn_sup.extend(pn_supbd)
    #         else:
    #             lst_depl.extend(depl)
    #
    #     if len(deplhg) > 0:
    #         lst_new_pos = self.find_saut(deplhg, pn_suphg, pb_suphg)
    #         depl = self.nettoyage_depl(deplhg, pn_suphg, pb_suphg)
    #
    #         if len(lst_new_pos) > 0:
    #             self.cpt += 1
    #             dict_saut[self.sol + str(self.cpt)] = [position, *depl]
    #             lst_new_pos_saut.extend(lst_new_pos)
    #
    #             if self.color_dame == "noir":
    #                 lst_pb_sup.extend(pb_suphg)
    #             else:
    #                 lst_pn_sup.extend(pn_suphg)
    #         else:
    #             lst_depl.extend(depl)
    #
    #     if len(deplhd) > 0:
    #         lst_new_pos = self.find_saut(deplhd, pn_suphd, pb_suphd)
    #         depl = self.nettoyage_depl(deplhd, pn_suphd, pb_suphd)
    #
    #         if len(lst_new_pos) > 0:
    #             self.cpt += 1
    #             dict_saut[self.sol + str(self.cpt)] = [position, *depl]
    #             lst_new_pos_saut.extend(lst_new_pos)
    #
    #             if self.color_dame == "noir":
    #                 lst_pb_sup.extend(pb_suphd)
    #             else:
    #                 lst_pn_sup.extend(pn_suphd)
    #         else:
    #             lst_depl.extend(depl)
    #
    #     return dict_saut, lst_new_pos_saut, lst_depl, lst_pn_sup, lst_pb_sup

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

        if len(dict2) > 0:
            for val in dict1.values():
                for element in val:
                    for val2 in dict2.values():
                        if element == val2[0]:
                            index_el = val.index(element)
                            lst_temp.append((val[:index_el] + val2))
                        else:
                            pass
        else:
            pass

        # Création d'un nouveau dictionnaire
        dict_temp = {}
        cpt = 0

        for val in lst_temp:
            cpt += 1
            dict_temp[self.sol + str(cpt)] = val

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

    def find_solution_saut_depl(self):
        """Appel de la methode saut_depl_possible pour recupérer
        les possibilités saut ou deplacements"""

        dict_temp = {}
        dict_reverse = {}
        dict_test = {}
        new_pos_temp = []

        position = self.pos_dame

        dict_saut, new_pos, lst_depl, pn_sup, pb_sup = self.find_depl_saut(
            position,
        )

        dict_reverse = self.reverse_dict(dict_saut)
        print(f"dict_reverse : {dict_reverse}")
        dict_test = self.test_dict(dict_saut)
        print(f"dict_test : {dict_test}")

        if len(dict_saut) > 0:
            self.dict_saut = dict_saut
            if len(pn_sup) > 0:
                self.lst_pn_sup.extend(pn_sup)
            else:
                self.lst_pb_sup.extend(pb_sup)
            self.new_pos = new_pos
        else:
            self.lst_depl = lst_depl
            print(f"self.lst_depl : {self.lst_depl}")

        print(f"self.dict_saut : {self.dict_saut}")

        if len(self.new_pos) > 0:
            cpt = 0
            for pos in self.new_pos:
                (
                    dict_saut2,
                    new_pos2,
                    _,
                    pn_sup2,
                    pb_sup2,
                ) = self.find_depl_saut(
                    pos,
                )

                dict_saut2 = self.verif_recherche_solution(
                    dict_saut2,
                    dict_test,
                    dict_reverse,
                )

                if len(dict_saut2) > 0:
                    cpt += 1
                    for val in dict_saut2.values():
                        dict_temp[self.sol + str(cpt)] = val

                    if len(pn_sup2) > 0:
                        self.lst_pn_sup.extend(pn_sup2)
                    else:
                        self.lst_pb_sup.extend(pb_sup2)
                    new_pos_temp.extend(new_pos2)

                else:
                    pass

            self.new_pos = self.clean_lst(new_pos_temp)
        else:
            pass

        print(f"dict_temp : {dict_temp}")
        self.dict_saut2 = self.fusion_dict(self.dict_saut, dict_temp)

        print(f"self.dict_saut2 : {self.dict_saut2}")
        print(f"self.new_pos : {self.new_pos}")
