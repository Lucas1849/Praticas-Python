#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
atual = datetime.today().year
Dados = {}
Dados['Nome'] = input('Nome: ').capitalize()
Dados['Nascimento'] = int(input('Ano de nascimento: '))
Dados['Idade'] = atual - Dados['Nascimento']
Dados['CTPS'] = int(input('Carteira de Trabalho (0 = não tem): '))
if Dados['CTPS'] != 0:
    Dados['Contratação'] = int(input('Ano de contratação: '))
    Dados['Salário'] = float(input('Salário: R$'))
    Dados['Aposentadoria'] = Dados['Idade'] + ((Dados['Contratação'] + 35) - atual)
del Dados['Nascimento']
for k, v in Dados.items():
    print(f'{"-":>5} {k} tem valor de {v}')
