20
print('a >= b > 0')
a = int(input('Введите a: '))
b = int(input('Введите b: '))
g = 1
while True:
    if a % 2 == 0 and b % 2 == 0:
        a *= 0.5
        b *= 0.5
        g *= 2
    else:
        break
u = a
v = b
A = 1
B = 0
C = 0
D = 1
while u != 0:
    while u % 2 == 0:
        u = u * 0.5
        if A % 2 == 0 and B % 2 == 0:
            A *= 0.5
            B *= 0.5
        else:
            A = (A + b) * 0.5
            B = (B - a) * 0.5
    while v % 2 == 0:
        v = v * 0.5
        if C % 2 == 0 and D % 2 == 0:
            C *= 0.5
            D *= 0.5
        else:
            C = (C + b) * 0.5
            D = (D - a) * 0.5
    if u >= v:
        u = u - v
        A = A - C
        B = B - D
    else:
        v = v - u
        C = C - A
        D = D - B
d = g * v
x = C
y = D
print(d, x, y)
