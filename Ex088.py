#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
temp = []
Geral = []
jogos = int(input('Quantos jogos você deseja gerar ? '))
while True:
    cont = 1
    while cont <= 6:
        palpites = randint(1,60)
        if palpites not in temp:
            temp.append(palpites)
            temp.sort()
            cont += 1
    Geral.append(temp[:])
    temp.clear()
    if len(Geral) == jogos:
        break
print(f'Os {jogos} jogos que você pediu são: ')
for c in range(0,jogos):
    sleep(0.5)
    print(f'Jogo {c+1}: {Geral[c]}',end='\n')
    sleep(0.5) 
print(f'BOA SORTE!')