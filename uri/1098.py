I = 0.2

J = 1.2

DIFF = 3.1

orgj = 1.2

J2 = 2

print('I=0 J=1')

print('I=0 J=2')

print('I=0 J=3')

while I <= 2:

    if I == 1.0:
        I = 1

        print(f'I={I} J={J2}')

        J += 1

        J2 += 1

    if I > 1.9:
        I = 2

        J = int(J)

        print(f'I={I} J={J}')

        J += 1

    if I != 1.0 and I != 2.0:
        print(f'I={I:.1f} J={J:.1f}')

        J += 1

    if J > 3 and J - I > DIFF:
        I += 0.2

        orgj += 0.2

        J = orgj