#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#Exemplo:    0 – 1 – 1 – 2 – 3 – 5 - 8 
n = int(input('Quantos termos você quer ver ? '))
a1 = 0
a2 = 1
count = 3
print('{} - {} -'.format(a1,a2),end='')
while count <= n:
    count += 1
    a3 = a1 + a2
    print(' {}'.format(a3),end='') 
    print(' -'if count <= n else '',end='')
    a1 = a2
    a2 = a3


    
    

