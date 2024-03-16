#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
count = 0
soma = 0
while True:
    n = int(input('Digite um número (999 = parar o programa): '))
    if n == 999:
        break
    count += 1
    soma += n
#fstrings = nova forma de utilizar o print python 3.6+
print(f'Foram digitados {count} números')
print(f'E a soma entre eles é {soma}')
