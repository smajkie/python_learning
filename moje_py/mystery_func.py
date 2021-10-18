def mystery_func(num):
    x = list(map(int, str(num)))
    wynik = 1
    for i in range(1, len(x)+1):
        wynik = wynik * x[i-1]
    return wynik

print(mystery_func(133))