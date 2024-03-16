#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

N = int(input('Digite um número para saber a tabuada:'))

for c in range(0, 11):
    M = N*c
    print('{} x {} = {} '.format(N, c, M ))
