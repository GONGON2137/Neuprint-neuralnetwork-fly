punkty= int(input("podaj l. punktów: "))
if punkty >= 96:
    print("6")
elif punkty >= 91:
    print("5")
elif punkty >= 76:
    print("4")
elif punkty >= 56:
    print("3")
elif punkty >= 40:
    print("2")
elif punkty >= 0:
    print("1")
elif punkty > 100:
    print("za duża liczba")
else:
    print("borys pobiera fife error")
