def pierwsza(liczba):           # function calculating prime for given number
    if liczba <= 1:
        return False
    for x in range(2, liczba):
        if liczba % x == 0:             # reszta z dzielenia (modulo)
 #           z = print('nie jest')      # ten print bedzie tylko raz bo wejdzie tu tylko wtedy gdy reszta modulo bedzie 0 i wtedy od razu jest wyjscie z funkcji returnem
            return False
    else:                               # ten else jest do for, jak byl do if to bylo zle!!!
 #           print('jest')
            return True

def pierwsza_lista(y=100):
    for j in range(y):
        if pierwsza(j):
            print(f'{j}', end=' ', flush=True)

pierwsza_lista()
print()
pierwsza_lista(1000)
