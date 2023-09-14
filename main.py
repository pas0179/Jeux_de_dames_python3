"""Class principale pour le jeu de dames"""

import tkinter as tk
from tkinter import messagebox

from coord_convert import CoordConvert
from fonctions import convert_coord, convert_dict_lst
from player import Player
from solution_depl import Move

# from solution_depl_dame import DeplDames
# from solution_depl_dame_base import SolDeplDames

from solution_depl_dame_saut import SautDames
from sup_pion import SuppPion
from widget import Widget


class App:
    """Class principale pour le jeu de dames"""
    def __init__(self, title):
        """Initialisation des attributs"""
        self.fen = tk.Tk()

        """Configuration de la fenêtre"""
        self.fen.title(title)
        self.fen.geometry("750x610")
        self.fen.minsize(750, 610)
        self.fen.maxsize(750, 610)
        self.fen.config(bg="black")

        self.lst_case_vide = []
        self.lst_tour = []

        self.lst_case_possible = []
        self.dict_case_possible = {}

        self.lst_pb_sup = []
        self.lst_pn_sup = []

        self.lst_pion_noir_sup = []
        self.lst_pion_blanc_sup = []

        self.lst_depl_pion = []

        self.id_pion = 0

        self.id_ps = []

        self.dict_saut = {}
        self.compteur = 0

        # Tuple pour la position du pion noir ou blanc sélectionné
        self.pn_select = (0, 0)
        self.pb_select = (0, 0)

        self.lst_ids = []
        self.lst_coord = []

        self.pos_pion_select = (0, 0, 0, 0)

        self.dict_depl = {}

        # Intégration des widgets dans le fichier 'widget.py'
        self.widget = Widget(self.fen)
        self.player = Player()

        # Début du jeu
        self.start_game()

        # Lancement du fichier pour créer la liste des cases noirs vides
        self.lst_case_vide = self.widget.maj_lst_case_vide()

        # Récup evenement button souris 1
        self.fen.bind("<Button-1>", self.select_pion)
        self.fen.bind("<ButtonRelease-1>", self.release_pion)
        self.fen.bind("<Motion>", self.move_mouse)
        self.fen.bind("<Key>", self.quitter)

        # run
        self.fen.mainloop()

    def start_game(self):
        """Debut du jeu"""
        message = messagebox.askquestion(
            "Question", "Voulez vous commencer avec les pions blancs ?"
        )
        if message == "yes":
            debut = (0, "noir", 0, 0)
            self.lst_depl_pion.append(debut)
        else:
            debut = (1, "blanc", 0, 0)
            self.lst_depl_pion.append(debut)

    def quitter(self, event):
        """Quitter le jeu"""
        key = event.keysym
        if key in ('q', 'Escape'):
            self.fen.destroy()
            self.fen.quit()

    def move_mouse(self, event):
        """Mouvement de la souris"""
        new_pos = CoordConvert(event.x, event.y, self.widget.lst_cases_noir)
        coord = new_pos.coord

        self.lst_coord.append(coord)

    def verif_creation_dame(self, id_pion, coord_release):
        """on vérifie d'abord si le pion noir ou blanc
        est sur la case de création d'une dame"""
        color_pion = self.widget.find_color(id_pion)

        if color_pion == "noir" and (
            coord_release[1] >= 540 and coord_release[3] >= 540
        ):
            self.widget.can.delete(id_pion)
            self.widget.lst_pos_pn.remove(coord_release)
            self.widget.lst_id_pn.remove(id_pion)

            self.widget.create_dame_noir(coord_release[0], coord_release[1])

        elif color_pion == "blanc" and (
            coord_release[1] <= 60 and coord_release[3] <= 60
        ):
            self.widget.can.delete(id_pion)
            self.widget.lst_pos_pb.remove(coord_release)
            self.widget.lst_id_pb.remove(id_pion)

            # Création de la dame create_dame_blanche
            self.widget.create_dame_blanche(coord_release[0], coord_release[1])

        else:
            pass

    def select_pion(self, event):
        """Methode pour sélectionner un pion"""

        coord = (event.x, event.y)

        self.lst_coord = []

        self.lst_case_vide = self.widget.maj_lst_case_vide()

        # On identifie l'objet selectionné par le clic de souris
        self.id_pion = self.widget.find_id(coord)

        #   On récupère les coordonnées de l'objet selectionné
        coord_id = self.widget.can.coords(self.id_pion)
        # Modif des coordonnées
        coord_id = [
            coord_id[0] - 5,
            coord_id[1] - 5,
            coord_id[2] + 5,
            coord_id[3] + 5,
        ]

        # On vérifie que c'est bien un pion qui est selectionné
        if 100 < self.id_pion < 141:
            # # on recupère la couleur du pion selectionné
            color_pion = self.widget.find_color(self.id_pion)

            # On regarde a qui le tour sauf si saut
            player = self.player.select_player(
                self.id_pion,
                color_pion,
                self.lst_depl_pion,
                self.lst_pb_sup,
                self.lst_pn_sup,
            )

            if player == color_pion:
                self.widget.can.itemconfigure(
                    self.id_pion,
                    fill="red",
                    outline="red",
                )

                self.pos_pion_select = (
                    int(coord_id[0]),
                    int(coord_id[1]),
                    int(coord_id[0] + 60),
                    int(coord_id[1] + 60),
                )

                self.dict_depl = {}

                sol = Move(
                    # self.id,
                    self.pos_pion_select,
                    color_pion,
                    self.lst_case_vide,
                    self.widget.lst_pos_pn,
                    self.widget.lst_pos_pb,
                )
                self.dict_depl = sol.dict_solution
                self.lst_pn_sup = sol.lst_pn_sup
                self.lst_pb_sup = sol.lst_pb_sup

                # On lance la conversion pour passer d'un dictionnaire
                # a une liste de tuples
                self.lst_case_possible = convert_dict_lst(
                    self.dict_depl, self.pos_pion_select
                )

                # self.widget.color_case_possible(self.lst_case_possible)
            else:
                messagebox.showinfo(
                    "Erreur", "Ce nest pas a vous de jouer !!!"
                )

        # Si select dame
        elif self.id_pion > 140:
            # On recupère la couleur de la dame
            color_dame = self.widget.find_color(self.id_pion)

            player = self.player.select_player(
                self.id_pion,
                color_dame,
                self.lst_depl_pion,
                self.lst_pb_sup,
                self.lst_pn_sup,
            )

            if player == color_dame:
                self.widget.can.itemconfigure(
                    self.id_pion,
                    fill="red",
                    outline="red",
                )

                # On affecte les coordonnées
                self.pos_pion_select = (
                    int(coord_id[0]),
                    int(coord_id[1]),
                    int(coord_id[0] + 60),
                    int(coord_id[1] + 60),
                )

                # On récuprère la lise des deplacements possibles
                sol = SautDames(
                    self.pos_pion_select,
                    color_dame,
                    self.lst_case_vide,
                    self.widget.lst_pos_pn,
                    self.widget.lst_pos_pb,
                )

                lst_depl = sol.lst_depl
                lst_saut = convert_dict_lst(
                    sol.dict_saut,
                    self.pos_pion_select,
                )
                lst_other = convert_dict_lst(
                    sol.dict_other,
                    self.pos_pion_select,
                )
                self.lst_pn_sup = sol.lst_pn_sup
                self.lst_pb_sup = sol.lst_pb_sup

                self.lst_case_possible = lst_depl + lst_saut + lst_other
                # self.widget.color_case_possible(self.lst_case_possible)
            else:
                messagebox.showinfo(
                    "Erreur", "Ce n'est pas a vous de jouer !!!"
                )
        else:
            self.id_pion = 0

    def release_pion(self, event):
        """Methode pour relacher un pion"""
        # On récupère les coordonnées x, y du bouton relaché
        # x=98, y=275
        # On convertie x et y en coordonnées lisible
        coord_release = convert_coord(
            event.x,
            event.y,
            self.widget.lst_cases_noir,
        )

        # 1- Relachement du clic au même endroit sur un pion
        # On vérifie que c'est bien un pion qui a été sélectionné
        # if 100 < self.id < 141:
        if self.id_pion > 100:
            # C'est un pion
            # On récupère la couleur du pion sélectionné
            color_pion = self.widget.find_color(self.id_pion)
            # color_pion = ident_pion_noir_blanc(self.id)

            if (
                self.pos_pion_select[0] == coord_release[0]
                and self.pos_pion_select[1] == coord_release[1]
            ):

                self.widget.restor_pion_ou_dame(self.id_pion, color_pion)

                self.widget.restor_case_noir()

            # Relachement du clic sur une autre case
            else:
                if (
                    len(self.lst_case_possible) == 0
                    or coord_release not in self.lst_case_possible
                ):
                    self.widget.restor_pion_ou_dame(self.id_pion, color_pion)

                    self.widget.restor_case_noir()

                if coord_release in self.lst_case_possible:
                    if len(self.lst_pb_sup) == 0 and len(self.lst_pn_sup) == 0:

                        self.widget.depl_pion(
                            self.id_pion,
                            coord_release,
                            color_pion,
                            self.pos_pion_select,
                        )

                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                        self.widget.restor_case_noir()

                        self.lst_depl_pion.append(
                            (
                                self.id_pion,
                                color_pion,
                                0,
                                self.pos_pion_select,
                                coord_release,
                            )
                        )

                        self.verif_creation_dame(self.id_pion, coord_release)

                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                    else:

                        self.widget.depl_pion(
                            self.id_pion,
                            coord_release,
                            color_pion,
                            self.pos_pion_select,
                        )

                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                        self.widget.restor_case_noir()

                        # Fonction pour trouver le pion sauté et
                        # le supprimer de la liste des pion noir ou blanc
                        sup_pion = SuppPion(
                            self.id_pion,
                            self.pos_pion_select,
                            coord_release,
                            self.lst_coord,
                            self.lst_case_possible,
                            self.lst_pn_sup,
                            self.lst_pb_sup,
                        )

                        lst_pion_sup = sup_pion.sup_pion()

                        self.widget.sup_pion(self.id_pion, lst_pion_sup)

                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                        # Enregistrement du déplacement dans un dictionnaire
                        self.lst_depl_pion.append(
                            (
                                self.id_pion,
                                color_pion,
                                1,
                                self.pos_pion_select,
                                coord_release,
                            )
                        )

                        # Vérification si création d'une dame
                        self.verif_creation_dame(self.id_pion, coord_release)

                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                        # Suppression de l'id dans la liste des ids afin
                        # de savoir si le jeu est terminé
                        if (
                            len(self.widget.lst_id_pb) == 0
                            or len(self.widget.lst_id_pn) == 0
                        ):
                            messagebox.showinfo(
                                "Game", "Vous avez gagné le jeux. Bravo !!:"
                            )
                        else:
                            pass

                else:
                    pass

        else:
            pass


# ------------------------- Application ----------------------------------- #
App("Jeu de Dame")
