u = str(input('Введите 1-ое число: '))
v = str(input('Введите 2-ое число: '))
b = int(input("В какой системе счистления?: "))
v = [int(i) for i in v]
u = [int(i) for i in u]
n, m = len(u), len(v)
w = [0] * (n + m)

t = 0

for s in range(m + n):
    for i in range(s + 1):
        t = t + u[n - i - 1] * v[m - s + i - 1]
    w[m + n - s - 1] = t % b
    t = t // b
print("Result: ", w)
