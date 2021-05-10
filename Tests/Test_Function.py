from Logic.Function import *


def test_creare_rezervare():
    """
    Testarea unctiei de creare rezervare.
    :return:
    """
    rezervare = creare_rezerare(1, 'Ghita', 'economy_plus', 42.32, 'nu')
    assert rezervare == [1, 'Ghita', 'economy_plus', 42.32, 'nu']


def test_adaugare_rezervare():
    """
    Testarea functiei de adaugare_rezervare.
    :return:
    """
    rezervari = []
    assert len(rezervari) == 0
    rezervare = creare_rezerare(1, 'Ghita', 'economy_plus', 42.32, 'nu')
    rezervari = adaugare_rezervare(rezervare, rezervari)
    assert len(rezervari) == 1
    assert rezervari[0] == [1, 'Ghita', 'economy_plus', 42.32, 'nu']


def test_modificare_rezervare():
    """
    Testarea functiei de modificare_rezervare.
    :return:
    """

    rezervare = creare_rezerare(1, 'Ghita', 'economy_plus', 42.32, 'nu')
    rezervari = [rezervare]
    rezervare_2 = creare_rezerare(2, 'Ghita', 'economy', 25.75, 'nu')
    rezervari.append(rezervare_2)
    assert rezervari[1] == [2, 'Ghita', 'economy', 25.75, 'nu']
    modificare_rezervare(rezervari, 2, [2, 'Ghita Mariss', 'economy', 25.75, 'da'])
    assert rezervari[1] == [2, 'Ghita Mariss', 'economy', 25.75, 'da']


def test_stergere_rezervare():
    """
    Testarea functiei de stergere_rezervare.
    :return:
    """
    rezervare = creare_rezerare(1, 'Iulia Costin', 'economy_plus', 42.32, 'da')
    rezervari = [rezervare]
    rezervare_2 = creare_rezerare(2, 'Ghita Mariss', 'economy', 25.75, 'nu')
    rezervari.append(rezervare_2)
    assert rezervari[0] == [1, 'Iulia Costin', 'economy_plus', 42.32, 'da']
    assert len(rezervari) == 2
    stergere_rezervare(rezervari, 1)
    assert rezervari[0] == [2, 'Ghita Mariss', 'economy', 25.75, 'nu']
    assert len(rezervari) == 1


def test_trecere_clasa_superioara():
    """
    testarea functiei de trecere_clasa_superioara.
    :return:
    """
    rezervari = []
    rezervare = creare_rezerare(1, 'Ghita', 'economy', 42.32, 'nu')
    rezervare_1 = creare_rezerare(2, 'Ghita Anton', 'economy_plus', 42.32, 'nu')
    rezervare_2 = creare_rezerare(3, 'Ghita', 'economy_plus', 42.32, 'nu')
    rezervari = adaugare_rezervare(rezervare, rezervari)
    rezervari = adaugare_rezervare(rezervare_1, rezervari)
    rezervari = adaugare_rezervare(rezervare_2, rezervari)

    assert get_clasa(rezervari[0]) == 'economy'
    assert get_clasa(rezervari[1]) == 'economy_plus'
    assert get_clasa(rezervari[2]) == 'economy_plus'

    rezervari = trecere_clasa_superioara(rezervari, 'Ghita')

    assert get_clasa(rezervari[0]) == 'economy_plus'
    assert get_clasa(rezervari[1]) == 'economy_plus'
    assert get_clasa(rezervari[2]) == 'business'


def test_ieftinire_procentaj():
    """
    Testarea functiei de ieftinire procentaj.
    :return:
    """
    rezervari = []
    rezervare = creare_rezerare(1, 'Ghita', 'economy', 100, 'da')
    rezervare_1 = creare_rezerare(2, 'Ghita Anton', 'economy_plus', 200, 'nu')
    rezervare_2 = creare_rezerare(3, 'Ghita', 'economy_plus', 50, 'da')
    rezervari = adaugare_rezervare(rezervare, rezervari)
    rezervari = adaugare_rezervare(rezervare_1, rezervari)
    rezervari = adaugare_rezervare(rezervare_2, rezervari)

    assert get_pret(rezervari[0]) == 100
    assert get_pret(rezervari[1]) == 200
    assert get_pret(rezervari[2]) == 50

    rezervari = ieftinire_procentaj(rezervari, 10)

    assert get_pret(rezervari[0]) == 90
    assert get_pret(rezervari[1]) == 200
    assert get_pret(rezervari[2]) == 45


def test_det_maxim_pret():
    """
    Testarea functiei de det_maxim_pret
    :return:
    """
    rezervari = []
    rezervare = creare_rezerare(1, 'Ghita', 'economy', 100, 'da')
    rezervare_1 = creare_rezerare(2, 'Ghita Anton', 'economy_plus', 20, 'nu')
    rezervare_2 = creare_rezerare(3, 'Ghita', 'business', 50, 'da')
    rezervare_3 = creare_rezerare(4, 'Ghita', 'economy', 1, 'da')
    rezervare_4 = creare_rezerare(5, 'Ghita Anton', 'economy_plus', 200, 'nu')
    rezervare_5 = creare_rezerare(6, 'Ghita', 'business', 500, 'da')
    rezervari = adaugare_rezervare(rezervare, rezervari)
    rezervari = adaugare_rezervare(rezervare_1, rezervari)
    rezervari = adaugare_rezervare(rezervare_2, rezervari)
    rezervari = adaugare_rezervare(rezervare_3, rezervari)
    rezervari = adaugare_rezervare(rezervare_4, rezervari)
    rezervari = adaugare_rezervare(rezervare_5, rezervari)

    cl = det_pret_maxim(rezervari)

    assert cl[0] == ['economy', 100]
    assert cl[1] == ['economy plus', 200]
    assert cl[2] == ['business', 500]


def test_desc_pret():
    """
    Testarea functiei de descresc_pret.
    :return:
    """
    rezervari = []
    rezervare = creare_rezerare(1, 'Ghita', 'economy', 100, 'da')
    rezervare_1 = creare_rezerare(2, 'Ghita Anton', 'economy_plus', 200, 'nu')
    rezervare_2 = creare_rezerare(3, 'Ghita', 'economy_plus', 50, 'da')
    rezervari = adaugare_rezervare(rezervare, rezervari)
    rezervari = adaugare_rezervare(rezervare_1, rezervari)
    rezervari = adaugare_rezervare(rezervare_2, rezervari)

    rezervari = descresc_pret(rezervari)

    assert rezervari[0] == [2, 'Ghita Anton', 'economy_plus', 200, 'nu']
    assert rezervari[1] == [1, 'Ghita', 'economy', 100, 'da']
    assert rezervari[2] == [3, 'Ghita', 'economy_plus', 50, 'da']


def test_det_suma_per_nume():
    """
    Testarea functiei det_suma_per_nume().
    :return:
    """
    rezervari = []
    rezervare = creare_rezerare(1, 'Ghita', 'economy', 100, 'da')
    rezervare_1 = creare_rezerare(2, 'Ghita Anton', 'economy_plus', 200, 'nu')
    rezervare_2 = creare_rezerare(3, 'Ghita', 'economy_plus', 50, 'da')
    rezervari = adaugare_rezervare(rezervare, rezervari)
    rezervari = adaugare_rezervare(rezervare_1, rezervari)
    rezervari = adaugare_rezervare(rezervare_2, rezervari)

    nume_suma = det_suma_per_nume(rezervari)

    assert nume_suma[0] == ['Ghita', 150]
    assert nume_suma[1] == ['Ghita Anton', 200]


test_creare_rezervare()
test_adaugare_rezervare()
test_modificare_rezervare()
test_stergere_rezervare()
test_trecere_clasa_superioara()
test_ieftinire_procentaj()
test_det_maxim_pret()
test_desc_pret()
test_det_suma_per_nume()
