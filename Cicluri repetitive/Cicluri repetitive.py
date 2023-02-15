# i = 0
#
# while i<=10:
#     print(i)
#     i +=1
# print("Done!")
'''
#FOR - FOR/ELSe
'''

# for i in range (10):
#     print(i)
# for i in range (20,4, -1):
#     print(i)

'''
FOR EACH
'''
culori=['rosu','albastru','galben','mov']
for culoare in culori :
    print(culoare)
for i in range (len(culori)):
    print(culori[i])
# i=0
# while(i<=10000):
#     print(i)
#     if i ==5:
#         break
#     i += 1
# i = 0
# while True:
#     print(f'Valoarea lui i este {i}')
#     i +=1
#     if i >=40:
#         break
#
# culori=['rosu','albastru','galben','mov']
# for culoare in culori:
#     if culoare == 'albastru' :
#           continue
#     print(culoare)
'''
Adunare toate numerele din lista
'''
list1 = [1,2,3,4,5,6,7,8,9,10]
# s=0
# for lista2 in list1:
#      s=s+lista2
# print(s)


# i=0
# sum=0
# while i < len(list1):
#     sum = sum + list1[i]
#     i += 1
# print(sum)


# anotimpuri=['primvara','vara','toamna','iarna']
# for anotimp in anotimpuri:
#      if anotimp =='iarna':
#          pass
#      #    break
#      # print(anotimp)
#      if anotimp == 'vara':
#          continue
#      print(anotimp)

''' 
SORTARE BUBBLE
'''
list= [10,12,0,4,1,7]
'''
marge sort 
intersection sort
quiq sort
'''
for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j], list[j+1]=list[j+1],list[j]
print(list)
