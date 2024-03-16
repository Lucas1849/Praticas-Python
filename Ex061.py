#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a10 = a1 + (10*r - 1*r) 
n = a1

while n <= a10 :
    print('{}'.format(n),end='')
    print(' - ' if n < a10 else '',end='')
    n += r
    