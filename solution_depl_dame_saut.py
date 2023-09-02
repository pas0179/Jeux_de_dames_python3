"""
Class pour gerer les sauts possibles d'une dame 
noir ou blanc

"""

from solution_depl_dame_base import SolDeplDames

from fonctions import convert_dict_lst


class SautDames:
    def __init__(self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb):
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

    """ Methode:
    - Mise a jour des compteur et clé du dictionnaire """

    def maj_dict_saut(self, dict_saut):
        compteur = 0
        dict_temp = {}

        for val in dict_saut.values():
            compteur += 1
            dict_temp[self.sol + str(compteur)] = val

        return dict_temp

    """ Nettoyage de la liste des deplacements,
    Suppression des positions des pions sautés """

    def nettoyage_depl(self, depl, pn_sup, pb_sup):
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

    """
    Methode:
    - Si saut possible -> création d'une liste pour itérer
    sur les diagonales adjacentes et trouver si autre saut
    possible.
    de 1er case après saut -> fin de la liste des deplacements
    possibles
    """

    def find_saut(self, lst_depl, lst_pn_sup, lst_pb_sup):
        lst_temp = []
        new_pos_saut = ()

        """ Trouver saut et position pour nouvelle liste """
        if len(lst_pn_sup) > 0:
            new_pos_saut = lst_pn_sup[0]
        elif len(lst_pb_sup) > 0:
            new_pos_saut = lst_pb_sup[0]
        else:
            pass

        if new_pos_saut != ():
            """Touver l'index de la position du pion sauté dans la liste
            des deplacements"""
            index_pos_saut = lst_depl.index(new_pos_saut)

            """ Création de la nouvelle liste """
            lst_temp = lst_depl[index_pos_saut + 1 :]

            """ Suppression des pos de sauts dans la liste des depl """
            lst_temp = self.nettoyage_depl(lst_temp, lst_pn_sup, lst_pb_sup)

        else:
            pass

        return lst_temp

    def fusion_dict(self, dict_1, dict_2):
        # Dict1 : self.dict_saut , dict2 : dict_saut
        # dict_fusion = {}
        dict_temp = {}

        lst_dict1, lst_dict2 = [], []

        for val in dict_1.values():
            lst_dict1.extend(val)

        for val in dict_2.values():
            lst_dict2.extend(val)

        print(lst_dict1)
        print(lst_dict2)


        return dict_temp

    """
    Methode:
    - Création dictionnaire si saut 
    - Création liste si deplacement simple en diagonale
    """

    def saut_depl_possible(self, position):
        dict_saut = {}
        lst_depl = []

        lst_new_pos_saut = []

        lst_pn_sup = []
        lst_pb_sup = []

        deplbg, pn_supbg, pb_supbg = self.depl.solution_depl_dame_b_gauche(position)
        deplbd, pn_supbd, pb_supbd = self.depl.solution_depl_dame_b_droit(position)
        deplhg, pn_suphg, pb_suphg = self.depl.solution_depl_dame_h_gauche(position)
        deplhd, pn_suphd, pb_suphd = self.depl.solution_depl_dame_h_droit(position)

        if len(deplbg) > 0 and deplbg not in self.dict_saut.values():
            """
            Test si saut avec methode lst_nouveau_depl
            - retourne une liste des deplacements nettoyés
            - retourne une liste après 1er saut.
            """
            lst_new_pos = self.find_saut(deplbg, pn_supbg, pb_supbg)
            depl = self.nettoyage_depl(deplbg, pn_supbg, pb_supbg)

            if len(lst_new_pos) > 0:
                """Saut possible"""
                self.cpt += 1
                dict_saut[self.sol + str(self.cpt)] = [position, *depl]
                # new_pos[self.sol + str(self.cpt)] = lst_new_pos

                lst_new_pos_saut.extend(lst_new_pos)

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_supbg)
                else:
                    lst_pn_sup.extend(pn_supbg)

                """ Après un deplbg ---> deplbd et deplhg si saut dans deplbg """

            else:
                lst_depl.extend(depl)

        if len(deplbd) > 0 and deplbd not in self.dict_saut.values():
            """Test si saut avec methode lst_nouveau_depl"""
            lst_new_pos = self.find_saut(deplbd, pn_supbd, pb_supbd)
            depl = self.nettoyage_depl(deplbd, pn_supbd, pb_supbd)

            if len(lst_new_pos) > 0:
                """Saut possible"""
                self.cpt += 1

                dict_saut[self.sol + str(self.cpt)] = [position, *depl]
                # new_pos[self.sol + str(self.cpt)] = lst_new_pos

                lst_new_pos_saut.extend(lst_new_pos)

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_supbd)
                else:
                    lst_pn_sup.extend(pn_supbd)
            else:
                lst_depl.extend(depl)

        if len(deplhg) > 0 and deplhg not in self.dict_saut.values():
            """Test si saut avec methode lst_nouveau_depl"""
            lst_new_pos = self.find_saut(deplhg, pn_suphg, pb_suphg)
            depl = self.nettoyage_depl(deplhg, pn_suphg, pb_suphg)

            if len(lst_new_pos) > 0:
                """Saut possible"""
                self.cpt += 1

                dict_saut[self.sol + str(self.cpt)] = [position, *depl]
                # new_pos[self.sol + str(self.cpt)] = lst_new_pos

                lst_new_pos_saut.extend(lst_new_pos)

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_suphg)
                else:
                    lst_pn_sup.extend(pn_suphg)
            else:
                lst_depl.extend(depl)

        if len(deplhd) > 0 and deplhd not in self.dict_saut.values():
            """Test si saut avec methode lst_nouveau_depl"""
            lst_new_pos = self.find_saut(deplhd, pn_suphd, pb_suphd)
            depl = self.nettoyage_depl(deplhd, pn_suphd, pb_suphd)

            if len(lst_new_pos) > 0:
                """Saut possible"""
                self.cpt += 1

                dict_saut[self.sol + str(self.cpt)] = [position, *depl]
                # new_pos[self.sol + str(self.cpt)] = lst_new_pos

                lst_new_pos_saut.extend(lst_new_pos)

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_suphd)
                else:
                    lst_pn_sup.extend(pn_suphd)
            else:
                lst_depl.extend(depl)
        else:
            pass

        return dict_saut, lst_new_pos_saut, lst_depl, lst_pn_sup, lst_pb_sup

    """
    Methode pour calculer si d'autre saut possible pour une dame
    """

    def find_solution_saut_depl(self):
        """Appel de la methode saut_depl_possible pour recupérer
        les possibilités saut ou deplacements"""

        lst_pn_sup = []
        lst_pb_sup = []

        position = self.pos_dame

        dict_saut, new_pos, lst_depl, pn_sup, pb_sup = self.saut_depl_possible(position)

        if len(lst_depl) > 0:
            self.lst_depl = lst_depl

        if len(dict_saut) > 0 and len(new_pos) > 0:
            self.dict_saut = dict_saut
            self.new_pos = new_pos

            lst_pn_sup.extend(pn_sup)
            lst_pb_sup.extend(pb_sup)

        else:
            pass

        """ Après la 1er diagonale, la dame peut changer de diagonale
        que si il y a eu un saut possible sur la 1er diagonale et 
        que sur la 2eme il y a aussi un autre saut disponible """


        if len(new_pos) > 0:
            for pos in new_pos:
                (
                    dict_saut_temp,
                    pos_temp,
                    _,
                    pn_temp,
                    pb_temp,
                ) = self.saut_depl_possible(pos)

                if len(dict_saut_temp) > 0:
                    self.dict_saut2.update(dict_saut_temp)
                    self.new_pos2.extend(pos_temp)

                    if len(pn_temp) > 0:
                        lst_pn_sup.extend(pn_temp)
                    elif len(pb_temp) > 0:
                        lst_pb_sup.extend(pb_temp)
                    else:
                        pass
                else:
                    pass
        else:
            pass

        if len(self.dict_saut2) > 0:
            """Mise a jour des clés de dict_saut2"""
            self.dict_saut2 = self.maj_dict_saut(self.dict_saut2)

            self.dict_saut = self.fusion_dict(self.dict_saut, self.dict_saut2)
            print(f"self.dict_saut : {self.dict_saut}")
            self.new_pos = self.new_pos2

        else:
            pass

        self.lst_pn_sup = lst_pn_sup
        self.lst_pb_sup = lst_pb_sup

        print(f"dict_saut : {self.dict_saut}")
        # print(f"new_pos : {self.new_pos}")

        print(f"self.dict_saut2 : {self.dict_saut2}")
        # print(f"self.dict_saut : {self.dict_saut}")
        # print(f"self.new_pos2 : {self.new_pos2}")
        # print(f"self.lst_depl : {self.lst_depl}")
