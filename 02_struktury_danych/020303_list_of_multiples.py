def list_of_multiples (num, length):
    wynik = [] * length
    for i in range(1,length+1):
        wynik.append((i)*num)
    return wynik

print(list_of_multiples(12,10))

# indexerror: list assignment index out of range - to sie bierze z tego ze zainicjowana listan ie ma elementu, nie mozna wiec przypisac wartosci do elementu ktory nie istnieje.
# dwa rozwiazania:
# - uzywanie append czyli dopisywania do listy
# - zainicjowanie pustej listy z x iloscia elementow