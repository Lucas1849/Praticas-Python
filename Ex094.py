#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade 
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
Dados = {}
Cadastro = []
mulheres = []
acima = []
soma = 0
confirm = 'S'
while confirm in 'Ss':
    Dados.clear()
    Dados['Nome'] = input('Nome: ').capitalize()
    Dados['Sexo'] = input('[F/M]: ').upper().strip()[0]
    while Dados['Sexo'] not in 'FfMm':
        Dados['Sexo'] = input('Opção inválida.Escolha apenas [F/M]: ')
    Dados['Idade'] = int(input('Idade: '))
    soma += Dados['Idade']
    if Dados['Sexo'] in 'Ff':
        mulheres.append(Dados['Nome'])
    Cadastro.append(Dados.copy())
    if Dados['Idade'] > soma/len(Cadastro):
        acima.append(Dados.copy())
    confirm = input('Deseja continuar [S/N] ? ')
    while confirm not in 'SsNn':
        confirm = input('Opção inválida.Deseja continuar [S/N] ? ')
print("-="*30)
print(f'Foram cadastradas {len(Cadastro)} pessoas.')
print(f'A média de idades é {soma/len(Cadastro):.2f}')
print(f'As mulheres cadastradas foram ',end='')
for c in range (0,len(mulheres)):
    print(mulheres[c],end=' ')
    if c < len(mulheres) - 2:
        print(', ',end='')
    elif c == len(mulheres) - 2:
        print(' e ',end='')
print()
for c in range(0,len(acima)):
    print(f'{"":>5}Nome = {acima[c]["Nome"]}; Sexo = {acima[c]["Sexo"]}; Idade = {acima[c]["Idade"]}')
