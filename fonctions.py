# Fonction pour trouver les cases noirs vides

# au début de la partie



def ident_pion_noir_blanc(id):
    pion = ""
    if 100 < id < 121:
        pion = "noir"
    elif 120 < id < 141:
        pion = "blanc"
    elif id > 140:
        pion = "dame"

    return pion


def convert_coord(x, y, lst_case_noir):
    coord = (0, 0, 0, 0)

    for el in lst_case_noir:
        if el[0] < x < el[2] and el[1] < y < el[3]:
            coord = (el[0], el[1], el[0] + 60, el[1] + 60)
        else:
            pass

    return coord


def convert_dict_lst(dict, pos_pion):
    lst_case_possible = []

    if len(dict) > 0:
        for val in dict.values():
            for el in val:
                lst_case_possible.append(el)

        # Nettoyage de la position de départ
        lst_temp = []
        for el in lst_case_possible:
            if el != pos_pion:
                lst_temp.append(el)
            else:
                pass

        lst_case_possible = lst_temp

    else:
        pass

    return lst_case_possible



def depl_pion_bas_gauche(pos_pion_select):
    # Position du pion selectionné
    pos_x, pos_y = pos_pion_select[0], pos_pion_select[1]

    # Valeur de déplacement d'un pion vers le bas
    depl_x, depl_y = 60, 60

    x, y = pos_x - depl_x, pos_y + depl_y

    # Déplacement bas gauche
    depl_b_g = (x, y, x + 60, y + 60)

    return depl_b_g


def depl_pion_bas_droit(pos_pion_select):
    # Position du pion selectionné
    pos_x, pos_y = pos_pion_select[0], pos_pion_select[1]

    # Valeur de déplacement d'un pion vers le bas
    depl_x, depl_y = 60, 60

    x, y = pos_x + depl_x, pos_y + depl_y

    # Déplacement bas droit
    depl_b_d = (x, y, x + 60, y + 60)

    return depl_b_d


def depl_pion_haut_gauche(pos_pion_select):
    # Position du pion selectionné
    pos_x, pos_y = pos_pion_select[0], pos_pion_select[1]

    # Valeur de déplacement d'un pion vers le haut
    depl_x, depl_y = 60, 60

    x, y = pos_x - depl_x, pos_y - depl_y

    # Déplacement haut gauche et droit
    depl_h_g = (x, y, x + 60, y + 60)

    return depl_h_g


def depl_pion_haut_droit(pos_pion_select):
    # Position du pion selectionné
    pos_x, pos_y = pos_pion_select[0], pos_pion_select[1]

    # Valeur de déplacement d'un pion vers le haut
    depl_x, depl_y = 60, 60

    x, y = pos_x + depl_x, pos_y - depl_y

    # Déplacement haut gauche et droit
    depl_h_d = (x, y, x + 60, y + 60)

    return depl_h_d


def saut_bas_g(id, pion_select, lst_case_vide, pos_pn, pos_pb):
    saut = ()
    pn_sup, pb_sup = (), ()
    new_pos = ()

    color_pion = ident_pion_noir_blanc(id)

    depl_bg = depl_pion_bas_gauche(pion_select)

    if color_pion == "noir":
        for el in pos_pb:
            if el[0] == depl_bg[0] and el[1] == depl_bg[1]:
                new_pos = depl_pion_bas_gauche(depl_bg)
            if new_pos in lst_case_vide:
                saut = new_pos
                pb_sup = depl_bg
            else:
                pass

    elif color_pion == "blanc":
        for el in pos_pn:
            if el[0] == depl_bg[0] and el[1] == depl_bg[1]:
                new_pos = depl_pion_bas_gauche(depl_bg)
                if new_pos in lst_case_vide:
                    saut = new_pos
                    pn_sup = depl_bg
                else:
                    pass
    else:
        pass

    return saut, pn_sup, pb_sup


def saut_bas_d(id, pion_select, lst_case_vide, pos_pn, pos_pb):
    saut = ()
    pn_sup, pb_sup = (), ()
    new_pos = ()

    color_pion = ident_pion_noir_blanc(id)

    depl_bd = depl_pion_bas_droit(pion_select)

    if color_pion == "noir":
        for el in pos_pb:
            if el[0] == depl_bd[0] and el[1] == depl_bd[1]:
                new_pos = depl_pion_bas_droit(depl_bd)
            if new_pos in lst_case_vide:
                saut = new_pos
                pb_sup = depl_bd
            else:
                pass
    elif color_pion == "blanc":
        for el in pos_pn:
            if el[0] == depl_bd[0] and el[1] == depl_bd[1]:
                new_pos = depl_pion_bas_droit(depl_bd)
            if new_pos in lst_case_vide:
                saut = new_pos
                pn_sup = depl_bd
            else:
                pass
    else:
        pass

    return saut, pn_sup, pb_sup


def saut_haut_g(id, pion_select, lst_case_vide, pos_pn, pos_pb):
    saut = ()
    pn_sup, pb_sup = (), ()
    new_pos = ()

    color_pion = ident_pion_noir_blanc(id)

    depl_hg = depl_pion_haut_gauche(pion_select)

    if color_pion == "noir":
        for el in pos_pb:
            if el[0] == depl_hg[0] and el[1] == depl_hg[1]:
                new_pos = depl_pion_haut_gauche(depl_hg)
            if new_pos in lst_case_vide:
                saut = new_pos
                pb_sup = depl_hg
            else:
                pass

    elif color_pion == "blanc":
        for el in pos_pn:
            if el[0] == depl_hg[0] and el[1] == depl_hg[1]:
                new_pos = depl_pion_haut_gauche(depl_hg)
                if new_pos in lst_case_vide:
                    saut = new_pos
                    pn_sup = depl_hg
                else:
                    pass
    else:
        pass

    return saut, pn_sup, pb_sup


def saut_haut_d(id, pion_select, lst_case_vide, pos_pn, pos_pb):
    saut = ()
    pn_sup, pb_sup = (), ()
    new_pos = ()

    color_pion = ident_pion_noir_blanc(id)

    depl_hd = depl_pion_haut_droit(pion_select)

    if color_pion == "noir":
        for el in pos_pb:
            if el[0] == depl_hd[0] and el[1] == depl_hd[1]:
                new_pos = depl_pion_haut_droit(depl_hd)
            if new_pos in lst_case_vide:
                saut = new_pos
                pb_sup = depl_hd
            else:
                pass

    elif color_pion == "blanc":
        for el in pos_pn:
            if el[0] == depl_hd[0] and el[1] == depl_hd[1]:
                new_pos = depl_pion_haut_droit(depl_hd)
                if new_pos in lst_case_vide:
                    saut = new_pos
                    pn_sup = depl_hd

                else:
                    pass
    else:
        pass

    return saut, pn_sup, pb_sup
