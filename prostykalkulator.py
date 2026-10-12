liczba_a = float(input("liczba a: "))
obliczenie= float(input("znak działania: "))
liczba_b = float(input("liczba b: "))
if obliczenie == "+":
        print(liczba_a + liczba_b)
elif liczba_b == 0 and obliczenie == "/":
        print("nie można dzielić przez zero")
elif obliczenie == "-":
        print(liczba_a - liczba_b)
elif obliczenie == "*":
        print(liczba_a * liczba_b)
elif obliczenie == "/":
        print(liczba_a / liczba_b)
elif obliczenie == "^":
        print(liczba_a ** liczba_b)
elif obliczenie == "%":
        print(liczba_a % liczba_b)
else:
        print("błąd znaku i borys odpalił download machine")

