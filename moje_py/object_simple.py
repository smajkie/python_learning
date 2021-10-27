class Auto:                                                 # class name is by default capital letter

    def __init__(self, lakier, lampy):
        """Initialize class attributes"""
        self.lakier = lakier
        self.lampy = lampy

    def pomaluj(self):
        print(f'Kolor mojego auta jest {self.lakier}')

    def swiatla(self):
        print(f'Mam swiatla {self.lampy}')


def main():
    audi = Auto('zolty', 'led')
    print(f'Kolor mojego auta bez metody jest {audi.lakier}')
    audi.pomaluj()
    audi.swiatla()


if __name__ == '__main__':
    main()
