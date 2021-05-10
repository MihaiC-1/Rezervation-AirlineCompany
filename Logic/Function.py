from Domain.Setter import *


def creare_rezerare(id, nume, clasa, pret, chekin):
    """
    Se creeaza o noua rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: long
    :param chekin: string
    :return: lista ce reprezinta o rezervare
    """

    try:
        if id != int(id):
            raise ValueError("Eroare la id!")
        if nume == '':
            raise ValueError("Eroare la nume")
        if clasa not in ['economy', 'economy_plus', 'business']:
            raise ValueError("Eroare la clasa. Ea trebuie sa fie : economy / economy plus / business!")
        if pret != float(pret):
            raise ValueError("Eroare la pret!")
        if chekin not in ['da', 'nu']:
            raise ValueError("Eroare checkin!")
    except ValueError as e:
        raise ValueError(e)

    return [id, nume, clasa, pret, chekin]


def adaugare_rezervare(rezervare, rezervari):
    """
    Adauga o rezervare la lista de rezervari
    :return:
    """

    for index in range(len(rezervari)):
        if int(rezervare[0]) == get_id(rezervari[index]):
            raise ValueError("Exista deja o rezervare cu acest id.")

    rezervare = set_id(int(rezervare[0]), rezervare)
    rezervare = set_pret(float(rezervare[3]), rezervare)

    rezervari.append(rezervare)

    return rezervari


def afisare_rezervare(rezervari):
    """
    Se face afisarea unei rezervari
    :param rezervari:
    :return:
    """

    for i in range(len(rezervari)):
        print("ID : ", get_id(rezervari[i]), ", Nume : ", get_nume(rezervari[i]), ", Clasa : ", get_clasa(rezervari[i]),
              ", Pret : ", get_pret(rezervari[i]), ", Checkin : ", get_chekin(rezervari[i]), "\n")


def modificare_rezervare(rezervari, id, rezervare_noua):
    """
    Modificarea unei rezervari existente.
    :param rezervari:
    :param id:
    :param rezervare_noua:
    :return:
    """
    count = 0
    for index in range(len(rezervari)):
        if id != get_id(rezervari[index]):
            count += 1
    if count == len(rezervari):
        raise ValueError("Nu exista rezervare cu acest id.")

    i = 0
    while get_id(rezervari[i]) != id:
        i += 1

    set_id(get_id(rezervare_noua), rezervari[i])
    set_nume(get_nume(rezervare_noua), rezervari[i])
    set_clasa(get_clasa(rezervare_noua), rezervari[i])
    set_pret(get_pret(rezervare_noua), rezervari[i])
    set_chekin(get_chekin(rezervare_noua), rezervari[i])

    return rezervari


def stergere_rezervare(rezervari, id):
    """
    Se face eliminarea unei rezervari din lista de rezervari.
    :param rezervari:
    :param id:
    :return:
    """

    count = 0
    for index in range(len(rezervari)):
        if id != get_id(rezervari[index]):
            count += 1
    if count == len(rezervari):
        raise ValueError("Nu exista rezervare cu acest id.")

    for i in range(len(rezervari)):
        if get_id(rezervari[i]) == id:
            rezervari.pop(i)
            break

    return rezervari


def trecere_clasa_superioara(rezervari, nume):
    """
    Se iau toate rezervarile de la un nume citit si se trec intr-o clasa superioara.
    :param rezervari:
    :param nume:
    :return:
    """

    count = 0
    for index in range(len(rezervari)):
        if nume != get_nume(rezervari[index]):
            count += 1
    if count == len(rezervari):
        raise ValueError("Nu exista rezervare cu acest nume.")

    for index in range(len(rezervari)):
        if nume == get_nume(rezervari[index]):
            if get_clasa(rezervari[index]) == 'economy':
                rez = rezervari[index]
                rez = set_clasa('economy_plus', rez)
                rezervari = modificare_rezervare(rezervari, get_id(rezervari[index]), rez)
            elif get_clasa(rezervari[index]) == 'economy_plus':
                rez = rezervari[index]
                rez = set_clasa('business', rez)
                rezervari = modificare_rezervare(rezervari, get_id(rezervari[index]), rez)

    return rezervari


def ieftinire_procentaj(rezervari, proc):
    """
    Se ieftinesc toate rezervarile ce au un chekin facut cu un procentaj
    :return:
    """

    for i in range(len(rezervari)):
        if get_chekin(rezervari[i]) == 'da':
            calc_proc = float(proc * get_pret(rezervari[i]) / 100)
            nou = rezervari[i]
            nou = set_pret(get_pret(nou) - calc_proc, nou)
            rezervari = modificare_rezervare(rezervari, get_id(rezervari[i]), nou)

    return rezervari


def det_pret_maxim(rezervari):
    """
    Se determina pretul maxim pentru fiecare clasa.
    :param rezervari:
    :return:
    """

    clase = [['economy', 0.0], ['economy plus', 0.0], ['business', 0.0]]

    for i in range(len(rezervari)):
        if get_clasa(rezervari[i]) == 'economy':
            if get_pret(rezervari[i]) > clase[0][1]:
                clase[0][1] = get_pret(rezervari[i])
        elif get_clasa(rezervari[i]) == 'economy_plus':
            if get_pret(rezervari[i]) > clase[1][1]:
                clase[1][1] = get_pret(rezervari[i])
        elif get_clasa(rezervari[i]) == 'business':
            if get_pret(rezervari[i]) > clase[2][1]:
                clase[2][1] = get_pret(rezervari[i])

    return clase


def interschimba(rezervari, i, j):
    """
    Inteschimba doua rezervari din lista.
    :param rezervari:
    :param i:
    :param j:
    :return:
    """
    cop_rezervari = []

    for k in range(len(rezervari)):
        if k == i:
            cop_rezervari.append(rezervari[j])
        elif k == j:
            cop_rezervari.append(rezervari[i])
        else:
            cop_rezervari.append(rezervari[k])

    return cop_rezervari


def descresc_pret(rezervari):
    """
    Ordoneaza toata rezervarile descrescator dupa pret.
    :param rezervari:
    :return:
    """

    for i in range(len(rezervari)-1):
        for j in range(i+1, len(rezervari)):
            if get_pret(rezervari[i]) < get_pret(rezervari[j]):
                rezervari = interschimba(rezervari, i, j)

    return rezervari


def det_suma_per_nume(rezervari):
    """
    Determinarea sumelor preturilor pentru fiecare nume din rezervari
    :param rezervari:
    :return:
    """

    nume_suma = []

    for i in range(len(rezervari)):
        if len(nume_suma) == 0:
            nume_suma.append([get_nume(rezervari[i]), get_pret(rezervari[i])])
        else:
            ok = True
            for j in range(len(nume_suma)):
                if nume_suma[j][0] == get_nume(rezervari[i]):
                    nume_suma[j][1] += get_pret(rezervari[i])
                    ok = False
            if ok:
                nume_suma.append([get_nume(rezervari[i]), get_pret(rezervari[i])])

    return nume_suma


def verif_undo(rezervari):
    """
    Verifica daca mai poate face un undo
    :param rezervari:
    :return:
    """

    if len(rezervari) == 0:
        raise ValueError("Lista a ajuns in forma initiala.")

    return True


def verif_redo(rezervari):
    """
    Verifica daca se mai poate face redo.
    :param rezervari:
    :return:
    """
    if len(rezervari) == 0:
        raise ValueError("Nu se mai poate face redo.")

    return True
