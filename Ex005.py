#Desafio 005 -Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor
n = int(input('Digite um número:'))
print('Analisando o valor {}, seu sucessor é {}'.format(n, n+1), end=' ')
print('e o seu antecessor é {}'.format(n-1))