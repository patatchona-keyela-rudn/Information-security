u = input('Введите 1ое число: ')
v = input('Введите 2ое число: ')
u_int, v_int = int(u), int(v)
n = len(u) - 1
t = len(v) - 1
b = int(input("В какой системе счистления?:"))

v = [int(i) for i in v]
u = [int(i) for i in u]


if (t > n) or (t<1) or v[t] == 0:
    print("Введены неправильные данные")
else:
    q = [0]*(n-t+1)
    while u_int >= v_int * b ** (n - t):
        q[n-t] += 1
        u_int -= v_int * b ** (n-t)
    for i in range(n,t,-1):
        if u[i] >= v[t]:
            q[i-t-1] = b-1
        else:
            q[i-t-1] = (u[i]*b + u[i-1]) // v[t]
        while q[i-t-1] * (v[t]*b + v[t-1]) > (u[i]*b**2 + u[i-1]*b + u[i-2]):
            q[i-t-1] -= 1
        u_int -= q[i-t-1] * (b ** (i-t-1)) * v_int
    if u_int < 0:
        u_int += v_int * b**(i-t-1)
        q[i-t-1] -= 1
    
    q = int("".join(map(str, q)))
    r = u_int

    print(f"q = {q} r = {r}")
