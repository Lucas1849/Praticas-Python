#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
comp = randint(0,10)

jog = int(input('Tente advinhar no número que pensei de 1 a 10: '))
count = 0
while jog != comp:
    if jog > comp:
        print('Tente um número menor...')
    elif jog < comp:
        print('Tente um número maior...')
    jog = int(input('Você errou!, tente novamente: '))
    count += 1

if 1<= count + 1 <= 3:
    print('AH DROGA, você é bom! me venceu com apenas {} tentativa/s'.format(count + 1))
elif  count <= 5:
    print('Você me venceu com {} tentativas, parabéns!'.format(count + 1))
else:
    print('Você me venceu com {} tentativas'.format(count + 1))

