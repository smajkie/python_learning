x = True

lista = [1, 2, True, 'lala', 5, False, 'tadammmm', 6, 11]
def change_types(lista):
    for x in range(len(lista)):
        if (isinstance(lista[x], bool) == True and isinstance(lista[x], int) == True):
            lista[x] = not lista[x]
        elif (isinstance(lista[x], int) == True and isinstance(lista[x], bool) == False):
            if lista[x] % 2 == 0:
                lista[x] = lista[x] + 1
        elif isinstance(lista[x], str):
            lista[x] =  (lista[x]+'s').capitalize()
    return(lista)

for x in lista:
    print(x, end=' ')
print()
change_types(lista)
for x in lista:
    print(x, end=' ')

# print(isinstance(x, int))