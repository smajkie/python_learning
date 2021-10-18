slownik = {
    'klucz1': 'jedynka',
    'klucz2': 'dwojka',
    'klucz3': 'trojka',
    'klucz4': 'czworka',
    'klucz5': 'czworka',
}

for key, value in slownik.items():              # tu nie moze byc tylko 'slownik'
    print(f'Klucz {key} ma wartosc {value}')

for key in slownik.keys():                      # it can be just 'for key in slownik'
    print(f'Ten slownik ma takie klucze jak: {key}')

for value in slownik.values():                      # it can be just 'for key in slownik'
    print(f'Ten slownik ma takie wartosci jak: {value}')

for value in set(slownik.values()):                      # it can be just 'for key in slownik'
    print(f'Ten slownik ma takie unikalne wartosci jak: {value}')

print(slownik['klucz1'])
print(slownik.get('klucz5', 'Nie ma'))          # nice mthod to print something if the key is not found, default is 'None'