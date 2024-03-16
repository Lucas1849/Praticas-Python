#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma =  0
count = 0
for c in range(0,6):
    n = int(input('Digite um número:'))
    D = n%2
    if D == 0:
        soma +=  n
        count += 1
print('A soma dos {} valores pares nesse sequência é {}'.format(count, soma))
