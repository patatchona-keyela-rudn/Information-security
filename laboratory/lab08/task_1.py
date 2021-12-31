u = str(input('Введите 1 число: '))
v = str(input('Введите 1 число: '))
v = [int(i) for i in v]
u = [int(i) for i in u]
n = len(u)
b = 10
j = n - 1
k = 0
w = ''
while j >= 0:
    wj = (u[j] + v[j] + k) % b
    k = (u[j] + v[j] + k) // b
    w = str(wj) +w
    j -= 1
w = str(k) +w
print(w)


