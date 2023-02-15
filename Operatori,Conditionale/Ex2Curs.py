'''
joc de noroc-zarurri
1 zar.6 fete
primim de la tastatura un nr
de verificat daca nr este egal cu fata zarului aruncat
'''

import random
zar = [1, 2, 3, 4, 5, 6]
diceroll = random.choice(zar)

number = int(input('Alege un numar:' ))
if number < diceroll:
    print(f'Ai pierdut. Ai ales un nr mai mic. Ai ales numarul {number},dar a fost {diceroll}')
elif number > diceroll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {number},dar a fost {diceroll}')
else:
    print('Ai castigat.Felicitari!')
