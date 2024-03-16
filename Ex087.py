#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = maior = soma3 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um número para a posição {l} {c}: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
            
for l in range(0,3):
     soma3 = matriz[l][2]  
     
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c]  > maior:
             maior = matriz[1][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print(f'A soma de todos os valores pares digitados é {soma}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda coluna é {maior}')



