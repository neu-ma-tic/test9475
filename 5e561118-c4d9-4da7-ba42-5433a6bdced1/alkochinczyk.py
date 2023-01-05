import random
import os
path = os.getcwd()
filename = path+"\\zadania.txt"


def start():
    def gra():
        for x in range(0, gracze):
            input(nicki[x] + " twoj ruch")
            kostka = random.randint(1, 6)
            print("Wyrzuciles " + str(kostka) + " oczek")
            oczka[x] += kostka
            if oczka[x] >= 69:
                print("Koniec gry, wygral " + nicki[x] + "!\n\n")
                if input("Chcesz zagrac jeszcze raz? y/n\n") == "y":
                    start()
                else:
                    quit()

            print(zadania[oczka[x]-1])
            if zadania[oczka[x]-1] == '13. Pijesz i kazesz komus isc na pole 10':
                for i in range(0, gracze):
                    print(nicki[i] + ": " + str(oczka[i]))
                for x in range(0, gracze):
                    print(str(x+1) +". " +nicki[x])
                wybor = int(input("Wpisz cyfre gracza: "))
                oczka[wybor-1] = 10
            elif zadania[oczka[x]-1] == '16. Zamieniasz sie z graczem ktory byl na najdalszym polu i oboje pijecie':
                max = 0
                for y in range(0, gracze):
                    if oczka[y] >= oczka[max]:
                        max = y
                oczka[x], oczka[max] = oczka[max], oczka[x]
            elif zadania[oczka[x]-1] == '43. Pijesz i wracasz na start':
                oczka[x] = 0
            elif zadania[oczka[x]-1] == '45. Idziesz na pole 9 i pijesz 1x':
                oczka[x] = 9
            elif zadania[oczka[x]-1] == '46. Cofasz sie o 6 pol':
                oczka[x] -= 6
                if oczka[x] < 0:
                    oczka[x] = 0
            elif zadania[oczka[x]-1] == '56. Niefart, wracasz na start i pijesz 3x':
                oczka[x] = 0
            elif zadania[oczka[x]-1] == '63. Wszyscy cofaja sie o 1 pole':
                for i in range(0,gracze):
                    oczka[i] -= 1
            elif zadania[oczka[x]-1] == '12. Cofasz wybrana osobe na start':
                for i in range(0, gracze):
                    print(nicki[i] + ": " + str(oczka[i]))
                for x in range(0, gracze):
                    print(str(x+1) +". " +nicki[x])
                wybor = int(input("Wpisz cyfre gracza: "))
                oczka[wybor-1] = 0

            for x in range(0, gracze):
                print(nicki[x] + ": " + str(oczka[x]))
        gra()



    gracze = int(input("Podaj liczbe graczy: "))
    nicki = []
    file = open(filename, "r")
    zadania = file.readlines()
    oczka = []
    for x in range(0, gracze):
            nick = input("Podaj nazwe gracza: ")
            nicki.append(nick)
            oczka.append(0)
    tryb = input("1. Wersja oryginalna\n2. Mieszana ")
    if tryb != "1":
        zadania = random.sample(zadania, 69)
        file.close()
    gra()


start()

