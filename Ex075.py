#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

tp = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
# Contador de 9
print(f'O número nove apareceu {tp.count(9)} vezes')
#Posição do 3
if 3 in tp:
    posi = tp.index(3)+1
    print(f'O número 3 apareceu na {posi}ª posição')
#Número pares
print('Os número pares nesta tupla são: ')
for p in tp:
    if p%2 == 0:
        print(p,' ', end='')
