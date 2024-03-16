#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
lista = []
def sorteia():
    print(f'Sorteando 5 valores da lista: ',end='')
    for c in range(0,5):
        numb = randint(1,10)
        lista.append(numb)
    for p in lista:
        print(f'{p}',end='  ')
    print(f'PRONTO!')


def somaPar():
    soma = 0
    print(f'Somando os valores pares de {lista}, ',end='')
    for c in lista:
        if c % 2 == 0:
            soma += c 
    print(f'temos {soma}')

sorteia()
somaPar()
