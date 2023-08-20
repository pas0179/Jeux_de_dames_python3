"""
    Trouver des coordonnées exploitable avec x et y recupéré
    dans la fonction Motion de main 
"""


class CoordConvert:

    def __init__(self, x, y, lst_case_noir):

        self.x = x
        self.y = y 
        self.lst_case_noir = lst_case_noir

        self.coord = ()

        self.find_coord()


    def find_coord(self):

        for val in self.lst_case_noir:
            if val[0] < self.x < val[2] and val[1] < self.y < val[3]:
                self.coord = val
            else:
                pass


        
