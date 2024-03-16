#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.
Geral = [[],[]]
for n in range(0,7):
    valores = int(input('Digite um número: '))
    if valores % 2 == 0:
        Geral[0].insert(0,valores)
        Geral[0].sort()
    else:
        Geral[1].insert(0,valores)
        Geral[1].sort()

print(f'A lista de valores pare é {Geral[0]}')
print(f'A lista de valores ímpares é {Geral[1]}')
