def silnia(liczba):
    wynik = 1
    for i in range(1,liczba):
        wynik = wynik + (wynik * i)
    return wynik

cos = silnia(5)
print(cos)
