def main():
    x = {1: 'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery'}
#    y = dict('1' = 'jeden', 2 =='dwa', 3 == 'trzy', 4 == 'cztery') tak sie nie da bo on che przyisywac liczbe do stringa a nie klucz do wartosci
    listuj(x)
#    listuj(y)
    listuj_ladnie(x)
    listuj_inaczej(x)


def listuj(o):
    for i in o:
        print(f'ID:{i} a klucz to {o[i]}')

def listuj_ladnie(o):
    for a, b in o.items():
        print(f'ID:{a} a klucz to {b}')

def listuj_inaczej(o):
    for a in o.keys():
        print(a, end=' ')
    for b in o.values():
        print(b)


if __name__ == '__main__': main()