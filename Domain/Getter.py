def get_id(rezervare):
    """
    Returneaza id-ul rezervarii.
    :param rezervare:
    :return:
    """
    if len(rezervare) == 0:
        return 0
    return rezervare[0]


def get_nume(rezervare):
    """
    Returneaza numele rezervarii.
    :param rezervare:
    :return:
    """
    if len(rezervare) == 0:
        return 0
    return rezervare[1]


def get_clasa(rezervare):
    """
    Returneaza clasa rezervarii.
    :param rezervare:
    :return:
    """
    if len(rezervare) == 0:
        return 0
    return rezervare[2]


def get_pret(rezervare):
    """
    Returneaza pretul rezervarii.
    :param rezervare:
    :return:
    """
    if len(rezervare) == 0:
        return 0
    return rezervare[3]


def get_chekin(rezervare):
    """
    Returneaza chekin-ul rezervarii
    :param rezervare:
    :return:
    """
    if len(rezervare) == 0:
        return 0
    return rezervare[4]

