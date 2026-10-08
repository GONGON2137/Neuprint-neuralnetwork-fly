kwota= input("Podaj kwotę: ")
piatki= int(kwota)//5
reszta = int(kwota % 5)
dwojki= int(reszta) //2
reszta2 = int(kwota % 2)
jedynki = int(reszta2) / 1
print("to będzie: ", piatki, dwojki, jedynki)