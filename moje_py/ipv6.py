def szostka(adres):
    # inicjuje zmienne
    nowy_adres = ''
    lista = adres.split(':')

    print(*lista)

    max_czworki_zer = 1
    nasz_max = 1

    for m in range(1, len(lista)):
        if lista[m-1] == '0000' and lista[m] == '0000':
            print(f'Czworka numer {m} jest 0000 i ma sasiada ktory tez jest 0000')
            max_czworki_zer += 1
            print(f'Podbijam max do {max_czworki_zer}')
            if max_czworki_zer > nasz_max:
                nasz_max = max_czworki_zer
                print(f'Nowy kandydat na maxa:{nasz_max}')
        elif lista[m-1] == '0000' and lista[m] != '0000':
            # koniec liczenia maxa bo nastepny element nie jest zerami
            print(f'Czworka numer {m} jest 0000 ale jej sasiad juz NIE')
            if max_czworki_zer > nasz_max:
                nasz_max = max_czworki_zer
                print(f'Nowy kandydat na maxa:{nasz_max}')
                max_czworki_zer = 1
            else:
                print(f'Liczba czworek {max_czworki_zer} mniejsza od obecnego max - reject')
                max_czworki_zer = 1
        elif lista[m-1] != '0000':
            print(f'Pomijam czworke numer: {m} bo nie jest czworka zer')
            max_czworki_zer = 1

    print(f'Obliczony max ciag czworek zer to {nasz_max}')

    # zamien ciag 0000 na ::
    do_skrocenia_poczatek = nasz_max*('0000' + ':')
    do_skrocenia_srodek = (':' + nasz_max*('0000' + ':'))
    do_skrocenia_koniec = nasz_max*(':' + '0000')

    print(do_skrocenia_poczatek, do_skrocenia_srodek, do_skrocenia_koniec)

    print(adres)
    if (adres.find(do_skrocenia_srodek)) != -1:
        print('srodek')
        nowy_adres = adres.replace(do_skrocenia_srodek, '::', 1)
    elif (adres.find(do_skrocenia_poczatek)) != -1:
        print('poczatek')
        nowy_adres = adres.replace(do_skrocenia_poczatek, '::', 1)
    elif (adres.find(do_skrocenia_koniec)) != -1:
        print('koniec')
        nowy_adres = adres.replace(do_skrocenia_koniec, '::', 1)

    print(nowy_adres)

    kasuj_zera_1 = '0000:'
    result = nowy_adres.replace(kasuj_zera_1, '0:')
    print(result)

#if __name__ == "__main__":
 #   szostka('0000:2200:0:0000:0000:0000:asdd:0000:0000:0000:0000')

