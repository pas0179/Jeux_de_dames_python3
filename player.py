"""
Class player pour savoir qui doit jouer

"""

class Player:
    def __init__(self):
        self.lst_depl_pion = []

    def select_player(self, id, color_pion, lst_depl_pion, lst_pn_sup, lst_pb_sup):
        self.lst_depl_pion = lst_depl_pion

        player = ""
        old_id = lst_depl_pion[-1][0]
        old_color = lst_depl_pion[-1][1]
        saut = lst_depl_pion[-1][2]

        if color_pion == old_color:
            if old_id == id and saut == 1:
                if color_pion == "noir":
                    if len(lst_pb_sup) > 0:
                        player = "noir"
                    else:
                        player = "blanc"
                if color_pion == "blanc":
                    if len(lst_pn_sup) > 0:
                        player = "blanc"
                    else:
                        player = "noir"
                else:
                    pass
            else:
                pass

        else:
            player = color_pion

        return player
