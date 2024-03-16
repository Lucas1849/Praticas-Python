#Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:   
#A) Quantas pessoas foram cadastradas.
#Posso usar um contador ou len(lista)...
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
Dados = []
Geral = []
pesado = leve = 0
confirm = 'S'
while confirm in 'Ss':
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))
    if len(Geral) == 0:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
    Dados.append(nome)
    Dados.append(peso)
    Geral.append(Dados[:])
    Dados.clear()
    confirm = input('Deseja continuar [S/N] ? ').upper().strip()[0]
    while confirm not in 'SsNn':
        confirm = input('Opção inválida. Deseja continuar [S/N] ? ').upper().strip()[0]

print(f'Foram cadastradas {len(Geral)} pessoas.')
print(f'O maior peso é {pesado}Kg, as pessoas que pesam o maior peso são: ',end='')
for D in Geral:
   if D[1] == pesado:
       print(f'[{D[0]}] ',end='')
print(f'O menor peso é {leve}Kg, as peesoas que pesam o menor peso são: ',end='')
for P in Geral:
    if P[1] == leve:
        print(f'[{P[0]}] ',end='')

       


