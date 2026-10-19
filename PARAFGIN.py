
cena = 1
suma = 0
lsp  = -1

while cena > 0:
    cena=int(input("Podaj cenę produktu: "))
    suma = suma+cena
    lsp += 1
print("Suma to: ", suma,"zł")
print(lsp, "to liczba produktów")
print(int(suma/lsp), "To średnia cena produktu")
