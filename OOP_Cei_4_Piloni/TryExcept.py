try:
    lista=[1,3,4]
    lista[6]
except IndexError as e:
    print(e)
print('Am ajuns aici')