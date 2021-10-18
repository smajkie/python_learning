import time

pierwsza = 100000
dzielnik: range = range(1,pierwsza+1)
start = time.time()
for n in range(1,pierwsza+1):

    liczba_dzielen = 0
    for i in dzielnik:
        dzielenie = divmod(n,i)
        if dzielenie[1] == 0:
            liczba_dzielen = liczba_dzielen+1
#    print('Liczba {} ma {} dzielnikow'.format(n,liczba_dzielen))
    stop = time.time()
    if liczba_dzielen == 2:
        duration = stop-start
#        print('NIE! Liczba {} nie jest liczba pierwsza'.format(n))
        print('TAK! Liczba {} jest liczba pierwsza i policzylem to w czasie: {}'.format(n,duration))
    liczba_dzielen = 0
