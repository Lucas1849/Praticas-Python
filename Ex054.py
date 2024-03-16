#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
YT = date.today().year

count = 0
tot = 0
for c in range(1, 8):
    N = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade  = YT - N
    
    if idade >= 21:
        count += 1
    else:
        tot +=1

print('{} pessoas já são maiores'.format(count))
print('{} pessoas ainda não atingiram a maioridade'.format(tot))

