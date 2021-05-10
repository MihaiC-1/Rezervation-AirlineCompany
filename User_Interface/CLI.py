from Logic.Function import *


def comanda_linie():
    """
    Se citeste optiune dorita.

    """

    rezervari = []
    print("Scrie-ti 'help' pentru ajutor.")
    optiuni = input("Command line: ")
    while optiuni != 'stop':
        try:
            lista = optiuni.split(" ")
            if lista[len(lista) - 1] == '':
                lista.pop(len(lista) - 1)
        except ValueError:
            print("Nu a fost scrisa bine o comada! Scrieti 'help' pentru ajutor!")
        index = 0

        while index < len(lista):
            try:
                if lista[index] == 'add':
                    rezervari = adaugare_rezervare(lista[index + 1:index + 6], rezervari)
                    index = index + 6
                elif lista[index] == 'del':
                    rezervari = stergere_rezervare(rezervari, int(lista[index + 1]))

                elif lista[index] == 'mod':
                    rezervari = modificare_rezervare(rezervari, int(lista[index+1]), lista[index+2:index+7])
                    index = index + 7
                elif lista[index] == 'ord':
                    rezervari = descresc_pret(rezervari)
                    index = index + 1
                elif lista[index] == 'af':
                    afisare_rezervare(rezervari)
                    index = index + 1
                else:
                    print("Nu este corecta comanda data")
                    index = index + 1
            except ValueError as e:
                print(str(e))
                index += 1
        optiuni = input("Command line: ")
    return rezervari
