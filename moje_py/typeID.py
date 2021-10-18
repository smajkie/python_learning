x = 1
lista = [1, 'dwa', 3, 'cztery']
tupla = (1, 'dwa', 3, 'cztery')

print(type(lista), 'its ID is:', id(lista), 'but objectIDs are', id(lista[0]), id(lista[1]), id(lista[2]), id(lista[3]))
print(f'{type(tupla)} its ID is: {id(tupla)} but objectsIDs are {id(tupla[0])} {id(tupla[1])} {id(tupla[2])} {id(tupla[3])}')

print(type(x))