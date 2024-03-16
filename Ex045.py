# Crie um programa que faça o computador jogar Jokenpô com você
#Randomizar Rock Paper Sisor
from random import randrange
from time import sleep
C = randrange(1,4)

#Escolha do Jogador
print('''Escolha entre Pedra, Papel ou Tesoura:
[1] Pedra
[2] Papel
[3] Tesoura   
''')
Opção = int(input('Sua opção: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)

if Opção == 1 and C == 2:
    print('Eu escolhi Papel, você Perdeu!')
elif Opção == 1 and C == 3:
    print('Eu escolhi Tesoura, você Venceu!')
elif Opção == 2 and C == 1:
    print('Eu escolhi Pedra, você Venceu!')
elif Opção == 2 and C == 3:
    print('Eu escolhi Tesoura, você Perdeu!')
elif Opção == 3 and C == 1:
    print('Eu escolhi Pedra, você Perdeu!')
elif Opção == 3 and C == 2:
    print('Eu escolhi Papel, você Venceu!')
elif Opção == C:
    print('Escolhemos a mesma opção, EMPATE! =_=')
else:
    print('Jogada inválida, tente novamente')