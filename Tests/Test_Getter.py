from Domain.Getter import *


def test_get_id():
    """
    Se verifica functia get_id.
    """
    rezervare = [1, 'Vlad Cristian', 'economy', 23.45, 'da']
    assert get_id(rezervare) == 1

    rezervare = []
    assert get_id(rezervare) == 0


def test_get_nume():
    """
    Se verifica functia get_nume.
    """
    rezervare = [1, 'Vlad Cristian', 'economy', 23.45, 'da']
    assert get_nume(rezervare) == 'Vlad Cristian'

    rezervare = []
    assert get_nume(rezervare) == 0


def test_get_clasa():
    """
    Se verifica functia get_clasa.
    """
    rezervare = [1, 'Vlad Cristian', 'economy', 23.45, 'da']
    assert get_clasa(rezervare) == 'economy'

    rezervare = []
    assert get_clasa(rezervare) == 0


def test_get_pret():
    """
    Se verifica functia get_pret.
    """
    rezervare = [1, 'Vlad Cristian', 'economy', 23.45, 'da']
    assert get_pret(rezervare) == 23.45

    rezervare = []
    assert get_pret(rezervare) == 0


def test_get_chekin():
    """
    Se verifica functia get_chekin.
    """
    rezervare = [1, 'Vlad Cristian', 'economy', 23.45, 'da']
    assert get_chekin(rezervare) == 'da'

    rezervare = []
    assert get_chekin(rezervare) == 0


test_get_id()
test_get_nume()
test_get_clasa()
test_get_pret()
test_get_chekin()
