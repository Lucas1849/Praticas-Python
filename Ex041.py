#A Confederação Nacional de Natação precisa de um programa que leia o ano de nasicmento de um atleta e mostre sua categoria de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR 
# Acima de 25: MASTER

from datetime import date
ano = int(date.today().year)
nascicmento = int(input('Qual é seu ano de nascimento ?'))
idade = ano - nascicmento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Você está na categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Você está na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Você está na categoria JUNIOR')
elif idade > 19 and idade <= 25:
    print('Você está na categoria SÊNIOR')
elif idade > 25:
    print('Você está na categoria MASTER')
    