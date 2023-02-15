class Chef:
    def make_salat(self):
        print('Salat')
    def make_fries(self):
        print("fries")
class JapanesseChef(Chef):
    def make_sushi(self):
        print('sushi')
    def make_salat(self):
        print('Japanesse salat')
class italianChef(Chef):
    def make_pizza(self):
        print('Pizza')
chef = Chef()
japanessechef= JapanesseChef()
italian=italianChef()
chef.make_fries()
japanessechef.make_salat()
italian.make_pizza()
