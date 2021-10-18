def main():
    a = 1
    b = [2]
    print(f'Main() przed wolaniem nowa:   id a to {id(a)} a id b to {id(b)}')
    nowa(a,b)
    print(f'Main() PO wywolaniu nowa      id a to {id(a)} a id b to {id(b)}')

def nowa(x,y):
    print(f'Nowa() przed zmiana wartosci: id x to {id(x)} a id y to {id(y)}')
    x = 3
    y = [5]
    print(f'Nowa() PO zmianie wartosci:   id x to {id(x)} a id y to {id(y)}')

def inaczej():
    a = 1
    b = a
    check_id(a,b)
    b = 8
    check_id(a,b)
    # ale listy ktore są mutable:
    x = [1]
    y = x
    check_id(x,y)
    y[0] = 111
    check_id(x,y)

def check_id(a,b):
    if id(a) == id(b):
        print(f'Obiekty typu, {type(a)} oraz {type(b)} to te same obiekty (to samo ID: {id(a)}, {id(b)})!!!')
    else:
        print(f'Obiekty typu, {type(a)} oraz {type(b)} to rozne obiekty, ich ID to {id(a)}, {id(b)}')
if __name__ == '__main__': main()

inaczej()
# integers are immutable
# lists are mutable
# So when you assign a mutable, you're actually assigning a reference to the mutable, and I have the side effect that
# when I change an element of that list in one place, it gets changed in both places because it's really just one
# object, and functions work exactly the same way.
# Innymi slowy dla elementow mutable obie funkcje zmieniaja wartosci jednego obiektu, dla immutable sa tworzone osobne
# obiekty