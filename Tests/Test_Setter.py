from Domain.Setter import *


def test_set_id():
    """
    Se verifica functia  set_id.
    """
    rezervare = [1, 'Vlad Cristian', 'economy', 23.45, 'da']
    assert get_id(rezervare) == 1

    set_id(2, rezervare)
    assert get_id(rezervare) == 2


def test_set_nume():
    """
    Se verifica functia  set_nume.
    """
    rezervare = [1, 'Vlad Cristian', 'economy', 23.45, 'da']
    assert get_nume(rezervare) == 'Vlad Cristian'

    set_nume('Tudor Prut', rezervare)
    assert get_nume(rezervare) == 'Tudor Prut'


def test_set_clasa():
    """
    Se verifica functia  set_clasa.
    """
    rezervare = [1, 'Vlad Cristian', 'economy', 23.45, 'da']
    assert get_clasa(rezervare) == 'economy'

    set_clasa('economy plus', rezervare)
    assert get_clasa(rezervare) == 'economy plus'


def test_set_pret():
    """
    Se verifica functia  set_pret.
    """
    rezervare = [1, 'Vlad Cristian', 'economy', 23.45, 'da']
    assert get_pret(rezervare) == 23.45

    set_pret(32.29, rezervare)
    assert get_pret(rezervare) == 32.29


def test_set_chekin():
    """
    Se verifica functia  set_chekin.
    """
    rezervare = [1, 'Vlad Cristian', 'economy', 23.45, 'da']
    assert get_chekin(rezervare) == 'da'

    set_chekin('nu', rezervare)
    assert get_id(rezervare) == 'nu'


if __name__ == "__name__":
    test_set_id()
    test_set_nume()
    test_set_clasa()
    test_set_pret()
    test_set_chekin()
