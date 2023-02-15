# lista =[1,2,3,'Ion','Ana',4]
# print (lista)
# print(len(lista))
# lista.remove(lista [0]) #stergem din lista
# print(lista)
# lista.pop(0)
# print(lista)
# lista.extend([1,2,3,4])
# print(lista)
# lista1=lista + [1,2,3,4]
# print(lista1)
# lista.append('string')
# print(lista)
# lista1.insert(2,'avas')
# print(lista1)
# lista2=[1,6,3]
# lista2.extend(lista1)
# print(lista2)
# lista2.insert(3,lista1)
# print(lista2)
'''
DICTIONARE
'''
dictionar= {
    'fructe': 'mare', 'legume': 'rosie',
}
print(dictionar)
print(type(dictionar))
print(dictionar.values()) #afisare valori
print(dictionar.keys())
dictionar.update({2:'sambata'})
print(dictionar)
print(dictionar.get(2))
print(len(dictionar))
dictionar.pop(len(dictionar )-1)
print(dictionar)

'''
SET URI 
'''
# valori= {'mere','pere',2,3,4}
# print(valori)
# print(type(valori))
# masini2={'mere','gutui',4,7}
# valori.intersection(masini2)
# print(valori.intersection(masini2))
# print(valori.difference(masini2))
#  newSet1 = set()
#  newSet1.update({4,6,})
#  print(newSet1)

# '''
# TUPLA
# '''
# zile= ('mar','marti','miercuri')
# print(zile)
# luni='mai','iunie','iulie'
# print(luni)
# print(type(luni))
# mai ,iunie ,iulie= luni
# print(mai,iunie,iulie)
# mai2,_,_=luni
# mai2=luni
# saptamana= ('luni','marti',('miercuri','joi'),'vineri')
# print(saptamana)
# print(saptamana[2][1])