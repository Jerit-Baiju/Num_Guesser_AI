import random

a = 0
b = 100

r = random.randint(a, b)
print(f'random num = {r}')

for x in range(10):
    c = (a+b)/2
    if c % 2 != 0:
        if p == 'more':
            c = c - 1
        elif p == 'less':
            c = c + 1
    if b - a == 2:
        print(f'won --- {a+1} --- chance -- {x}')
        break
    if r == c:
        print(f'won --- {c} --- chance -- {x}')
        break

    elif r > c:
        p = 'more'
        a = c

    elif r < c:
        p = 'less'
        b = c

print(r)
