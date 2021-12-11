def jacobian_symbol(a, n):
    g = 1

    while True:
        if a == 0:
            return 0
        elif a == 1:
            return g
        else:
            k, a1 = 0, a
            while a1 % 2 == 0:
                k += 1
                a1 //= 2
            if k % 2 == 0:
                s = 1
            else:
                if abs(n % 8) == 1:
                    s = 1
                else:
                    s = -1
            if a1 == 1:
                return g * s
            if n % 4 == 3 and a1 % 4 == 3:
                s *= -1
            a = n % a1
            n = a1
            g = g * s


if __name__ == "__main__":
    n = int(input("Enter an odd number n>= 3: "))
    a = int(input("Enter an integer 0<= a <= n: "))
    print(jacobian_symbol(a, n))
