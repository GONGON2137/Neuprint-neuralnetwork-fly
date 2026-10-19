print("wszystkie dzielniki")
n=int(input("Podaj liczbę: "))
for d in range(2,n+1):
    if n % d==0:
        print(f"dzielnik: {d}")
        