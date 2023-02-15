class CarPy():
    def __init__(self,color):
        self.__color = color
    @property
    def color(self):
        return self.__color

    @color.getter
    def color(self):
        print(f'Getter: Culoarea este {self.__color}')
        return self.__color

    @color.setter
    def color(self,color):
        print(f'Setter:Noua culoare este {color}')
        self.__color = color

    @color.deleter
    def color(self):
        print(f'Deleter: Am sters culoarea')
        self.__color=None
car= CarPy('gray')
car.color = 'red'
car.color
del car.color
car.color
