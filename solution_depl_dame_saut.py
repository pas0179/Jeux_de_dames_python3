"""
Class pour gerer les sauts possibles d'une dame 
noir ou blanc

"""

from solution_depl_dame_base import SolDeplDames

# from fonctions import convert_dict_lst


class SautDames:
    def __init__(self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb):
        self.pos_dame = pos_dame
        self.color_dame = color_dame
        self.lst_case_vide = lst_case_vide
        self.lst_pos_pn = lst_pos_pn
        self.lst_pos_pb = lst_pos_pb

        self.dict_saut = {}
        self.new_pos = {}

        self.lst_depl = []

        self.lst_pn_sup = []
        self.lst_pb_sup = []

        self.cpt = 0

        self.sol = "Solution_"

        """ Initialisation de la class SolDeplDames """
        self.depl = SolDeplDames(
            self.color_dame,
            self.lst_case_vide,
            self.lst_pos_pn,
            self.lst_pos_pb,
        )

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
        new_pos_saut = []

        """ Trouver saut et position pour nouvelle liste """
        if len(lst_depl) > 0 and (len(lst_pn_sup) > 0 or len(lst_pb_sup) > 0):
            if len(lst_pn_sup) > 0:
                new_pos_saut = lst_pn_sup[0]
            elif len(lst_pb_sup) > 0:
                new_pos_saut = lst_pb_sup[0]
            else:
                pass

            """Touver l'index de la position du pion sauté dans la liste
            des deplacements"""
            index_pos_saut = lst_depl.index(new_pos_saut)

            """ Création de la nouvelle liste """
            lst_temp = lst_depl[index_pos_saut + 1 :]

            """ Suppression des pos de sauts dans la liste des depl """
            lst_temp2 = [
                val
                for val in lst_temp
                if val not in lst_pn_sup or val not in lst_pb_sup
            ]

            lst_temp = lst_temp2

        else:
            pass

        return lst_temp

    """ Nettoyage de la liste des deplacements,
    Suppression des positions des pions sautés """

    def nettoyage_depl(self, depl, pn_sup, pb_sup):
        lst_depl = []
        for val in depl:
            if val not in pn_sup and val not in pb_sup:
                lst_depl.append(val)
            else:
                pass

        return lst_depl

    """
    Methode:
    - Création dictionnaire si saut 
    - Création liste si deplacement simple en diagonale
    """

    def saut_depl(self, position):
        dict_saut = {}
        lst_depl = []
        new_pos = {}

        lst_pn_sup = []
        lst_pb_sup = []

        deplbg, pn_supbg, pb_supbg = self.depl.solution_depl_dame_b_gauche(position)
        deplbd, pn_supbd, pb_supbd = self.depl.solution_depl_dame_b_droit(position)
        deplhg, pn_suphg, pb_suphg = self.depl.solution_depl_dame_h_gauche(position)
        deplhd, pn_suphd, pb_suphd = self.depl.solution_depl_dame_h_droit(position)

        if len(deplbg) > 0:
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
                dict_saut[self.sol + str(self.cpt)] = [self.pos_dame, *depl]
                new_pos[self.sol + str(self.cpt)] = lst_new_pos

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_supbg)
                else:
                    lst_pn_sup.extend(pn_supbg)
            else:
                lst_depl.extend(depl)
        else:
            pass

        if len(deplbd) > 0:
            """Test si saut avec methode lst_nouveau_depl"""
            lst_new_pos = self.find_saut(deplbd, pn_supbd, pb_supbd)
            depl = self.nettoyage_depl(deplbd, pn_supbd, pb_supbd)

            if len(lst_new_pos) > 0:
                """Saut possible"""
                self.cpt += 1

                dict_saut[self.sol + str(self.cpt)] = [self.pos_dame, *depl]
                new_pos[self.sol + str(self.cpt)] = lst_new_pos

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_supbd)
                else:
                    lst_pn_sup.extend(pn_supbd)
            else:
                lst_depl.extend(depl)
        else:
            pass

        if len(deplhg) > 0:
            """Test si saut avec methode lst_nouveau_depl"""
            lst_new_pos = self.find_saut(deplhg, pn_suphg, pb_suphg)
            depl = self.nettoyage_depl(deplhg, pn_suphg, pb_suphg)

            if len(lst_new_pos) > 0:
                """Saut possible"""
                self.cpt += 1

                dict_saut[self.sol + str(self.cpt)] = [self.pos_dame, *depl]
                new_pos[self.sol + str(self.cpt)] = lst_new_pos

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_suphg)
                else:
                    lst_pn_sup.extend(pn_suphg)
            else:
                lst_depl.extend(depl)
        else:
            pass

        if len(deplhd) > 0:
            """Test si saut avec methode lst_nouveau_depl"""
            lst_new_pos = self.find_saut(deplhd, pn_suphd, pb_suphd)
            depl = self.nettoyage_depl(deplhd, pn_suphd, pb_suphd)

            if len(lst_new_pos) > 0:
                """Saut possible"""
                self.cpt += 1

                dict_saut[self.sol + str(self.cpt)] = [self.pos_dame, *depl]
                new_pos[self.sol + str(self.cpt)] = lst_new_pos

                if self.color_dame == "noir":
                    lst_pb_sup.extend(pb_suphd)
                else:
                    lst_pn_sup.extend(pn_suphd)
            else:
                lst_depl.extend(depl)
        else:
            pass

        print(f"dict_saut : {dict_saut}")
        print(f"new_pos : {new_pos}")
        print(f"lst_depl : {lst_depl}")

        return lst_depl, lst_pn_sup, lst_pb_sup

    """
    Methode pour calculer si d'autre saut possible pour une dame
    """
    def find_autre_saut(self):

        position = self.pos_dame

        lst_depl, lst_pn_sup, lst_pb_sup = self.saut_depl(position)

        if len(lst_depl) > 0:
            self.lst_depl = lst_depl
        else:
            pass

        return self.lst_depl, lst_pn_sup, lst_pb_sup

