hp = 20
npchp = 30
while True:
    if hp==0:
        print("Zostałeś pokonany Koniec gry")
        break
    if npchp==0:
        print("Zwyciężyłeś! pokonałeś bestię")
        break
    print("Ty:", hp,"Hp", "Potwór:", npchp,"HP")
    decyzja=input("Wybierz akcję: (1. Atak/ 2. leczenie/ 0. Ucieczka)")
    if decyzja == "1":
        npchp-= 6
        print("Zadałeś cios potwór traci 6 hp")
    elif decyzja == "2":
        hp+=8
        print("Wipijasz miksturę leczenia zyskujesz 8 hp")
    elif decyzja == "0":
        print("Uciekasz od walki Koniec gry")
        break
    else:
        print("Nie ma takiej akcji")
        continue
    print("Potwór zadajie cios -5hp")
    hp-=5


