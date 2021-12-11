import random

n = int(input('Введите нечетное целое число n>=5: '))
s, r = 0, n - 1
while r % 2 == 0:
    s += 1
    r //= 2
a = random.randint(2, n - 2)
y = (a ** r) % n
if y != 1 and y != n - 1:
    j = 1
    if j <= s - 1 and y != n - 1:
        y = (y ** 2) % n
        if y==1:
            print(f'Число {n} составное')
        j +=1
    if y != n - 1:
        print(f'Число {n} составное')
else:
    print(f'Число {n} ,вероятно, простое')
