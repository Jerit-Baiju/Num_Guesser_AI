import random

a = 0
b = 100

r = random.randint(a,b)
print(f'random num = {r}')

for x in range(10):
    c = (a+b)/2
    if c % 2 != 0:
        if p == 'more':
            c = c - 1
        elif p == 'less':
            c = c + 1
    print(f'c is {c}')
    if r == c:
        print('win')
        break

    elif r > c:
        p = 'more'
        print('r is more')
        a = c
        
    elif r < c:
        p = 'less'
        print('r is less')
        b = c
            
    else:
        print('else')

print(r)