class auto:
    lakier = 'srebrny'
    lampy = 'led'

    def pomaluj(self):
        print(f'Kolor mojego auta jest {self.lakier}')

    def swiatla(self):
        print(f'Mam swiatla {self.lampy}')

def main():
    audi = auto()
    audi.pomaluj()
    audi.swiatla()

if __name__ == '__main__': main()