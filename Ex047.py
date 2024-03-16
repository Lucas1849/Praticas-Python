#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


print('Os números pares presentes em um intervalo de 1 até 50 são: ')
for c in range(1,51):
    D = c%2
    if D == 0:
        print(c, end=' ')