from Curs6 import Car
class Service:
    listCar= []
    numberofcars = 0
    price = 0

    def __init__(self):
        pass

    def setListCar(self,listCar):
        self.listCar = listCar
    def getNumberofcars(self):
        self.numberofcars = len(self.listCar)
        return self.numberofcars
    def setPrice(self,price):
        self.price = price
    def calculateprice(self):
        for i in self.listCar:
            if i.model == 'Duster':
                print(f'Pretul este 3000 lei')
                self.setPrice(3000)
            elif i.model =='Sandero':
                print(f'Pretul este 4000')
                self.setPrice(4000)
            else:
                print(f'Pretul este 2500')
                self.setPrice(2500)

car1 = Car('Logan','Negru')
car2 = Car('sandero','alb')
car3 = Car('Duster','mov')
car4= Car('Spring','rosu')
service = Service()
service.setListCar([car1,car2,car3,car4])
service.calculateprice()
print(service.getNumberofcars())
service.setListCar([car1,car2,car3,car4,car4])
print(service.getNumberofcars())