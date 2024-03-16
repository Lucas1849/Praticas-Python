#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
    Numb = list(num)
    print('Analisando os valores...')
    for c in Numb:
        print(f'{c} ',end='')
    print(f'foram informados {len(Numb)} valores ao todo.')
    if len(num) != 0:
        print(f'O maior valor informado é {max(Numb)}')
    else:print(f'O maior valor informado é 0')



def linha():
    print('-='*15)


linha()
maior(2,9,4,5,7,1)
linha()
maior(4,7,0)
linha()
maior(1,2)
linha()
maior(6)
linha()
maior()
linha()