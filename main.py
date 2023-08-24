import tkinter as tk
from tkinter import messagebox

from fonctions import (
    convert_coord,
    convert_dict_lst,
    ident_pion_noir_blanc,
)
from solution_depl import Move
from player import Player
from widget import Widget
from sup_pion import SuppPion
from coord_convert import CoordConvert
from solution_depl_dame_simple import SolDeplDames


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
        color_pion = ident_pion_noir_blanc(id)

        print(f"color_pion : {color_pion}")

        print(f"coord_release : {coord_release}")

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

        # On identifie l'objet selectionné par le clic de souris
        self.id_ps = self.widget.find_id(coord)
        self.id = self.id_ps[0]

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
        if 100 < self.id < 141:
            # # on recupère la couleur du pion selectionné
            color_pion = ident_pion_noir_blanc(self.id)

            # On affecte les coordonnées
            self.pos_pion_select = (
                int(coord_id[0]),
                int(coord_id[1]),
                int(coord_id[0] + 60),
                int(coord_id[1] + 60),
            )

            # On récupère le dictionnaires des déplacements possibles
            self.dict_depl = {}

            sol = Move(
                self.id,
                self.pos_pion_select,
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

            # On regarde a qui le tour sauf si saut
            player = self.player.select_player(
                self.id, self.lst_depl_pion, self.lst_pb_sup, self.lst_pn_sup
            )

            if player == color_pion:
                self.widget.can.itemconfigure(self.id, fill="red", outline="red")

                # Trouver les ids des solutions pour changer la couleur
                # des cases noirs en cases jaunes afin de voir les solutions
                self.lst_ids = []
                if len(self.lst_case_possible) > 0:
                    for val in self.lst_case_possible:
                        id = self.widget.find_id(val)
                        self.lst_ids.append(id[0])

                else:
                    pass

                if len(self.lst_ids) > 0:
                    for el in self.lst_ids:
                        self.widget.can.itemconfigure(
                            el,
                            fill="yellow",
                        )
                else:
                    pass
            else:
                messagebox.showinfo("Erreur", "Ce nest pas a vous de jouer !!!")

        # Si select dame
        elif self.id > 140:
            # On recupère la couleur de la dame
            color_dame = ident_pion_noir_blanc(self.id)

            # On affecte les coordonnées
            self.pos_dame_select = (
                int(coord_id[0]),
                int(coord_id[1]),
                int(coord_id[0] + 60),
                int(coord_id[1] + 60),
            )

            # On récuprère la lise des deplacements possible
            self.dict_depl = {}

            sol_dame = SolDeplDames(self.pos_dame_select, self.lst_case_vide)
            self.dict_depl = sol_dame.solution_depl_dame()

            # On convertie le dictionnaire des solutions en liste de tuples
            self.lst_case_possible = convert_dict_lst(
                self.dict_depl, self.pos_dame_select
            )

            # On va jaunir les cases noirs pour voir les solutions
            self.lst_ids = []
            if len(self.lst_case_possible) > 0:
                for val in self.lst_case_possible:
                    id = self.widget.find_id(val)
                    self.lst_ids.append(id[0])
            else:
                pass

            if len(self.lst_ids) > 0:
                for el in self.lst_ids:
                    self.widget.can.itemconfigure(
                        el,
                        fill="yellow",
                    )
            else:
                pass

            # On regarde a qui le tour
            player = self.player.select_player(
                self.id, self.lst_depl_pion, self.lst_pb_sup, self.lst_pn_sup
            )

            if player != color_dame:
                messagebox.showinfo("Erreur", "Ce n'est pas a vous de jouer !!!")
            else:
                self.widget.can.itemconfigure(self.id, fill="red", outline="red")

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
        if 100 < self.id < 141:
            # On récupère la couleur du pion sélectionné
            color_pion = ident_pion_noir_blanc(self.id)

            if (
                self.pos_pion_select[0] == coord_release[0]
                and self.pos_pion_select[1] == coord_release[1]
            ):
                # Même endroit, on applique la couleur d'origine du pion
                # selectionné. On lance la fonction de restauration
                # des couleurs
                self.widget.restor_pion_ou_dame(self.id, color_pion)
                self.widget.restor_case_noir(self.lst_ids)

            # Relachement du clic sur une autre case
            else:
                # 1- La case de destination n'est pas valide
                if (
                    len(self.lst_case_possible) == 0
                    or coord_release not in self.lst_case_possible
                ):
                    # On lance la fonction "restor_pion"
                    self.widget.restor_pion_ou_dame(self.id, color_pion)
                    # self.widget.restor_case_noir(self.lst_ids)

                # 2- La case de destination est valide
                if coord_release in self.lst_case_possible:
                    # On vérifie si saut ou non
                    if len(self.lst_pb_sup) == 0 and len(self.lst_pn_sup) == 0:
                        # Déplacement simple du pion avec la fonction
                        # depl_pion
                        self.widget.depl_pion(
                            self.id, coord_release, color_pion, self.pos_pion_select
                        )
                        # Maj de la liste des cases vides
                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                        # Restauration des couleurs d'origine
                        # Doit etre desactivé si les cases possibles
                        # Ne sont plus visible en jaune
                        self.widget.restor_case_noir(self.lst_ids)
                        # Enregistrement du déplacement dans une liste
                        # 0: pas de saut, 1: saut d'un pion
                        self.lst_depl_pion.append(
                            (
                                self.id,
                                color_pion,
                                0,
                                self.pos_pion_select,
                                coord_release,
                            )
                        )

                        # Vérification si création d'une dame
                        self.verif_creation_dame(self.id, coord_release)

                    else:
                        # Déplacement du pion selctionné avec un saut
                        self.widget.depl_pion(
                            self.id, coord_release, color_pion, self.pos_pion_select
                        )
                        self.lst_case_vide = self.widget.maj_lst_case_vide()

                        self.widget.restor_case_noir(self.lst_ids)

                        # Fonction pour trouver le pion sauté et
                        # le supprimer de la liste des pion noir ou blanc

                        sup_pion = SuppPion(
                            self.id,
                            self.pos_pion_select,
                            coord_release,
                            self.lst_coord,
                            self.lst_case_possible,
                            self.lst_pn_sup,
                            self.lst_pb_sup,
                        )

                        lst_pion_sup = sup_pion.sup_pion()

                        if len(lst_pion_sup) > 0:
                            self.widget.sup_pion(self.id, lst_pion_sup)
                            # Mise a jour de la liste des cases vides
                            self.lst_case_vide = self.widget.maj_lst_case_vide()
                        else:
                            pass

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

        elif self.id > 140:
            color_dame = self.widget.can.gettags(self.id)
            color_dame = color_dame[0]
            print(f"color_dame : {color_dame}")
            print(f"self.id : {self.id}")

            # Relachement du clic au même endroit
            if (
                self.pos_dame_select[0] == coord_release[0]
                and self.pos_dame_select[1] == coord_release[1]
            ):
                self.widget.restor_pion_ou_dame(self.id, color_dame)

                self.widget.restor_case_noir(self.lst_ids)

            else:
                # La case de destination n'est pas valide
                if (
                    len(self.lst_case_possible) == 0
                    or coord_release not in self.lst_case_possible
                ):
                    # On lance la restoration de la dame
                    self.widget.restor_pion_ou_dame(self.id, color_dame)

                # La case de destination est valide
                else:
                    if coord_release in self.lst_case_possible:
                        # On vérifie si saut ou non
                        pass

        else:
            pass


# ------------------------- Application ----------------------------------- #
App("Jeu de Dame")
