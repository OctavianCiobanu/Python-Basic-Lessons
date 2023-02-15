class Car:
    __color ='gray' # '__' privat
    model='BMW'
    def get_color(self): #folosim getter sa afisam culoarea
        return self.__color
    def set_color(self,culoare_dorita): #folosim setter ca sa setam o alta culoare
        self.__color= culoare_dorita
        self.__mesaj(f'Culoarea a fost schimbata in {culoare_dorita}')
    def __mesaj(self,mesaj):
        print(mesaj)

masina=Car()
masina.set_color('rosu')

#Exercitiu

class Triunghi():
    baza = 0
    inaltime = 0
    arie=0
    def __init__(self,baza,inaltime):
        self.baza=baza
        self.inaltime=inaltime
    def get_arie(self):
        self.__calculateArie()
        return self.__arie

    def __calculateArie(self):
        self.__arie = self.baza * self.inaltime / 2
triunghi= Triunghi(7,4)
print(triunghi.get_arie())

