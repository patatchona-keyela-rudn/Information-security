def f(x,n):
    return (x**2 + 5) % n

def gcd(a,b):
    r = [a, b]
    while True:
        if r[-2] % r[-1] == 0:
            d = r[-1]
            break
        else:
            r.append(r[-2] % r[-1])
    return d

def pollard_p_method(n,c=1,f=f):
    a, b = c, c
    d = 1

    while d==1:
        a = f(a,n) % n
        b = f(f(b,n),n)%n

        d = gcd(a-b,n)

        print(f"a = {a} b = {b} d = {d}")

    if d != n:
        print(f"Нетривиальный делитель {n} : {d}")
        return d
    else:
        print("Нетривиальный делитель не найден")
        return d

def decompose(N):
    div1 = pollard_p_method(N)
    div2 = N // div1
    div1,div2 = max(div1,div2), min(div1,div2)
    print(f"\nDecomposition of {N} :")
    print(f"{N} = {int((div1 + div2)//2)}^2 - {int((div1 - div2)/2)}^2\n")
    
if __name__ == "__main__":
    N = int(input("Enter the number to decompose: "))
    decompose(N)