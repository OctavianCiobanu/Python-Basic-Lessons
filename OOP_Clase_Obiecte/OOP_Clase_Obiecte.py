class Car :
    make='Dacia'
    model= None
    years= 2022
    color= None
#Constructor
    def __init__(self ,model,color):
        self.model= model
        self.color= color


    def getfields(self):
        print(self.color)
        print(self.model)
        print(self.years)
        print(self.make)
    def accelerate(self):
        print('Vruum vruum!')
    def stop(self):
        print('STOP!')
# car = Car('Spring','Black')
# car2= Car('Duster','rosu')
# car.getfields()
# car2.getfields()
#
#
# car.accelerate()
# car2.stop()