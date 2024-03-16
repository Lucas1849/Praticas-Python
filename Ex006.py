#Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um número:'))
print('O dobro de {} é {}'.format(n, n*2), end='')
print(', o seu triplo é {}'.format(n*3), end=' ')
print('e sua raiz quadrada é {:.3f}'.format(n**(1/2)))
