#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

#Como resolvi primordialmente
from math import factorial

n = int(input('Digite um número: '))
fac = factorial(n)
print('O fatorial do número {} é {}'.format(n,fac))

#Outra solução do professor
c = n
f = 1
print('Calculando {}! = '.format(c),end='')
while c > 0: 
    print('{}'.format(c),end='')
    print(' x '  if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f)
    