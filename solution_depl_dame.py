""" 
Class pour trouver les solutions de deplacement avec ou sans saut
pour une dame sélectionnée 

Solutions pour une dame :

dame depl_h_d et depl_b_g : depl_b_d et depl_h_g
dame depl_h_g et depl_b_d : depl_b_g et depl_h_d

"""

from solution_depl_dame_base import SolDeplDames


class DeplDame:
    def __init__(self):
        self.dict_depl = {}

    def depl_dame_b_g(
        self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
    ):
        lst_temp = []
        lst_depl = []
        lst_dame_noir = []
        lst_dame_blanc = []
        lst_pn_sup = []
        lst_pb_sup = []

        depl_b_g, pn_sup, pb_sup = SolDeplDames().solution_depl_dame_b_gauche(
            pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
        )

        if len(depl_b_g) > 0 and (len(pn_sup) > 0 or len(pb_sup) > 0):
            lst_depl = depl_b_g
            lst_pb_sup = pb_sup
            lst_pn_sup = pn_sup

            """Touver le position apres le 1er saut et en faire
            une nouvelle liste"""
            if color_dame == "noir":
                pos_saut = pb_sup[0]

                """ Touver la position de pos_saut dans la liste de depl_b_g """
                index_pos_saut = depl_b_g.index(pos_saut)

                lst_temp = depl_b_g[index_pos_saut + 1 :]

                """ Supprimer les pos saut dans la liste depl_b_g """
                lst_dame_noir = [val for val in lst_temp if val not in pb_sup]

                print(f"Liste dame noir : {lst_dame_noir}")

                """ 
                Sur chaque pos dans la nouvelle liste :
                - vérifier si saut possible dans les diagonales
                - depl_b_d et depl_h_g

                """

                for pos in lst_dame_noir:
                    depl_b_d, _, pb_sup1 = SolDeplDames().solution_depl_dame_b_droit(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )
                    depl_h_g, _, pb_sup2 = SolDeplDames().solution_depl_dame_h_gauche(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )

                    if len(depl_b_d) > 0 and len(pb_sup1) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_b_d]
                        lst_pb_sup = [*lst_pb_sup, *pb_sup1]
                    elif len(depl_h_g) > 0 and len(pb_sup2) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_h_g]
                        lst_pb_sup = [*lst_pb_sup, *pb_sup2]
                    else:
                        pass

                print(f"liste depl : {lst_depl}")

            elif color_dame == "blanc":
                pos_saut = pn_sup[0]

                """ Touver la position de pos_saut dans la liste de depl_b_g """
                index_pos_saut = depl_b_g.index(pos_saut)

                lst_temp = depl_b_g[index_pos_saut + 1 :]

                """ Supprimer les pos saut dans la liste depl_b_g """
                lst_dame_blanc = [val for val in lst_temp if val not in pn_sup]

                print(f"liste dame blanc : {lst_dame_blanc}")

                """ 
                Sur chaque pos dans la nouvelle liste :
                - vérifier si saut possible dans les diagonales
                - depl_b_d et depl_h_g

                """

                for pos in lst_dame_blanc:
                    depl_b_d, pn_sup1, _ = SolDeplDames().solution_depl_dame_b_droit(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )
                    depl_h_g, pn_sup2, _ = SolDeplDames().solution_depl_dame_h_gauche(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )

                    if len(depl_b_d) > 0 and len(pn_sup1) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_b_d]
                        lst_pn_sup = [*lst_pn_sup, *pn_sup1]
                    elif len(depl_h_g) > 0 and len(pn_sup2) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_h_g]
                        lst_pn_sup = [*lst_pn_sup, *pn_sup2]
                    else:
                        pass

                print(f"liste depl : {lst_depl}")

            else:
                pass
        else:
            pass

        return lst_depl, lst_pn_sup, lst_pb_sup

    def depl_dame_b_d(
        self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
    ):
        lst_temp = []
        lst_depl = []
        lst_dame_noir = []
        lst_dame_blanc = []
        lst_pn_sup = []
        lst_pb_sup = []

        depl_b_d, pn_sup, pb_sup = SolDeplDames().solution_depl_dame_b_droit(
            pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
        )

        if len(depl_b_d) > 0 and (len(pn_sup) > 0 or len(pb_sup) > 0):
            lst_depl = depl_b_d
            lst_pb_sup = pb_sup
            lst_pn_sup = pn_sup

            """Touver le position apres le 1er saut et en faire
            une nouvelle liste"""
            if color_dame == "noir":
                pos_saut = pb_sup[0]

                """ Touver la position de pos_saut dans la liste de depl_b_d """
                index_pos_saut = depl_b_d.index(pos_saut)

                lst_temp = depl_b_d[index_pos_saut + 1 :]

                """ Supprimer les pos saut dans la liste depl_b_g """
                lst_dame_noir = [val for val in lst_temp if val not in pb_sup]

                print(f"Liste dame noir : {lst_dame_noir}")

                """ 
                Sur chaque pos dans la nouvelle liste :
                - vérifier si saut possible dans les diagonales
                - depl_b_d et depl_h_g

                """

                for pos in lst_dame_noir:
                    depl_b_g, _, pb_sup1 = SolDeplDames().solution_depl_dame_b_gauche(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )
                    depl_h_d, _, pb_sup2 = SolDeplDames().solution_depl_dame_h_droit(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )

                    if len(depl_b_g) > 0 and len(pb_sup1) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_b_g]
                        lst_pb_sup = [*lst_pb_sup, *pb_sup1]
                    elif len(depl_h_d) > 0 and len(pb_sup2) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_h_d]
                        lst_pb_sup = [*lst_pb_sup, *pb_sup2]
                    else:
                        pass

                print(f"liste depl : {lst_depl}")

            elif color_dame == "blanc":
                pos_saut = pn_sup[0]

                """ Touver la position de pos_saut dans la liste de depl_b_g """
                index_pos_saut = depl_b_d.index(pos_saut)

                lst_temp = depl_b_d[index_pos_saut + 1 :]

                """ Supprimer les pos saut dans la liste depl_b_g """
                lst_dame_blanc = [val for val in lst_temp if val not in pn_sup]

                print(f"liste dame blanc : {lst_dame_blanc}")

                """ 
                Sur chaque pos dans la nouvelle liste :
                - vérifier si saut possible dans les diagonales
                - depl_b_d et depl_h_g

                """

                for pos in lst_dame_blanc:
                    depl_b_g, pn_sup1, _ = SolDeplDames().solution_depl_dame_b_gauche(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )
                    depl_h_d, pn_sup2, _ = SolDeplDames().solution_depl_dame_h_droit(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )

                    if len(depl_b_g) > 0 and len(pn_sup1) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_b_g]
                        lst_pn_sup = [*lst_pn_sup, *pn_sup1]
                    elif len(depl_h_d) > 0 and len(pn_sup2) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_h_d]
                        lst_pn_sup = [*lst_pn_sup, *pn_sup2]
                    else:
                        pass

                print(f"liste depl : {lst_depl}")

            else:
                pass
        else:
            pass

        return lst_depl, lst_pn_sup, lst_pb_sup

    def depl_dame_h_g(
        self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
    ):
        lst_temp = []
        lst_depl = []
        lst_dame_noir = []
        lst_dame_blanc = []
        lst_pn_sup = []
        lst_pb_sup = []

        depl_h_g, pn_sup, pb_sup = SolDeplDames().solution_depl_dame_h_gauche(
            pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
        )

        if len(depl_h_g) > 0 and (len(pn_sup) > 0 or len(pb_sup) > 0):
            lst_depl = depl_h_g
            lst_pb_sup = pb_sup
            lst_pn_sup = pn_sup

            """Touver le position apres le 1er saut et en faire
            une nouvelle liste"""
            if color_dame == "noir":
                pos_saut = pb_sup[0]

                """ Touver la position de pos_saut dans la liste de depl_b_d """
                index_pos_saut = depl_h_g.index(pos_saut)

                lst_temp = depl_h_g[index_pos_saut + 1 :]

                """ Supprimer les pos saut dans la liste depl_b_g """
                lst_dame_noir = [val for val in lst_temp if val not in pb_sup]

                print(f"Liste dame noir : {lst_dame_noir}")

                """ 
                Sur chaque pos dans la nouvelle liste :
                - vérifier si saut possible dans les diagonales
                - depl_b_d et depl_h_g

                """

                for pos in lst_dame_noir:
                    depl_b_g, _, pb_sup1 = SolDeplDames().solution_depl_dame_b_gauche(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )
                    depl_h_d, _, pb_sup2 = SolDeplDames().solution_depl_dame_h_droit(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )

                    if len(depl_b_g) > 0 and len(pb_sup1) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_b_g]
                        lst_pb_sup = [*lst_pb_sup, *pb_sup1]
                    elif len(depl_h_d) > 0 and len(pb_sup2) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_h_d]
                        lst_pb_sup = [*lst_pb_sup, *pb_sup2]
                    else:
                        pass

                print(f"liste depl : {lst_depl}")

            elif color_dame == "blanc":
                pos_saut = pn_sup[0]

                """ Touver la position de pos_saut dans la liste de depl_b_g """
                index_pos_saut = depl_h_g.index(pos_saut)

                lst_temp = depl_h_g[index_pos_saut + 1 :]

                """ Supprimer les pos saut dans la liste depl_b_g """
                lst_dame_blanc = [val for val in lst_temp if val not in pn_sup]

                print(f"liste dame blanc : {lst_dame_blanc}")

                """ 
                Sur chaque pos dans la nouvelle liste :
                - vérifier si saut possible dans les diagonales
                - depl_b_d et depl_h_g

                """

                for pos in lst_dame_blanc:
                    depl_b_g, pn_sup1, _ = SolDeplDames().solution_depl_dame_b_gauche(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )
                    depl_h_d, pn_sup2, _ = SolDeplDames().solution_depl_dame_h_droit(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )

                    if len(depl_b_g) > 0 and len(pn_sup1) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_b_g]
                        lst_pn_sup = [*lst_pn_sup, *pn_sup1]
                    elif len(depl_h_d) > 0 and len(pn_sup2) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_h_d]
                        lst_pn_sup = [*lst_pn_sup, *pn_sup2]
                    else:
                        pass

                print(f"liste depl : {lst_depl}")

            else:
                pass
        else:
            pass

        return lst_depl, lst_pn_sup, lst_pb_sup

    def depl_dame_h_d(
        self, pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
    ):
        lst_temp = []
        lst_depl = []
        lst_dame_noir = []
        lst_dame_blanc = []
        lst_pn_sup = []
        lst_pb_sup = []

        depl_h_d, pn_sup, pb_sup = SolDeplDames().solution_depl_dame_h_droit(
            pos_dame, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb
        )

        if len(depl_h_d) > 0 and (len(pn_sup) > 0 or len(pb_sup) > 0):
            lst_depl = depl_h_d
            lst_pb_sup = pb_sup
            lst_pn_sup = pn_sup

            """Touver le position apres le 1er saut et en faire
            une nouvelle liste"""
            if color_dame == "noir":
                pos_saut = pb_sup[0]

                """ Touver la position de pos_saut dans la liste de depl_b_g """
                index_pos_saut = depl_h_d.index(pos_saut)

                lst_temp = depl_h_d[index_pos_saut + 1 :]

                """ Supprimer les pos saut dans la liste depl_b_g """
                lst_dame_noir = [val for val in lst_temp if val not in pb_sup]

                print(f"Liste dame noir : {lst_dame_noir}")

                """ 
                Sur chaque pos dans la nouvelle liste :
                - vérifier si saut possible dans les diagonales
                - depl_b_d et depl_h_g

                """

                for pos in lst_dame_noir:
                    depl_b_d, _, pb_sup1 = SolDeplDames().solution_depl_dame_b_droit(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )
                    depl_h_g, _, pb_sup2 = SolDeplDames().solution_depl_dame_h_gauche(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )

                    if len(depl_b_d) > 0 and len(pb_sup1) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_b_d]
                        lst_pb_sup = [*lst_pb_sup, *pb_sup1]
                    elif len(depl_h_g) > 0 and len(pb_sup2) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_h_g]
                        lst_pb_sup = [*lst_pb_sup, *pb_sup2]
                    else:
                        pass

                print(f"liste depl : {lst_depl}")

            elif color_dame == "blanc":
                pos_saut = pn_sup[0]

                """ Touver la position de pos_saut dans la liste de depl_b_g """
                index_pos_saut = depl_h_d.index(pos_saut)

                lst_temp = depl_h_d[index_pos_saut + 1 :]

                """ Supprimer les pos saut dans la liste depl_b_g """
                lst_dame_blanc = [val for val in lst_temp if val not in pn_sup]

                print(f"liste dame blanc : {lst_dame_blanc}")

                """ 
                Sur chaque pos dans la nouvelle liste :
                - vérifier si saut possible dans les diagonales
                - depl_b_d et depl_h_g

                """

                for pos in lst_dame_blanc:
                    depl_b_d, pn_sup1, _ = SolDeplDames().solution_depl_dame_b_droit(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )
                    depl_h_g, pn_sup2, _ = SolDeplDames().solution_depl_dame_h_gauche(
                        pos,
                        color_dame,
                        lst_case_vide,
                        lst_pos_pn,
                        lst_pos_pb,
                    )

                    if len(depl_b_d) > 0 and len(pn_sup1) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_b_d]
                        lst_pn_sup = [*lst_pn_sup, *pn_sup1]
                    elif len(depl_h_g) > 0 and len(pn_sup2) > 0:
                        """Deplacement avec saut"""
                        lst_depl = [*lst_depl, *depl_h_g]
                        lst_pn_sup = [*lst_pn_sup, *pn_sup2]
                    else:
                        pass

                print(f"liste depl : {lst_depl}")

            else:
                pass
        else:
            pass

        return lst_depl, lst_pn_sup, lst_pb_sup
