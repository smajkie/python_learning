class Auto:                                                 # class name is by default capital letter

    def __init__(self, lakier, lampy):
        """Initialize class attributes"""
        self.lakier = lakier
        self.lampy = lampy
        self.przebieg = 0

    def pomaluj(self):
        print(f'Kolor mojego auta jest {self.lakier}')

    def swiatla(self):
        wynik = f'Mam swiatla {self.lampy}'
        return wynik

    def nalatane(self):
        print(self.przebieg)

    def nalatane_dodaj(self,km):
        """ manipulowanie attribute przez funkcje"""
        self.przebieg += km

class Osiagi:
    """ Simple class gathering all variables and methods for performance"""
    def __init__(self, bateria):
        self.przyspieszenie = 2
        self.bateria = 75

    def pokaz_przyspieszenie(self):
        print(f'Przyspieszenie to {self.przyspieszenie} sec do 100kmh')

class ElektryczneAuto(Auto):
    """Dziedziczenie"""
    def __init__(self,lakier,lampy):    # takes the information required to make Auto instance
        super().__init__(lakier,lampy)  # This line tells Python to call the __init__() method from Auto, which gives
                                        # an ElektryczneAuto instance all the attributes defined in that method.
#        self.bateria = 75
        self.bateria = Osiagi()

    def jaka_bateria(self):
        print(f'Ten wozek ma baterie o pojemnosci {self.bateria} kWh')

    def nalatane(self):
        """ Overriding methods from parent"""
        print('Elektryki nie lataja!')


def main():
    audi = Auto('zolty', 'led')
    audi.przebieg = 100                                         #direct assignenement
    audi.nalatane_dodaj(123)                                    #simple method on object
    print(f'Kolor mojego auta bez metody jest {audi.lakier}')   #call to object's property
    print(audi.swiatla())                                       #call to object's method value
    audi.pomaluj()
    audi.nalatane()
    # a teraz lets see czy elektryk dziedziczy ladnie
    tesla = ElektryczneAuto('niebieskie', 'superhiperled')
    tesla.pomaluj()
    tesla.jaka_bateria()
    print(f'{tesla.swiatla()}')
    tesla.nalatane()                                            #method from child overrides the same name method from parent
    tesla.bateria.pokaz_przyspieszenie()                        #instances as attributes


if __name__ == '__main__':
    main()
