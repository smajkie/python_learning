def main():
    x = (1,2,3)
    nowa(*x)

def nowa(*args):
    if len(args):
        for i in args:
            print(i)
    else:
        print('zonk')

if __name__ == '__main__': main()


