import random
from task_2 import jacobian_symbol

n = int(input('Введите нечетное целое число n>=5: '))
a = random.randint(2, n - 2)
r = a ** ((n - 1) / 2) % n
if r != 1 and r != n - 1:
    print(f'Число {n} - составное')
else:
    s = jacobian_symbol(a, n)
    if r % n == s:
        print(f'Число {n} составное')
    else:
        print(f'Число {n} ,вероятно, простое')
