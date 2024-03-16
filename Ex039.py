#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alista ao serviço militar.
#Se é a hora de se alistar
#Se já passou do tempo de alistamento.
#Seu programa deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano de seu nascimento ?'))
idade = atual - nascimento 

if idade < 18:
    print('Sua hora de se alistar no exército ainda não chegou, você têm {} anos, seu alistamento acontecerá em {}'.format(idade,nascimento + 18))
    print('Faltam {} anos para o seu alistamento'.format(18 - idade))
elif idade == 18:
    print('Sua hora de se alistar para o exército brasileiro chegou! ')
else:
    print('Seu alistamento para o exército já deveria ter sido realizado, você têm {} anos, seu alistamento foi em {}'.format(idade,nascimento + 18))
    print('Já se passaram {} anos do seu alistamento'.format(idade - 18))