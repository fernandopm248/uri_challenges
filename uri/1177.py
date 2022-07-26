
t = int(input())
n = []
val = 0

while len(n) < 1000 :
    if val < t :
        n.append(val)

        val += 1
    else:
        val = 0
        n.append(val)

        val += 1


for i , val in enumerate(n) :
    print(f'N[{i}] = {val}')