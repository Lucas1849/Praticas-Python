#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
Dados = {}
Dados['Nome'] = input('Nome: ').capitalize().strip()
Dados['Média'] = float(input('Média do aluno: '))
if Dados['Média'] >= 7:
    Dados['Situação'] = 'APROVADO'
elif 5 < Dados['Média'] < 7:
    Dados['Situação'] = 'RECUPERAÇÃO'
else:
    Dados['Situação'] = 'REPROVADO'
print(('-=')*30)
for k, v in Dados.items():
    print(f'{"-":>3} {k} tem o valor de {v}')   
print(('-=')*30)