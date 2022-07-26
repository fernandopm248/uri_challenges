
acu = 0
for x in range(5):
    n = int(input())
    cont = 0

    if n % 2 == 0:

       cont += 1
       acu += cont


print(f'{acu} valores pares')
