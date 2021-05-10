"""
    Scrieți  un  program  pentru  gestionarea rezervărilor  unei  companii  aeriene.

    Vor   fi suportate operațiile:

    1.Adăugare / ștergere / modificare rezervare: se efectuează pe bază de număr de rezervare /  ID.
    O  rezervare conține: ID, nume, clasa  (economy,  economy  plus, business), preț,checkin făcut (da / nu).

    2.Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.

    3.Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.

    4.Determinarea prețului maxim pentru fiecare clasă.

    5.Ordonarea rezervărilor descrescător după preț.

    6.Afișarea sumelor prețurilor pentru fiecare nume.

    7.Undo.
"""
from Tests.Test_Function import *
from Tests.Test_Getter import *
from Tests.Test_Setter import *
from User_Interface.Meniu import *
from User_Interface.CLI import *
from Domain.Getter import *
from Domain.Setter import *
from copy import deepcopy


def main():
    rezervari = []
    rezervari_undo = []
    rezervari_redo = []
    #rezervari = comanda_linie()
    comanda = 0

    while comanda != 10:
        try:
            meniu_principal()
            comanda = optiune()

            if comanda == 1:
                while comanda != 4:
                    meniu_op1()
                    comanda = optiune()
                    if comanda == 1:
                        rezervari_undo.append(deepcopy(rezervari))
                        rezervari_redo = []
                        id = int(input("ID : "))
                        nume = input("Nume : ")
                        clasa = input("Clasa : ")
                        pret = float(input("Pret : "))
                        chekin = 'nu'
                        rezervare = creare_rezerare(id, nume, clasa, pret, chekin)
                        rezervari = adaugare_rezervare(rezervare, rezervari)
                    elif comanda == 2:
                        rezervari_undo.append(deepcopy(rezervari))
                        rezervari_redo = []
                        id = int(input("ID-ul rezervarii pentru care se face stergerea : "))
                        rezervari = stergere_rezervare(rezervari, id)
                    elif comanda == 3:
                        rezervari_undo.append(deepcopy(rezervari))
                        rezervari_redo = []
                        id_bun = int(input("ID-ul rezervarii pentru care se face modificarea : "))
                        print("\nNoua rezervare va avea : \n")
                        id = int(input("ID : "))
                        nume = input("Nume : ")
                        clasa = input("Clasa : ")
                        pret = float(input("Pret : "))
                        chekin = input("Checkin : ")
                        rezervare = creare_rezerare(id, nume, clasa, pret, chekin)
                        rezervari = modificare_rezervare(rezervari, id_bun, rezervare)
                    elif comanda == 4:
                        print("Back.")
                    else:
                        print("Comanda introdusa nu exista.")
            elif comanda == 2:
                rezervari_undo.append(deepcopy(rezervari))
                rezervari_redo = []
                nume = input("Numele pentru care se face trecere la clasa superioara : ")
                rezervari = trecere_clasa_superioara(rezervari, nume)
            elif comanda == 3:
                rezervari_undo.append(deepcopy(rezervari))
                rezervari_redo = []
                proc = int(input("Cu cat la suta se se ieftineasca preturile : "))
                rezervari = ieftinire_procentaj(rezervari, proc)
            elif comanda == 4:
                cl = det_pret_maxim(rezervari)
                for i in range(len(cl)):
                    print("Clasa : ", cl[i][0], " Pret maxim : ", cl[i][1])
            elif comanda == 5:
                rezervari_undo.append(deepcopy(rezervari))
                rezervari_redo = []
                rezervari = descresc_pret(rezervari)
                print("Au fost ordonate!\n")
            elif comanda == 6:
                nume_sum = det_suma_per_nume(rezervari)
                for i in range(len(nume_sum)):
                    print("Nume : ", nume_sum[i][0], "  Suma : ", nume_sum[i][1])
            elif comanda == 7:
                if verif_undo(rezervari_undo):
                    rezervari_redo.append(deepcopy(rezervari))
                    rezervari = rezervari_undo[len(rezervari_undo)-1]
                    rezervari_undo.pop(len(rezervari_undo)-1)
            elif comanda == 8:
                if verif_redo(rezervari_redo):
                    rezervari_undo.append(deepcopy(rezervari))
                    rezervari = rezervari_redo[len(rezervari_redo)-1]
                    rezervari_redo.pop(len(rezervari_redo)-1)
            elif comanda == 9:
                afisare_rezervare(rezervari)
            else:
                print("Nu exista comanda")
        except ValueError as e:
            print(str(e))


main()