def meniu_principal():
    """
        Se afiseaza meniul principal.
    """

    print("\nSelectati una dintre optiuniile de mai jos : ")
    print("\t1. Adaugare/Stergere/Modificare rezervare.")
    print("\t2. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.")
    print("\t3. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("\t4. Determinarea prețului maxim pentru fiecare clasă.")
    print("\t5. Ordonarea rezervărilor descrescător după preț.")
    print("\t6. Afișarea sumelor prețurilor pentru fiecare nume.")
    print("\t7. Undo.")
    print("\t8. Redo.")
    print("\t9. Afisarea tuturor rezervarilor.")
    print("\t10. Exit.")


def meniu_op1():
    """
        Se afiseaza meniul de la optiunea 1.
    """

    print("Selectati una dintre optiunile afisate mai jos : ")
    print("\t 1. Adaugare rezervare")
    print("\t 2. Stergere rezervare")
    print("\t 3. Modificare rezervare")
    print("\t 4. Go back")


def optiune():
    """
        Se citeste un intreg de la tastatura.
    """

    try:
        op = int(input("Optiunea dorita : "))

    except ValueError:
        return 100

    return op

