#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhiado pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
from time import sleep
v = random.randrange(0,5)

u = int(input('Vou pensar em um número de 0 a 5... Tente advinhar:'))
print('PROCESSANDO...')
sleep(3)
if u == v:
    print('Parabéns, você venceu')
else:
    print('Infelizmente, você perdeu, eu pensei no número {}'.format(v))