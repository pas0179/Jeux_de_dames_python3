"""Création du damier, des pions et des dames"""

import tkinter as tk

from fonctions import ident_pion_noir_blanc, convert_coord


class Widget:
    """Classe widget"""
    def __init__(self, fen):
        """initialisation des attributs"""
        self.fen = fen

        """initialisation des variables pour les méthodes"""
        self.lst_cases_noir = []
        self.lst_id_pn = []
        self.lst_id_pb = []
        self.lst_case_vide = []

        self.id_dame = 141

        # Listes des cases jaunes ( case possible)
        self.lst_id_case_jaune = []

        """Création du damier"""
        self.create_damier()

        self.damier = []

        self.lst_pos_pn = self.lst_cases_noir[0:20]
        self.lst_pos_pb = self.lst_cases_noir[30:]

        self.create_pion()

    def create_damier(self):
        """Creation du damier"""
        self.can = tk.Canvas(self.fen, bg="ivory")
        self.can.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        color = ["#fbfebc", "#3f0b01"]

        pos_x, pos_y = 0, 0
        pos_dx, pos_dy = 60, 60

        for j in range(0, 10):
            for i in range(0, 10):
                self.damier = self.can.create_rectangle(
                    pos_x * i,
                    pos_y * j,
                    pos_x * i + pos_dx,
                    pos_y * j + pos_dy,
                    outline="black",
                    width=2,
                    fill=color[(j + i) % 2],
                )
                pos_x = pos_dx
                if (j + i) % 2 == 1:
                    self.lst_cases_noir.append(
                        (
                            pos_x * i,
                            pos_y * j,
                            pos_x * i + pos_dx,
                            pos_y * j + pos_dy,
                        )
                    )
            pos_y = pos_dy

    # Création des pions a partir d'une classe
    def create_pion(self):
        """Creation des pions"""
        # Liste des N° d'objets de 101 a 120: Pions noirs
        # de 121 a 140: Pions Blancs
        self.lst_id_pn = []
        id_pn = 101
        for element in self.lst_pos_pn:
            PionNoir(self.can, element[0], element[1])
            self.lst_id_pn.append(id_pn)
            id_pn += 1

        # Création des pions blancs
        self.lst_id_pb = []
        id_pb = 121
        for element in self.lst_pos_pb:
            PionBlanc(self.can, element[0], element[1])
            self.lst_id_pb.append(id_pb)
            id_pb += 1

    def maj_lst_case_vide(self):
        """ Création de la liste des cases vides sur l'échiquier """
        lst_case_vide = []

        lst_case_vide = [
            (i[0], i[1], i[0] + 60, i[1] + 60)
            for i in self.lst_cases_noir
            if i not in self.lst_pos_pn and i not in self.lst_pos_pb
        ]

        return lst_case_vide

    def find_id(self, coord):
        """Renvoie l'id du pion"""
        posx, posy = coord[0], coord[1]
        id_pion = self.can.find_closest(posx, posy)
        id_pion = id_pion[0]

        return id_pion

    def find_pos_all_dames(self, color_dame, lst_pos_pn, lst_pos_pb):
        """Renvoie la liste des positions des dames"""
        lst_id_dame = []

        if color_dame == "noir":
            for val in lst_pos_pn:
                id_temp = self.find_id(val)
                if id_temp > 140:
                    lst_id_dame.append(id_temp)
                else:
                    pass
        if color_dame == "blanc":
            for val in lst_pos_pb:
                id_temp = self.find_id(val)
                if id_temp > 140:
                    lst_id_dame.append(id_temp)
                else:
                    pass
        else:
            pass

        return lst_id_dame

    def find_color(self, id_pion):
        """Renvoie la couleur du pion"""
        color = ""

        if 100 < id_pion < 141:
            color = ident_pion_noir_blanc(id_pion)
        elif id_pion > 140:
            color = self.can.gettags(id_pion)[0]
        else:
            pass

        return color

    def maj_lst_pos_pion(self, id_pion, old_pos, new_pos):
        """Mise à jour des positions des pions"""
        color_pion = self.find_color(id_pion)

        old_pos = (old_pos[0], old_pos[1], old_pos[0] + 60, old_pos[1] + 60)

        if color_pion == "noir":
            if old_pos in self.lst_pos_pn:
                self.lst_pos_pn.remove(old_pos)

                self.lst_pos_pn.append(new_pos)
            else:
                pass
        if color_pion == "blanc":
            if old_pos in self.lst_pos_pb:
                self.lst_pos_pb.remove(old_pos)

                self.lst_pos_pb.append(new_pos)

            else:
                pass

    def restor_case_noir(self):
        """
        On applique la couleur noir aux cases jaunes qui sont dans la liste
        des ids des cases jaunes

        """
        if len(self.lst_id_case_jaune) > 0:
            for element in self.lst_id_case_jaune:
                self.can.itemconfigure(element, fill="#3f0b01")
        else:
            pass

    def color_case_possible(self, lst_case_possible):
        """
        Recherche des ids des cases noirs dans la listes des cases possible
        et enregistrement des ids dans une liste

        """
        self.lst_id_case_jaune = []

        if len(lst_case_possible) > 0:
            self.lst_id_case_jaune = [
                (self.find_id(val)) for val in lst_case_possible
            ]

        else:
            pass

        if len(self.lst_id_case_jaune) > 0:
            for element in self.lst_id_case_jaune:
                self.can.itemconfigure(element, fill="yellow")
        else:
            pass

    def restor_pion(self, id_pion, color_pion):
        """Restauration de la couleur du pion"""
        if color_pion == "noir":
            self.can.itemconfigure(id_pion, fill="black", outline="#87ce3b")
        elif color_pion == "blanc":
            self.can.itemconfigure(id_pion, fill="white", outline="#3b41ce")
        else:
            pass

    def restor_dame_blanche_noir(self, id, color_dame):
        """Restauration de la couleur de la dame"""
        if color_dame == "blanc":
            self.can.itemconfigure(id, fill="white", outline="#e67e22")
        elif color_dame == "noir":
            self.can.itemconfigure(id, fill="black", outline="#e67e22")
        else:
            pass

    def restor_pion_ou_dame(self, id_pion, color_pion):
        """Recherche quel type de pion ou dame est le pion"""
        if 100 < id_pion < 141:
            self.restor_pion(id_pion, color_pion)
        elif id_pion > 140:
            self.restor_dame_blanche_noir(id_pion, color_pion)
        else:
            pass

    def depl_pion(self, id_pion, coord_release, color_pion, pos_pion_select):
        """Déplacement du pion"""
        new_pos = (
            coord_release[0] + 5,
            coord_release[1] + 5,
            coord_release[0] + 55,
            coord_release[1] + 55,
        )
        # Convert new_pos car format non valide
        new_coord = convert_coord(new_pos[0], new_pos[1], self.lst_cases_noir)

        # Déplacement du pion suivant l'id
        self.can.coords(
            id_pion,
            new_pos[0],
            new_pos[1],
            new_pos[2],
            new_pos[3],
        )

        # On lance la fonction "restor_pion"
        self.restor_pion_ou_dame(id_pion, color_pion)
        # Lancement de la mise a jour des listes
        self.maj_lst_pos_pion(id_pion, pos_pion_select, new_coord)

    def sup_pion(self, id_pion, lst_pion_sup):
        """Suppression des pions"""
        lst_id_pion_sup = []

        lst_id_pion_sup = [
            (self.find_id((val[0] + 15, val[1] + 15))) for val in lst_pion_sup
        ]

        color_pion = self.find_color(id_pion)

        if color_pion == "noir":
            for val in lst_id_pion_sup:
                # Suppression de la liste des ids
                self.lst_id_pb.remove(val)
                # Suppression de l'objet par son id
                self.can.delete(val)

            for val in lst_pion_sup:
                # Suppression de la liste des positions des PionNoir
                self.lst_pos_pb.remove(val)

        elif color_pion == "blanc":
            for val in lst_id_pion_sup:
                self.lst_id_pn.remove(val)
                self.can.delete(val)

            for val in lst_pion_sup:
                self.lst_pos_pn.remove(val)

        else:
            pass

    def create_dame_noir(self, pos_x, pos_y):
        """Creation des dames noires"""
        DameNoir(self.can, pos_x, pos_y)
        self.lst_id_pn.append(self.id_dame)
        self.lst_pos_pn.append((pos_x, pos_y, pos_x + 60, pos_y + 60))
        self.id_dame += 1

    def create_dame_blanche(self, pos_x, pos_y):
        """Creation des dames blanches"""
        DameBlanche(self.can, pos_x, pos_y)
        self.lst_id_pb.append(self.id_dame)
        self.lst_pos_pb.append((pos_x, pos_y, pos_x + 60, pos_y + 60))
        self.id_dame += 1


class PionNoir:
    """Création des pions noirs"""
    def __init__(self, can, posx, posy):
        self.can = can
        self.pos_x = posx
        self.pos_y = posy

        self.can.create_oval(
            self.pos_x + 5,
            self.pos_y + 5,
            self.pos_x + 55,
            self.pos_y + 55,
            fill="black",
            outline="#87ce3b",
            width=5,
            tag="noir",
        )


class PionBlanc:
    """Création des pions blancs"""
    def __init__(self, can, posx, posy):
        self.can = can
        self.pos_x = posx
        self.pos_y = posy

        self.can.create_oval(
            self.pos_x + 5,
            self.pos_y + 5,
            self.pos_x + 55,
            self.pos_y + 55,
            fill="white",
            outline="#3b41ce",
            width=5,
            tag="blanc",
        )


class DameBlanche:
    """Création des dames blanches"""
    def __init__(self, can, posx, posy):
        self.can = can
        self.pos_x = posx
        self.pos_y = posy

        self.can.create_oval(
            self.pos_x + 5,
            self.pos_y + 5,
            self.pos_x + 55,
            self.pos_y + 55,
            fill="white",
            outline="#e67e22",
            width=5,
            tag="blanc",
        )


class DameNoir:
    def __init__(self, can, posx, posy):
        self.can = can
        self.pos_x = posx
        self.pos_y = posy

        self.can.create_oval(
            self.pos_x + 5,
            self.pos_y + 5,
            self.pos_x + 55,
            self.pos_y + 55,
            fill="black",
            outline="#e67e22",
            width=5,
            tag="noir",
        )
