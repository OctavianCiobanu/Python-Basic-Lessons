# def print_hi():
#     print('Helo')
#     print('sfdsf')
# print_hi()
# print_hi()
# print_hi()

'''
parametrii-DATE care inta in functia
resprectiva(de mai sus),introduse de programator
sunt initializare la apelarea functiei
'''

# def print_hi(user,age=None):
#     print(age)
#     print(f'Hi {user}')
# print_hi('Andrei')
# print_hi('Costel')
# print_hi('Costel',44) # Am suprascris None

'''
RETURN
'''
# def if_natural(numar):
#     if numar >= 0:
#         return True
#     else:
#         return False
# raspuns = if_natural(4)
# if raspuns:
#     print('Numarul este natural')
# else:
#     print('Numarul nu este natural')
# raspuns = if_natural(-4)
# if raspuns:
#     print('Numarul este natural')
# else:
#     print('Numarul nu este natural')

''' Exercitii curs'''
# def cont_bancar(userName,parola,plata):
#     i=0
#     while i < 3 :
#         sold=200
#         if userName== 'Marius' :
#             if parola == '2323':
#                 if plata <= sold:
#                     print('Tranzactie reusita')
#                     break
#                 else:
#                     print('Fonduri insuficiente!')
#                     break
#             else:
#                 print('Parola gresita')
#                 parola=int(input('Introduceti parola'))
#                 i+=1
#         else:
#             print('User name gresit')
#             userName=input('ID:')
#             i+=1
#     print('Multumim,o zi frumoasa')
# # cont_bancar('Marius','2323',200)
# cont_bancar(input('ID:'),input('Parola:'),int(input('Sold:')))

''' Sortare bublle sort'''

# def bubllesort(lista):
#     for i in range(len(lista)):
#         for j in range (len(lista)-1):
#             if lista[j] > lista[j+1]:
#                 lista[j],lista[j+1]= lista[j +1],lista[j]
#     return lista

# listaSortata= bubllesort([32,4,7,2,84,2,7,4])
# print(listaSortata)

''' MAxim'''

# def listaMAX(lista):
#    listaSortata =bubllesort(lista)
#    return  listaSortata[-1]
# max = listaMAX([5,3,1,7,0,7,23])
# print(max)

'''2'''
# def list_max2(lista):
#     maxim=0
#     for i in range(len(lista)):
#         if lista[i] >= maxim:
#             maxim= lista[i]
#     return maxim
# maxim = list_max2([5,3,1,7,0,7,23])
# print(maxim)

''' DICE ROLL'''
import random

def diceRoll():
    zar =[1,2,3,4,5,6]
    numarZar = random.choice(zar)
    numarAles= int(input('Alege un numar:'))
    if numarAles < numarZar:
        print(f'Ai pierdut. Ai ales un nr mai mic. Ai ales numarul {numarAles},dar a fost {numarZar}')
    elif numarAles > numarZar:
        print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numarAles},dar a fost {numarZar}')
    else:
        print('Ai castigat.Felicitari!')
diceRoll()
diceRoll()
diceRoll()
diceRoll()
diceRoll()
diceRoll()