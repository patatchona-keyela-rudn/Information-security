print('a >= b > 0')
a = int(input('Введите a: '))
b = int(input('Введите b: '))
r = [a, b]
x = [1, 0]
y = [0, 1]
while True:
    if r[-2] % r[-1] == 0:
        d = r[-1]
        X = x[-1]
        Y = y[-1]
        break
    else:
        q_i = r[-2] // r[-1]
        x.append(x[-2]-q_i*x[-1])
        y.append(y[-2]-q_i*y[-1])
        r.append(r[-2] % r[-1])
print(d, X, Y)
