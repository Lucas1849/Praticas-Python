#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = maior = menor = count = 0
resp = 'S'

while resp in 'Ss':
    n = int(input('Digite um número: '))
    count += 1
    soma += n
    if count == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]

média = soma/count
print('A média dos números escolhidos é {}'.format(média))
print('O maior número dentre os escolhidos é {}'.format(maior))
print('O menor valor dentre os escolhidos é {}'.format(menor))