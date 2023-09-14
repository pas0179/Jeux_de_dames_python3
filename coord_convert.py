"""
    Trouver des coordonnées exploitable avec x et y recupéré
    dans la fonction Motion de main
"""


class CoordConvert:
    """Class pour trouver les coordonnées exploitable
    pour la suppression des pions ou dames"""
    def __init__(self, posx, posy, lst_case_noir):
        """Initialisation des attributs"""
        self.pos_x = posx
        self.pos_y = posy
        self.lst_case_noir = lst_case_noir

        self.coord = ()

        self.find_coord()

    def find_coord(self):
        """Fonction qui retourne les coordonnées"""
        for val in self.lst_case_noir:
            if val[0] < self.pos_x < val[2] and val[1] < self.pos_y < val[3]:
                self.coord = val
            else:
                pass
