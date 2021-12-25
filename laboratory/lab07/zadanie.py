a = 10
b = 64
p = 107
u_0 = 2
v_0 = 2


def f(c, a, b, p):
    if c < (p // 2):
        return a * c
    else:
        return b * c


c = (a ** u_0 * b ** v_0) % p
d = c
i = 1
while True:
    print(f"Iteration {i} : c = {c} d = {d}")
    c = f(c, a, b, p) % p
    d = f(f(d, a, b, p) % p, a, b, p) % p
    
    if c == d % p:
        break
    i += 1
print(f"Iteration {i} : c = {c} d = {d}")

