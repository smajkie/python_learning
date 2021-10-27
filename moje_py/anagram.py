def anagram(slowo):

    lista=[]
    odwrotna=[]

    for i in slowo:
        lista.append(i)

    for j in slowo[len(slowo)::-1]:
        odwrotna.append(j)

    if lista == odwrotna:
        return True
    else:
        return False

#input = input('Podaj slowo:')


if anagram(input('Podaj')):
    print(f'Tak  to anagram!!!')
else:
    print(f'Slowo ktore podales {anagram}, to nie jest anagram')

