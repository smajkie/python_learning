# nice copy from list to list with while

lista1 = ['jeden', 'dwa', 'trzy']
lista2 = []

while lista1:                   # fajna metoda na petle dopoki cos jest w liscie
    kopiator = lista1.pop()
    lista2.append(kopiator)

print(lista1)
print()
print(*lista2)

while 'dwa' in lista2:
    lista2.remove('dwa')

print(*lista2)