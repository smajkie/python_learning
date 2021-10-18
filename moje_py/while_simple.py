# List in dict

banner = 'Podaj cos tylko nie q'
banner += '\nq = quit'
lista=[]

flaga = True
while flaga:
    wartosc=input(banner)

    if wartosc == 'q':
        flaga = False               # mozna tez zamist tego zrobic 'break'
    else:
        lista.append(wartosc)
        print(lista)
