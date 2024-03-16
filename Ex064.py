#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = int(input('Digite quantos números você quiser [999 = sair do programa]: '))
soma = 0
count = 0
while n != 999: 
    soma += n
    count += 1
    n = int(input('Digite quantos números você quise [999 = sair do programa]: '))
print('Foram digitados {} números'.format(count))
print('E a soma entre eles é de {}'.format(soma))

