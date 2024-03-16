#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

R1 = float(input('Digite o comprimento de primeira reta:'))
R2 = float(input('Digite o comprimento da segunda reta:'))
R3 = float(input('Digite o comprimento da terceira reta'))

if R1 < R2 + R3 and R2 < R3 + R1 and R3 < R1 + R2:
    print('Esses segmentos PODEM formar um triângulo')
else:
    print('Esses segmentos NÃO PODEM formar um triângulo')