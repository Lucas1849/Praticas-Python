#Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

count = 0
while True:
    computador = randint(0,10)
    jogador = int(input('Digite um valor de 0 a 10: '))
    jog = str(input('Par ou ímpar ? ')).upper().strip()[0]
    soma = computador + jogador
    print('-'*30)
    if soma%2 == 0 and jog in 'Pp':
        print('Você venceu!')
        print(f'Você jogou {jogador} e eu pensei no número {computador}. Sendo a soma entre eles {soma} que é um número par.')
        print('-'*30)
        count += 1
    elif soma%2 == 0 and jog in 'Ii':
        print(f'Você perdeu, eu escolhi {computador} e você escolheu {jogador}. Sendo a soma entre eles {soma} que é um número par')
        print(f'Com um total de {count} vitórias consecutivas.')
        print('-'*30)
        break
    elif soma%2 != 0 and jog in 'Ii':
        print('Você venceu!')
        print(f'Você jogou {jogador} e eu pensei no número {computador}. Sendo a soma entre eles {soma} que é um número ímpar')
        print('-'*30)
        count += 1
    else:
        print(f'Você perdeu, eu escolhi {computador} e você escolheu {jogador}. Sendo a soma entre eles {soma} que é um número ímpar')
        print(f'Com um total de {count} vitórias consecutivas.')
        print('-'*30)
        break
print('Fim de jogo!')

        
   
