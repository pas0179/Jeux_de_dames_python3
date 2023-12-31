"""Fichier des fonctions pour les class du jeu de dames"""


def ident_pion_noir_blanc(id_pion):
    """Renvoie la couleur du pion"""
    pion = ""
    if 100 < id_pion < 121:
        pion = "noir"
    elif 120 < id_pion < 141:
        pion = "blanc"
    else:
        pass

    return pion


def convert_coord(x, y, lst_case_noir):
    """Convertit et renvoie les coordonnées du pion"""
    coord = (0, 0, 0, 0)

    for element in lst_case_noir:
        if element[0] < x < element[2] and element[1] < y < element[3]:
            coord = (element[0], element[1], element[0] + 60, element[1] + 60)
        else:
            pass

    return coord


def convert_dict_lst(dict_saut, pos_pion):
    """Convertit un dictionnaire et renvoie une liste"""
    lst_case_possible = []

    if len(dict_saut) > 0:
        for val in dict_saut.values():
            for element in val:
                lst_case_possible.append(element)

        # Nettoyage de la position de départ
        lst_temp = []

        lst_temp = [
            element for element in lst_case_possible if element != pos_pion
        ]

        lst_case_possible = lst_temp

    else:
        pass

    return lst_case_possible


def depl_pion_bas_gauche(pos_pion_select):
    """calcul et revoie la nouvelle position du pion si c'est possible"""
    pos_x, pos_y = pos_pion_select[0], pos_pion_select[1]

    # Valeur de déplacement d'un pion vers le bas
    depl_x, depl_y = 60, 60

    x, y = pos_x - depl_x, pos_y + depl_y

    # Déplacement bas gauche
    depl_b_g = (x, y, x + 60, y + 60)

    return depl_b_g


def depl_pion_bas_droit(pos_pion_select):
    """calcul et revoie la nouvelle position du pion si c'est possible"""
    pos_x, pos_y = pos_pion_select[0], pos_pion_select[1]

    # Valeur de déplacement d'un pion vers le bas
    depl_x, depl_y = 60, 60

    x, y = pos_x + depl_x, pos_y + depl_y

    # Déplacement bas droit
    depl_b_d = (x, y, x + 60, y + 60)

    return depl_b_d


def depl_pion_haut_gauche(pos_pion_select):
    """calcul et revoie la nouvelle position du pion si c'est possible"""
    pos_x, pos_y = pos_pion_select[0], pos_pion_select[1]

    # Valeur de déplacement d'un pion vers le haut
    depl_x, depl_y = 60, 60

    x, y = pos_x - depl_x, pos_y - depl_y

    # Déplacement haut gauche et droit
    depl_h_g = (x, y, x + 60, y + 60)

    return depl_h_g


def depl_pion_haut_droit(pos_pion_select):
    """calcul et revoie la nouvelle position du pion si c'est possible"""
    pos_x, pos_y = pos_pion_select[0], pos_pion_select[1]

    # Valeur de déplacement d'un pion vers le haut
    depl_x, depl_y = 60, 60

    x, y = pos_x + depl_x, pos_y - depl_y

    # Déplacement haut gauche et droit
    depl_h_d = (x, y, x + 60, y + 60)

    return depl_h_d


def saut_bas_g(pion_select, color_pion, lst_case_vide, pos_pn, pos_pb):
    """Calcul et renvoie la nouvelle position d'un pion pour un saut
    si c'est possible"""
    saut = ()
    pn_sup, pb_sup = (), ()
    new_pos = ()

    depl_bg = depl_pion_bas_gauche(pion_select)

    if color_pion == "noir":
        for pos in pos_pb:
            if pos[0] == depl_bg[0] and pos[1] == depl_bg[1]:
                new_pos = depl_pion_bas_gauche(depl_bg)
            if new_pos in lst_case_vide:
                saut = new_pos
                pb_sup = depl_bg
            else:
                pass

    elif color_pion == "blanc":
        for pos in pos_pn:
            if pos[0] == depl_bg[0] and pos[1] == depl_bg[1]:
                new_pos = depl_pion_bas_gauche(depl_bg)
                if new_pos in lst_case_vide:
                    saut = new_pos
                    pn_sup = depl_bg
                else:
                    pass
    else:
        pass

    return saut, pn_sup, pb_sup


def saut_bas_d(pion_select, color_pion, lst_case_vide, pos_pn, pos_pb):
    """Calcul et renvoie la nouvelle position d'un pion pour un saut"""
    saut = ()
    pn_sup, pb_sup = (), ()
    new_pos = ()

    depl_bd = depl_pion_bas_droit(pion_select)

    if color_pion == "noir":
        for pos in pos_pb:
            if pos[0] == depl_bd[0] and pos[1] == depl_bd[1]:
                new_pos = depl_pion_bas_droit(depl_bd)
            if new_pos in lst_case_vide:
                saut = new_pos
                pb_sup = depl_bd
            else:
                pass
    elif color_pion == "blanc":
        for pos in pos_pn:
            if pos[0] == depl_bd[0] and pos[1] == depl_bd[1]:
                new_pos = depl_pion_bas_droit(depl_bd)
            if new_pos in lst_case_vide:
                saut = new_pos
                pn_sup = depl_bd
            else:
                pass
    else:
        pass

    return saut, pn_sup, pb_sup


def saut_haut_g(pion_select, color_pion, lst_case_vide, pos_pn, pos_pb):
    """Calcul et renvoie la nouvelle position d'un pion pour un saut"""
    saut = ()
    pn_sup, pb_sup = (), ()
    new_pos = ()

    depl_hg = depl_pion_haut_gauche(pion_select)

    if color_pion == "noir":
        for pos in pos_pb:
            if pos[0] == depl_hg[0] and pos[1] == depl_hg[1]:
                new_pos = depl_pion_haut_gauche(depl_hg)
            if new_pos in lst_case_vide:
                saut = new_pos
                pb_sup = depl_hg
            else:
                pass

    elif color_pion == "blanc":
        for pos in pos_pn:
            if pos[0] == depl_hg[0] and pos[1] == depl_hg[1]:
                new_pos = depl_pion_haut_gauche(depl_hg)
                if new_pos in lst_case_vide:
                    saut = new_pos
                    pn_sup = depl_hg
                else:
                    pass
    else:
        pass

    return saut, pn_sup, pb_sup


def saut_haut_d(pion_select, color_pion, lst_case_vide, pos_pn, pos_pb):
    """Calcul et renvoie la nouvelle position d'un pion pour un saut"""
    saut = ()
    pn_sup, pb_sup = (), ()
    new_pos = ()

    depl_hd = depl_pion_haut_droit(pion_select)

    if color_pion == "noir":
        for pos in pos_pb:
            if pos[0] == depl_hd[0] and pos[1] == depl_hd[1]:
                new_pos = depl_pion_haut_droit(depl_hd)
            if new_pos in lst_case_vide:
                saut = new_pos
                pb_sup = depl_hd
            else:
                pass

    elif color_pion == "blanc":
        for pos in pos_pn:
            if pos[0] == depl_hd[0] and pos[1] == depl_hd[1]:
                new_pos = depl_pion_haut_droit(depl_hd)
                if new_pos in lst_case_vide:
                    saut = new_pos
                    pn_sup = depl_hd

                else:
                    pass
    else:
        pass

    return saut, pn_sup, pb_sup
