print('a >= b > 0')
a = int(input('Введите a: '))
b = int(input('Введите b: '))
r = [a, b]
while True:
    if r[-2] % r[-1] == 0:
        d = r[-1]
        break
    else:
        r.append(r[-2] % r[-1])
print(f'НОД(a,b) = {d}')
