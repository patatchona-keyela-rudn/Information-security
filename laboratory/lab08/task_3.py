u = str(input('Введите 1ое число: '))
v = str(input('Введите 2ое число: '))
b = int(input("В какой системе счистления?: "))
v = [int(i) for i in v]
u = [int(i) for i in u]
n, m = len(u), len(v)
j = m

w = [0]*(n+m)

while j > 0 :
    if v[j-1] != 0:
        k = 0
        for i in range(n,0,-1):
            t = u[i-1] * v[j-1] + w[i+j-1] + k
            w[i+j-1] = t % b
            k = t // b
        w[j-1] = k
    else:
        w[j-1] = 0
    j -= 1

w = int("".join(map(str, w)))
print("Result: ",w)
