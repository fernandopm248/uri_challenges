import math
try:
    a,b,c = input().split()


    a = float(a)
    b = float(b)
    c = float(c)

    ac = (b ** 2) - 4 * a * c
    raiz = math.sqrt(ac)

    r1 = (-b + raiz) /(2 * a)
    r2 = (-b - raiz) /(2 * a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
except:
    print('Impossivel calcular')
