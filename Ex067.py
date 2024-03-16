#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Deseja ver a tabuada de qual valor [valor negativo = encerrar programa] ? '))
    if n < 0:
        break
    else:
        for c in range (0,11):
            m = n*c
            print(f'{n} x {c} = {m}')
print('Calculadora de tabuada encerrado...')


    