"""
    class pour trouver les solutions de deplacement des dames blanches 
    ou noires avec saut ou pas. Le calcul se fait sur les diagonales 
    suivant la position de la dame.

Solutions pour une dame :

dame depl_h_d et depl_b_g : depl_b_d et depl_h_g
dame depl_h_g et depl_b_d : depl_b_g et depl_h_d


"""

from fonctions import (
    depl_pion_bas_droit,
    depl_pion_bas_gauche,
    depl_pion_haut_droit,
    depl_pion_haut_gauche,
    saut_bas_g,
    saut_bas_d,
    saut_haut_g,
    saut_haut_d,
)


class SolDeplDames:
    def __init__(self, color_dame, lst_case_vide, lst_pos_pn, lst_pos_pb):

        self.color_dame = color_dame
        self.lst_case_vide = lst_case_vide
        self.lst_pos_pn = lst_pos_pn
        self.lst_pos_pb = lst_pos_pb

        self.lst_depl = []
        self.dict_saut = {}
        self.new_pos = {}




    """
    Methode calcul des solutions de deplacements Bas Gauche
    pour une dame noire ou blanche,  
    - depl_bas gauche : depl_bas droit et depl_haut gauche    
    """
    def solution_depl_dame_b_gauche(self, position):
        lst_depl = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []
        new_pos_saut = []

        """ Initialisation de la position de la dame sélectionnée """
        new_pos = position

        """ Boucle pour créer la liste des deplacements possibles
        sur la même diagonale """
        while len(new_pos) > 0:
            depl_temp = ()

            """ fonction de deplacement d'une case en diagonale """
            depl_temp = depl_pion_bas_gauche(new_pos)

            """
            Si la case est vide :
            - ajout dans la liste des deplacements
            """
            if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                lst_depl.append(depl_temp)

                new_pos = depl_temp

            else:
                """Si la case n'est pas vide :
                - lancement fonction saut_bas_g"""
                saut_temp, pn_sup, pb_sup = saut_bas_g(
                    new_pos,
                    self.color_dame,
                    self.lst_case_vide,
                    self.lst_pos_pn,
                    self.lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    """Saut possible sur la meme diagonale"""
                    new_pos_saut.append(saut_temp)
                    if len(pn_sup) > 0:
                        lst_pn_sup.append(pn_sup)
                        lst_depl.append(pn_sup)
                    elif len(pb_sup) > 0:
                        lst_pb_sup.append(pb_sup)
                        lst_depl.append(pb_sup)
                    else:
                        pass

                    """ Ajout dans la liste des depl """
                    lst_depl.append(saut_temp)
                    new_pos = saut_temp

                else:
                    """Saut ou deplacement impossible"""
                    new_pos = ()

        return lst_depl, lst_pn_sup, lst_pb_sup

    def solution_depl_dame_b_droit(self, position):
        lst_depl = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []
        new_pos_saut = []

        new_pos = position

        while len(new_pos) > 0:
            depl_temp = ()
            depl_temp = depl_pion_bas_droit(new_pos)

            if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                lst_depl.append(depl_temp)

                new_pos = depl_temp

            else:
                saut_temp, pn_sup, pb_sup = saut_bas_d(
                    new_pos,
                    self.color_dame,
                    self.lst_case_vide,
                    self.lst_pos_pn,
                    self.lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    new_pos_saut.append(saut_temp)

                    if len(pn_sup) > 0:
                        lst_pn_sup.append(pn_sup)
                        lst_depl.append(pn_sup)
                    if len(pb_sup) > 0:
                        lst_pb_sup.append(pb_sup)
                        lst_depl.append(pb_sup)
                    else:
                        pass

                    lst_depl.append(saut_temp)

                    new_pos = saut_temp

                else:
                    new_pos = ()

        return lst_depl, lst_pn_sup, lst_pb_sup

    def solution_depl_dame_h_gauche(self, position):
        lst_depl = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []
        new_pos_saut = []

        new_pos = position

        while len(new_pos) > 0:
            depl_temp = ()
            depl_temp = depl_pion_haut_gauche(new_pos)

            if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                lst_depl.append(depl_temp)

                new_pos = depl_temp

            else:
                saut_temp, pn_sup, pb_sup = saut_haut_g(
                    new_pos,
                    self.color_dame,
                    self.lst_case_vide,
                    self.lst_pos_pn,
                    self.lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    new_pos_saut.append(saut_temp)

                    if len(pn_sup) > 0:
                        lst_pn_sup.append(pn_sup)
                        lst_depl.append(pn_sup)
                    if len(pb_sup) > 0:
                        lst_pb_sup.append(pb_sup)
                        lst_depl.append(pb_sup)
                    else:
                        pass

                    lst_depl.append(saut_temp)

                    new_pos = saut_temp

                else:
                    new_pos = ()

        return lst_depl, lst_pn_sup, lst_pb_sup

    def solution_depl_dame_h_droit(self, position):
        lst_depl = []
        pn_sup, pb_sup = [], []
        lst_pn_sup, lst_pb_sup = [], []
        new_pos_saut = []

        new_pos = position

        while len(new_pos) > 0:
            depl_temp = ()
            depl_temp = depl_pion_haut_droit(new_pos)

            if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                lst_depl.append(depl_temp)

                new_pos = depl_temp

            else:
                saut_temp, pn_sup, pb_sup = saut_haut_d(
                    new_pos,
                    self.color_dame,
                    self.lst_case_vide,
                    self.lst_pos_pn,
                    self.lst_pos_pb,
                )

                if len(saut_temp) > 0:
                    new_pos_saut.append(saut_temp)

                    if len(pn_sup) > 0:
                        lst_pn_sup.append(pn_sup)
                        lst_depl.append(pn_sup)
                    if len(pb_sup) > 0:
                        lst_pb_sup.append(pb_sup)
                        lst_depl.append(pb_sup)
                    else:
                        pass

                    lst_depl.append(saut_temp)

                    new_pos = saut_temp

                else:
                    new_pos = ()

        return lst_depl, lst_pn_sup, lst_pb_sup

    """ Methode pour test dans __main__ """

    def deplacements(self, position):

        deplbg, pn_supbg, pb_supbg = self.solution_depl_dame_b_gauche(position)

        deplbd, pn_supbd, pb_supbd = self.solution_depl_dame_b_droit(position)

        deplhg, pn_suphg, pb_suphg = self.solution_depl_dame_h_gauche(position)

        deplhd, pn_suphd, pb_suphd = self.solution_depl_dame_h_droit(position)

        depl = [*deplbg, *deplbd, *deplhg, *deplhd]
        pn_sup = [*pn_supbg, *pn_supbd, *pn_suphg, *pn_suphd]
        pb_sup = [*pb_supbg, *pb_supbd, *pb_suphg, *pb_suphd]

        return depl, pn_sup, pb_sup

