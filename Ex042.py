#Refaça o DESAFIO 035 dos triângulos, acrscentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

#Lei de formação do triângulo
R1 = float(input('Qual o comprimento do primeiro segmento ?'))
R2 = float(input('Qual o comprimento do segundo segmento ?'))
R3 = float(input('Qual o comprimento do terceiro segmento ?'))

if R1 < R3 + R2 and R2 < R1 + R3 and R3 < R1 + R2:
    print('Com esses segmentos é possível construir um triângulo')
    if R1 == R2 == R3:
        print('Esse triângulo que será formado é classificado como EQUILÁTERO')
    if R1 == R2 and R3!= R1  or R2 == R3 and R1 != R2 or R3 == R1 and R2!= R3:
        print('Esse triângulo que será formado é classificado como ISÓCELES')
    if R1 != R2 and R2 != R3 and R3 != R1:
        print('Esse triângulo que será formado é classificado como ESCALENO')
else:
    print('Com esses segmentos não é possível construir um triângulo')


