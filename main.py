import random

a = 0
b = 100

r = random.randint(a,b)
print(r)

for x in range(10):
    if r == (a+b)/2:
        print('win')

    elif r < (a+b)/2:
        print('r is less')
        c = (a+b)/2

    elif r > (a+b)/2:
        print('r is more')
        c = (a+b)/2
    else:
        print('else')
