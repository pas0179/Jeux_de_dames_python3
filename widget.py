import tkinter as tk

from fonctions import ident_pion_noir_blanc, convert_coord


class Widget:
    def __init__(self, fen):
        self.fen = fen

        self.lst_cases_noir = []
        self.lst_id_pn = []
        self.lst_id_pb = []
        self.lst_case_vide = []

        self.lst_id_dame_noir = []
        self.lst_id_dame_blanc = []

        self.pos_dame_noir = []
        self.pos_dame_blanc = []

        self.id_dame = 141

        # Listes des cases jaunes ( case possible)
        self.lst_id_case_jaune = []

        self.create_damier()

        self.damier = []

        self.lst_pos_pn = self.lst_cases_noir[0:20]
        self.lst_pos_pb = self.lst_cases_noir[30:]

        self.lst_pos_dn = []
        self.lst_pos_db = []

        self.create_pion()

    def create_damier(self):
        # Creation du canvas
        self.can = tk.Canvas(self.fen, bg="ivory")
        self.can.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Création du damier
        color = ["#fbfebc", "#3f0b01"]

        x, y = 0, 0
        dx, dy = 60, 60

        for j in range(0, 10):
            for i in range(0, 10):
                self.damier = self.can.create_rectangle(
                    x * i,
                    y * j,
                    x * i + dx,
                    y * j + dy,
                    outline="black",
                    width=2,
                    fill=color[(j + i) % 2],
                )
                x = dx
                if (j + i) % 2 == 1:
                    self.lst_cases_noir.append((x * i, y * j, x * i + dx, y * j + dy))
            y = dy

    # Création des pions a partir d'une classe
    def create_pion(self):
        # Création des pions noirs

        # Liste des N° d'objets de 101 a 120: Pions noirs
        # de 121 a 140: Pions Blancs
        self.lst_id_pn = []
        id_pn = 101
        for el in self.lst_pos_pn:
            PionNoir(self.can, el[0], el[1])
            self.lst_id_pn.append(id_pn)
            id_pn += 1

        # Création des pions blancs
        self.lst_id_pb = []
        id_pb = 121
        for el in self.lst_pos_pb:
            PionBlanc(self.can, el[0], el[1])
            self.lst_id_pb.append(id_pb)
            id_pb += 1

    def create_dame_noir(self, x, y):
        # création des dames
        pos_x, pos_y = x, y

        DameNoir(self.can, pos_x, pos_y)
        self.lst_id_dame_noir.append(self.id_dame)
        self.lst_pos_dn.append((pos_x, pos_y, pos_x + 60, pos_y + 60))
        self.id_dame += 1

    def create_dame_blanche(self, x, y):
        pos_x, pos_y = x, y
        DameBlanche(self.can, pos_x, pos_y)
        self.lst_id_dame_blanc.append(self.id_dame)
        self.lst_pos_db.append((pos_x, pos_y, pos_x + 60, pos_y + 60))
        self.id_dame += 1

    def maj_lst_case_vide(self):
        lst_case_vide = []

        """ Création de la liste des cases vides sur l'échiquier """

        lst_case_vide = [
            (i[0], i[1], i[0] + 60, i[1] + 60)
            for i in self.lst_cases_noir
            if i not in self.lst_pos_pn and i not in self.lst_pos_pb
        ]

        return lst_case_vide

    def find_id(self, coord):
        x, y = coord[0], coord[1]
        id = self.can.find_closest(x, y)
        id = id[0]

        return id

    def maj_lst_pos_pion(self, id, old_pos, new_pos):
        # On commence par la couleur du pion
        color_pion = ident_pion_noir_blanc(id)

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
            for el in self.lst_id_case_jaune:
                self.can.itemconfigure(el, fill="#3f0b01")
        else:
            pass

    def color_case_possible(self, lst_case_possible):
        self.lst_id_case_jaune = []

        """
        Recherche des ids des cases noirs dans la listes des cases possible
        et enregistrement des ids dans une liste

        """
        if len(lst_case_possible) > 0:
            self.lst_id_case_jaune = [(self.find_id(val)) for val in lst_case_possible]

        else:
            pass

        """
        On applique la couleur jaune aux cases noirs qui sont dans la liste
        des ids des cases possible

        """
        if len(self.lst_id_case_jaune) > 0:
            for el in self.lst_id_case_jaune:
                self.can.itemconfigure(el, fill="yellow")
        else:
            pass

    def restor_pion(self, id, color_pion):
        # Même endroit, on applique la couleur d'origine du pion selectionné
        if color_pion == "noir":
            self.can.itemconfigure(id, fill="black", outline="#87ce3b")
        elif color_pion == "blanc":
            self.can.itemconfigure(id, fill="white", outline="#3b41ce")
        else:
            pass

    def restor_dame_blanche_noir(self, id, color_dame):
        pion = ident_pion_noir_blanc(id)
        if pion == "dame":
            if color_dame == "blanc":
                self.can.itemconfigure(id, fill="white", outline="#e67e22")
            elif color_dame == "noir":
                self.can.itemconfigure(id, fill="black", outline="#e67e22")
            else:
                pass
        else:
            pass

    def restor_pion_ou_dame(self, id, color_pion):
        if 100 < id < 141:
            self.restor_pion(id, color_pion)
        elif id > 140:
            self.restor_dame_blanche_noir(id, color_pion)
        else:
            pass

    def depl_pion(self, id, coord_release, color_pion, pos_pion_select):
        # Convert d'un tuple en coordonnées de déplacement
        # pour un pion blanc ou noir
        new_pos = (
            coord_release[0] + 5,
            coord_release[1] + 5,
            coord_release[0] + 55,
            coord_release[1] + 55,
        )
        # Convert new_pos car format non valide
        new_coord = convert_coord(new_pos[0], new_pos[1], self.lst_cases_noir)

        # Déplacement du pion suivant l'id
        self.can.coords(id, new_pos[0], new_pos[1], new_pos[2], new_pos[3])

        # On lance la fonction "restor_pion"
        self.restor_pion_ou_dame(id, color_pion)
        # Lancement de la mise a jour des listes
        self.maj_lst_pos_pion(id, pos_pion_select, new_coord)

    def sup_pion(self, id, lst_pion_sup):
        lst_id_pion_sup = []

        lst_id_pion_sup = [
            (self.find_id((val[0] + 15, val[1] + 15))) for val in lst_pion_sup
        ]

        color_pion = ident_pion_noir_blanc(id)

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


class PionNoir:
    def __init__(self, can, x, y):
        self.can = can
        self.x = x
        self.y = y

        self.can.create_oval(
            self.x + 5,
            self.y + 5,
            self.x + 55,
            self.y + 55,
            fill="black",
            outline="#87ce3b",
            width=5,
            tag="noir",
        )


class PionBlanc:
    def __init__(self, can, x, y):
        self.can = can
        self.x = x
        self.y = y

        self.can.create_oval(
            self.x + 5,
            self.y + 5,
            self.x + 55,
            self.y + 55,
            fill="white",
            outline="#3b41ce",
            width=5,
            tag="blanc",
        )


class DameBlanche:
    def __init__(self, can, x, y):
        self.can = can
        self.x = x
        self.y = y

        self.can.create_oval(
            self.x + 5,
            self.y + 5,
            self.x + 55,
            self.y + 55,
            fill="white",
            outline="#e67e22",
            width=5,
            tag="blanc",
        )


class DameNoir:
    def __init__(self, can, x, y):
        self.can = can
        self.x = x
        self.y = y

        self.can.create_oval(
            self.x + 5,
            self.y + 5,
            self.x + 55,
            self.y + 55,
            fill="black",
            outline="#e67e22",
            width=5,
            tag="noir",
        )
