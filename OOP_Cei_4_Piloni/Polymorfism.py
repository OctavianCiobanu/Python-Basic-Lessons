'''SUPRAINCARCARE'''
# print(len('abc'))
# print(len([1,2,3,4]))
# def ad(x,y,z=0):
#     return x+y+z
#
# print(ad(2,3,5))

class Adunare():
    def add(self,x,y):
        return x+y
    def add(self,x,y,z=0):
        return x+y+z
adunare= Adunare()
print(adunare.add(5,6))
