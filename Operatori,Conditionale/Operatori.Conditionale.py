'''
Pt un bancomat verificam user name si parola
user are doar 2 incercari si parola la fel
userul doreste sa scoata o anunmita de bani avand un sold curent
suma dorita trebuie sa fie <= decat soldul curent
daca introduce o suma prea mare poate sa aleaga daca doreste sa reincerce sa nu
la 2 a incercare daca introduce din nou o suma prea mare iese din prog
'''
expetedUser= 'Marius'
expeterParola= '2345'
expetedsold=40000.3
user= input('Introduceti user name:')
if user == expetedUser:
    print('User name corect')
else:
    print('User name incorect.Reincercati.')
    user=input("Reintroduceti user name:")
    assert user == expetedUser ,'User name incorect. O zi buna'
    print('User name corect!')
parola=input('Introduceti parola:')
if parola == expeterParola:
    print('Parola corecta!')
else:
    print('Parola incorecta.Reincercati')
    parola=input('Reintroduceti parola:')
    assert  parola ==expeterParola , 'Parola gresita .O zi buna'
    print('Parola corecta!')

sold = float(input('Introduceti soldul pe care doriti sa-l scoateti:'))
if sold >= expetedsold:
    print('Suma dorita este prea mare pentru a fi scoasa. Reintroduceti alta suma')
    reincercare = input('Doriti sa incercati din nou? Da/Nu')
    if reincercare == "Da" :
        sold=float(input('Introdu suma dorita:'))
        assert sold <= expetedsold ,'Suma dorita este prea mare'
        print('Ridicati banii')
    elif reincercare =='Nu':
        print('La revedere')
    else:
        print('O zi buna')