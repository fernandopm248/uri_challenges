n1,qtd1,pr1 = input().split()

n1 =int(n1)
qtd1 =int(qtd1)
pr1 =float(pr1)
n2,qtd2,pr2 = input().split()
n2 =int(n2)
qtd2 =int(qtd2)
pr2 =float(pr2)

prfinal = (pr1 * qtd1) + (pr2 * qtd2)
print(f'VALOR A PAGAR: R$ {prfinal:.2f}')