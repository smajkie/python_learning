# Nesting

#autokomis1 = {'marka': 'audi', 'kolor': 'czerwony'}
#autokomis2 = {'marka': 'bmw', 'kolor': 'czarny'}
#autokomis3 = {'marka': 'citroen', 'kolor': 'zielony'}

auto = {
    'komis1': {'marka': 'audi', 'kolor': 'czerwony'},
    'komis2': {'marka': 'bmw', 'kolor': 'czarny'},
    'komis3': {'marka': 'citroen', 'kolor': 'zielony'},
}


#autohandelplatz = [autokomis1, autokomis2, autokomis3]      # test z lista

#lista_marek = []
#lista_kolorow = []

#for marks in autohandelplatz:
#    lista_marek.append(marks['marka'])

#print(f'W naszych salonach znajdziecie takie marki jak', *lista_marek, '\n')

for klucz, wartosc in auto.items():             #interesujace przypadki fstringu
    print(klucz)                                #printuje normalnie
    print(f'W zasobach', {klucz}, 'znajduje sie', {wartosc['marka']}, 'w kolorze', {wartosc['kolor']})  #printuje z {}'
    print(f"W zasobach {klucz} znajduje sie {wartosc['marka']} w kolorze {wartosc['kolor']}")           #printuje ok jak calosc jest w ""
    # on chyba nie lubi jesli w srodku '' znajduja sie kolejne ''
