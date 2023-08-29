import tkinter as tk
from tkinter import messagebox

from fonctions import (
    convert_coord,
    convert_dict_lst,
)
from solution_depl import Move
from player import Player
from widget import Widget
from sup_pion import SuppPion
from coord_convert import CoordConvert
from solution_depl_dame_base import SolDeplDames
# from solution_depl_dame import DeplDame


class App:
    def __init__(self, title):
        self.fen = tk.Tk()

        self.fen.title(title)
        self.fen.geometry("750x610")
        self.fen.minsize(750, 610)
        self.fen.maxsize(750, 610)
        self.fen.config(bg="black")

        # Listes pour le programme
        self.lst_case_vide = []
        self.lst_tour = []

        self.lst_case_possible = []
        self.dict_case_possible = {}

        self.lst_pb_sup = []
        self.lst_pn_sup = []

        self.lst_pion_noir_sup = []
        self.lst_pion_blanc_sup = []

        self.lst_depl_pion = []

        self.id_ps = []

        self.dict_saut = {}
        self.compteur = 0

        # Tuple pour la position du pion noir ou blanc sélectionné
        self.pn_select = (0, 0)
        self.pb_select = (0, 0)

        self.lst_ids = []
        self.lst_coord = []

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
        key = event.keysym
        if key == "q" or key == "Escape":
            self.fen.destroy()
            self.fen.quit()

    def move_mouse(self, event):
        x, y = event.x, event.y
        convert_coord = CoordConvert(x, y, self.widget.lst_cases_noir)
        coord = convert_coord.coord

        self.lst_coord.append(coord)

    def verif_creation_dame(self, id, coord_release):
        """on vérifie d'abord si le pion noir ou blanc
        est sur la case de création d'une dame"""
        color_pion = self.widget.find_color(id)

        if color_pion == "noir" and (
            coord_release[1] >= 540 and coord_release[3] >= 540
        ):
            """
            On supprime la pos et l'id dans les listes respective

            """
            self.widget.can.delete(id)
            self.widget.lst_pos_pn.remove(coord_release)
            self.widget.lst_id_pn.remove(id)

            """
            Création de la dame noir avec create_dame_noir
            """
            self.widget.create_dame_noir(coord_release[0], coord_release[1])

        elif color_pion == "blanc" and (
            coord_release[1] <= 60 and coord_release[3] <= 60
        ):
            self.widget.can.delete(id)
            self.widget.lst_pos_pb.remove(coord_release)
            self.widget.lst_id_pb.remove(id)

            # Création de la dame create_dame_blanche
            self.widget.create_dame_blanche(coord_release[0], coord_release[1])

        else:
            pass

    def select_pion(self, event):
        x, y = event.x, event.y

        coord = (x, y)

        self.lst_coord = []

        """
        Mise a jour de la liste des cases vides avant de commencer les calculs

        """
        self.lst_case_vide = self.widget.maj_lst_case_vide()

        # On identifie l'objet selectionné par le clic de souris
        self.id = self.widget.find_id(coord)

        #   On récupère les coordonnées de l'objet selectionné
        coord_id = self.widget.can.coords(self.id)
        # Modif des coordonnées
        coord_id = [
            coord_id[0] - 5,
            coord_id[1] - 5,
            coord_id[2] + 5,
            coord_id[3] + 5,
        ]

        # On vérifie que c'est bien un pion qui est selectionné
        """ Vérification que c'est bien un pion qui est sélectionné et non
        une case noir ou une dame """
        if 100 < self.id < 141:
            # # on recupère la couleur du pion selectionné
            color_pion = self.widget.find_color(self.id)

            # On regarde a qui le tour sauf si saut
            player = self.player.select_player(
                self.id,
                color_pion,
                self.lst_depl_pion,
                self.lst_pb_sup,
                self.lst_pn_sup,
            )

            """ Vérification de la couleur du pion sélectionné par rapport
            a la couleur du pion qui doit jouer """
            if player == color_pion:
                """On applique la couleur rouge sur le pion sélectionné"""
                self.widget.can.itemconfigure(self.id, fill="red", outline="red")

                """ Ajout dans le tuple des valeurs x+60 et y+60 """
                self.pos_pion_select = (
                    int(coord_id[0]),
                    int(coord_id[1]),
                    int(coord_id[0] + 60),
                    int(coord_id[1] + 60),
                )

                """ Récuperation du dictionnaire des déplacements possibles """
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

                """
                On va jaunir les cases noirs pour voir les solutions
                avec la méthode color_case_possible dans la class Widget 

                """

                self.widget.color_case_possible(self.lst_case_possible)

            else:
                messagebox.showinfo("Erreur", "Ce nest pas a vous de jouer !!!")

        # Si select dame
        elif self.id > 140:
            # On recupère la couleur de la dame
            color_dame = self.widget.find_color(self.id)

            player = self.player.select_player(
                self.id,
                color_dame,
                self.lst_depl_pion,
                self.lst_pb_sup,
                self.lst_pn_sup,
            )

            if player == color_dame:
                self.widget.can.itemconfigure(self.id, fill="red", outline="red")

                # On affecte les coordonnées
                self.pos_pion_select = (
                    int(coord_id[0]),
                    int(coord_id[1]),
                    int(coord_id[0] + 60),
                    int(coord_id[1] + 60),
                )

                # On récuprère la lise des deplacements possible
                print(f"self.lst_case_possible : {self.lst_case_possible}")
                print(f"lst_pn_sup : {self.lst_pn_sup}")
                print(f"lst_pb_sup : {self.lst_pb_sup}")
                #
                self.widget.color_case_possible(self.lst_case_possible)

            else:
                messagebox.showinfo("Erreur", "Ce n'est pas a vous de jouer !!!")
        else:
            self.id = 0

    def release_pion(self, event):
        # On récupère les coordonnées x, y du bouton relaché
        x, y = event.x, event.y
        # x=98, y=275
        # On convertie x et y en coordonnées lisible
        coord_release = convert_coord(x, y, self.widget.lst_cases_noir)

        # 1- Relachement du clic au même endroit sur un pion
        # On vérifie que c'est bien un pion qui a été sélectionné
        # if 100 < self.id < 141:
        if self.id > 100:
            # C'est un pion
            # On récupère la couleur du pion sélectionné
            color_pion = self.widget.find_color(self.id)
            # color_pion = ident_pion_noir_blanc(self.id)

            if (
                self.pos_pion_select[0] == coord_release[0]
                and self.pos_pion_select[1] == coord_release[1]
            ):
                """
                Le pion reste sur la même case
                - On relance la fonction de restauration des couleurs du pion
                - On relance la fonction de restauration des cases noirs
                    suite au case jaunes

                """

                self.widget.restor_pion_ou_dame(self.id, color_pion)

                self.widget.restor_case_noir()

            # Relachement du clic sur une autre case
            else:
                if (
                    len(self.lst_case_possible) == 0
                    or coord_release not in self.lst_case_possible
                ):
                    """
                    La case de destination n'est pas valide
                    - On relance la fonction de restauration des couleurs du pion
                    - On relance la fonction de restauration des cases noirs

                    """

                    self.widget.restor_pion_ou_dame(self.id, color_pion)

                    self.widget.restor_case_noir()

                if coord_release in self.lst_case_possible:
                    """
                    La case de déstination est valide
                    - Vérification si deplacement simple
                    """
                    if len(self.lst_pb_sup) == 0 and len(self.lst_pn_sup) == 0:
                        """Deplacement simple"""

                        self.widget.depl_pion(
                            self.id, coord_release, color_pion, self.pos_pion_select
                        )

                        """ Mise a jour de la liste des cases vides """

                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                        """ restoration des cases jaunes en noir"""

                        self.widget.restor_case_noir()

                        """ 
                        Enregistrement du deplacement dans une liste qui sert a Player
                        0: pas de saut, 1: saut d'un pion

                        """
                        self.lst_depl_pion.append(
                            (
                                self.id,
                                color_pion,
                                0,
                                self.pos_pion_select,
                                coord_release,
                            )
                        )

                        """ 
                        Verification si le pion est sur une case pour 
                        creation d'une dame 
                        """
                        self.verif_creation_dame(self.id, coord_release)

                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                    else:
                        """Saut simple ou multiple"""

                        self.widget.depl_pion(
                            self.id, coord_release, color_pion, self.pos_pion_select
                        )

                        """ Mise a jour de la liste des cases vides """
                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                        """ Restauration des cases jaunes en noir """
                        self.widget.restor_case_noir()

                        # Fonction pour trouver le pion sauté et
                        # le supprimer de la liste des pion noir ou blanc
                        """"
                        Appel a la class SuppPion du fichier 'supp_pion.py'
                        pour supprimer les pions sautés 
                           
                        """
                        sup_pion = SuppPion(
                            self.id,
                            self.pos_pion_select,
                            coord_release,
                            self.lst_coord,
                            self.lst_case_possible,
                            self.lst_pn_sup,
                            self.lst_pb_sup,
                        )

                        """ Récuperation de la liste des pions a supprimer """
                        lst_pion_sup = sup_pion.sup_pion()

                        """ 
                        Suppression des pions sautés avec la methode sup_pion 
                        de la class Widget 

                        """
                        self.widget.sup_pion(self.id, lst_pion_sup)

                        """ 
                        Mise a jour des la liste des cases vides 
                        """
                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                        # Enregistrement du déplacement dans un dictionnaire
                        self.lst_depl_pion.append(
                            (
                                self.id,
                                color_pion,
                                1,
                                self.pos_pion_select,
                                coord_release,
                            )
                        )

                        # Vérification si création d'une dame
                        self.verif_creation_dame(self.id, coord_release)

                        """
                        Mise a jour de la liste des cases vides au cas ou une dame 
                        serait créer
                        """
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

        # elif self.id > 140:
        #     color_dame = self.widget.can.gettags(self.id)
        #     color_dame = color_dame[0]
        #
        #     # Relachement du clic au même endroit
        #     if (
        #         self.pos_dame_select[0] == coord_release[0]
        #         and self.pos_dame_select[1] == coord_release[1]
        #     ):
        #         self.widget.restor_pion_ou_dame(self.id, color_dame)
        #
        #         self.widget.restor_case_noir()
        #
        #     else:
        #         # La case de destination n'est pas valide
        #         if (
        #             len(self.lst_case_possible) == 0
        #             or coord_release not in self.lst_case_possible
        #         ):
        #             # On lance la restoration de la dame
        #             self.widget.restor_pion_ou_dame(self.id, color_dame)
        #
        #         # La case de destination est valide
        #         else:
        #             if coord_release in self.lst_case_possible:
        #                 # On vérifie si saut ou non
        #                 pass

        else:
            pass


# ------------------------- Application ----------------------------------- #
App("Jeu de Dame")
