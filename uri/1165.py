
n = int(input())

for i in range(0,n):
    num = int(input())
    cont = 0
    m=1
    while m <= num:
        if num % m == 0:
            cont = cont + 1
        m = m + 1
    if cont > 2:
        print(f'{num} nao eh primo')
    else:
        print(f'{num} eh primo')




