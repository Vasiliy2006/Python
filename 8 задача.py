from itertools import product
numbers = product('01234567' , repeat=5)
k=0
for n in numbers:
    numb=''.join(n)
    if numb.count('6')==1 and numb[0] !='0':
        if '16' not in numb and '36' not in numb and '56' not in numb and\
               '76' not in numb and '61' not in numb and '63' not in numb and\
               '65' not in numb and '67' not in numb:
            k=k+1
print(k)
