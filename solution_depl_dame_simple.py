"""
    class pour trouver les solutions de deplacement des dames blanches ou noires

"""

from fonctions import (
    depl_pion_bas_droit,
    depl_pion_bas_gauche,
    depl_pion_haut_droit,
    depl_pion_haut_gauche,
    # ident_pion_noir_blanc,
)


class SolDeplDames:
    def __init__(self, dame_select, lst_case_vide):
        self.dame_select = dame_select  # Pos de la dame_select
        self.lst_case_vide = lst_case_vide  # liste des cases vides

        self.sol = "solution_"
        self.compteur = 0

        self.dict_depl = {}

    def solution_depl_dame_b_gauche(self):
        pos_pion = self.dame_select

        depl_b_g = depl_pion_bas_gauche(pos_pion)

        if len(depl_b_g) > 0 and depl_b_g in self.lst_case_vide:
            # Si la case est vide on incrémente le N° de la solution
            self.compteur += 1

            # Si la case est vide, on crée la solution de déplacement
            self.dict_depl[self.sol + str(self.compteur)] = [pos_pion, depl_b_g]

            # La nouvelle position de départ est décalé de 1
            pos_pion = depl_b_g

            while len(pos_pion) > 0:
                depl_temp = ()
                depl_temp = depl_pion_bas_gauche(pos_pion)

                if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                    # Si la case est vide, on l'ajoute a la solution de déplacement
                    self.dict_depl[self.sol + str(self.compteur)].append(depl_temp)

                    # On modifie la nouvelle position de départ
                    pos_pion = depl_temp

                else:
                    pos_pion = ()
        else:
            pass

    def solution_depl_dame_b_droit(self):
        pos_pion = self.dame_select

        depl_b_d = depl_pion_bas_droit(pos_pion)

        if len(depl_b_d) > 0 and depl_b_d in self.lst_case_vide:
            # Si la case est vide on incrémente le N° de la solution
            self.compteur += 1

            self.dict_depl[self.sol + str(self.compteur)] = [pos_pion, depl_b_d]

            pos_pion = depl_b_d

            while len(pos_pion) > 0:
                depl_temp = ()
                depl_temp = depl_pion_bas_droit(pos_pion)

                if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                    self.dict_depl[self.sol + str(self.compteur)].append(depl_temp)

                    pos_pion = depl_temp

                else:
                    pos_pion = ()

        else:
            pass

    def solution_depl_dame_h_gauche(self):
        pos_pion = self.dame_select

        depl_h_g = depl_pion_haut_gauche(pos_pion)

        if len(depl_h_g) > 0 and depl_h_g in self.lst_case_vide:
            # Si la case est vide on incrémente le N° de la solution
            self.compteur += 1

            # Si la case est vide, on crée la solution de déplacement
            self.dict_depl[self.sol + str(self.compteur)] = [pos_pion, depl_h_g]

            # La nouvelle position de départ est décalé de 1
            pos_pion = depl_h_g

            while len(pos_pion) > 0:
                depl_temp = ()
                depl_temp = depl_pion_haut_gauche(pos_pion)

                if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                    # Si la case est vide, on l'ajoute a la solution de déplacement
                    self.dict_depl[self.sol + str(self.compteur)].append(depl_temp)

                    # On modifie la nouvelle position de départ
                    pos_pion = depl_temp

                else:
                    pos_pion = ()

        else:
            pass

    def solution_depl_dame_h_droit(self):
        pos_pion = self.dame_select

        depl_h_d = depl_pion_haut_droit(pos_pion)

        if len(depl_h_d) > 0 and depl_h_d in self.lst_case_vide:
            self.compteur += 1

            self.dict_depl[self.sol + str(self.compteur)] = [pos_pion, depl_h_d]

            pos_pion = depl_h_d

            while len(pos_pion) > 0:
                depl_temp = ()
            
                depl_temp = depl_pion_haut_droit(pos_pion)
            
                if len(depl_temp) > 0 and depl_temp in self.lst_case_vide:
                    self.dict_depl[self.sol + str(self.compteur)].append(depl_temp)
            
                    pos_pion = depl_temp

                else:
                    pos_pion = ()

        else:
            pass

    def solution_depl_dame(self):
        # Lancement des 4 solutions de deplacement pour la dame
        self.solution_depl_dame_b_gauche()
        self.solution_depl_dame_b_droit()
        self.solution_depl_dame_h_gauche()
        self.solution_depl_dame_h_droit()

        return self.dict_depl
