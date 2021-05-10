from Domain.Getter import *


def set_id(id_nou, rezervare):
    """
    Modifica id-ul din rezervare.
    :param id_nou:
    :param rezervare:
    :return:
    """
    if get_id(rezervare) != id_nou:
        rezervare[0] = id_nou
        return rezervare

    return rezervare


def set_nume(nume_nou, rezervare):
    """
    Se modifica numele rezervarii.
    :param nume_nou:
    :param rezervare:
    :return:
    """
    if get_nume(rezervare) != nume_nou:
        rezervare[1] = nume_nou
        return rezervare

    return rezervare


def set_clasa(clasa_nou, rezervare):
    """
    Se modifica clasa rezervarii.
    :param clasa_nou:
    :param rezervare:
    :return:
    """
    if get_clasa(rezervare) != clasa_nou:
        rezervare[2] = clasa_nou
        return rezervare

    return rezervare


def set_pret(pret_nou, rezervare):
    """
    Se modifica pretul rezervarii.
    :param pret_nou:
    :param rezervare:
    :return:
    """
    if get_pret(rezervare) != pret_nou:
        rezervare[3] = pret_nou
        return rezervare

    return rezervare


def set_chekin(chekin_nou, rezervare):
    """
    Se modifica chekin-ul rezervarii.
    :param chekin_nou:
    :param rezervare:
    :return:
    """
    if get_chekin(rezervare) != chekin_nou:
        rezervare[4] = chekin_nou
        return rezervare

    return rezervare

