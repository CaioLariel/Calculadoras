from ast import Break

print('vamos calcular uma equação de 2 grau')

a = float(input('digite o valor de "a"='))
b = float(input('digite o valor de "b"='))
c = float(input('digite o valor de "c"='))
delta = b ** 2 - 4 * a * c
print('delta = ', delta)
raizdelta = delta ** (0.5)
print('raiz de delta = ', raizdelta)
x1 = (-b + raizdelta) / (2 * a)
print('x1 = ', x1)
x2 = (-b - raizdelta) / (2 * a)
print('x2 = ', x2)

a = (input("fim, aperte enter para fechar."))
Break