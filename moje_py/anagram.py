def anagram(slowo):

    #error check
    errors = False
    for znak in slowo:
        if znak == ' ':
            print(f'Podany ciag znakow zawiera spacje, usun to!')
            errors = True
        else:
            continue
    if errors == False:
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


if anagram(input('Podaj slowo: ')):
    print(f'Tak to slowo to anagram!!!')
else:
    print(f'Slowo ktore podales zawiera wykluczone znaki lub to nie jest anagram')

