
cos = "00200"
nowa_nazwa = ""

for i in range(len(cos)):
    if cos[i] == '0' and nowa_nazwa == "":
        nowa_nazwa += ''
        print(f'Jestem w pierwzy warunku, aktualny string: {nowa_nazwa}')
    else:
        nowa_nazwa += cos[i]
        print(f'Jestem w p22222 warunku, aktualny string: {nowa_nazwa}')


#cos = cos.replace('a','')
#print(nowa_nazwa)