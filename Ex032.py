#Faça um programa que leia um ano qualquer e msotre se ele é BISSEXTO
from datetime import date
ano = int(input('Digite um ano qualquer ou digite 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
b = ano%4
B = ano%400
c = ano%100


if  b == 0 != c or B == 0:
    print('O ano escolhido é Bixesto')
else:
    print('O ano escolhido não é Bixesto')


