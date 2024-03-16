#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
Jogadores = {}
Jogadores['1º jogador'] = randint(1,6)
Jogadores['2º jogador'] = randint(1,6)
Jogadores['3º jogador'] = randint(1,6)
Jogadores['4º jogador'] = randint(1,6)
ranking = {}
for k,v in Jogadores.items():
    sleep(0.5)
    print(f'O {k} tirou {v}')
    sleep(0.5)

ranking = sorted(Jogadores.items(), key = itemgetter(1), reverse = True)
print(f'{"== RANKING DOS JOGADORES ==":>30}')
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'{i+1}º lugar é o {v[0]} que tirou {v[1]} ')
    sleep(0.5)