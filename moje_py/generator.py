def main():
    for i in inclusive_range(2,22,21):
        print(i, end=' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 1                   # domyslny start gdyby podany tylko 1 arg (to jest stop)
    step = 1                    # domyslny step gdyby tylko podany 1 (end) lub 2 args (start i stop)

    # initialize parameters
    print(type(args), args)
    if numargs < 1:
        print(f'Error: Expected at least one arg, got {numargs}')
        return
    elif numargs == 1:
        stop = args[0]      # tu musi byc args[0] bo jak jest stop = args to do stopa probuje przypisac cala tuple a nie pierwsza wartosc
                            #  -> Line25:TypeError: '<=' not supported between instances of 'int' and 'tuple'
    elif numargs == 2:
        if args[0] > args[1]:   # check aby start byl mniejszy niz end
            print('Error: End cannot be less than start')
            return
        else:
            (start,stop) = args[0],args[1]  # ja bym napisal tak ale zobacz nizej, mozna wprost
    elif numargs == 3:
        if args[0] > args[1]:   # check aby start byl mniejszy niz end
            print('Error: End cannot be less than start')
            return
        elif args[2] > args[1] - args[0]:
            print('Error: Step does not work if its bigger than start end diff')
            return
        else:
            (start,stop,step) = args
    else:
        raise TypeError(f'Expected 1-3 args, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step               # zwieksz krok

if __name__ == '__main__': main()