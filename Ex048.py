#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
#IMPORTANTE = para realizar a soma de todos os números é necessário os acumuladores, que ainda não foram passados na aula 13

soma = 0
count = 0
for c in range(-1,501):

    D = c%2
    d = c%3
    if D != 0 and d == 0:
        soma = soma + c
        count = count + 1
print('A soma de todos os {} valores ímpares e multiplos de 3 é {}'.format(count,soma))
       
        
        