'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro
alunos e mostre a ordem serteada
'''
import random

A1 = 'Gabriel'
A2 = 'Lucas'
A3 = 'Leonardo'
A4 = 'Tomaz'
Alunos = [A1, A2, A3, A4]
random.shuffle(Alunos)
print('A ordem de apresentação será {}'.format(Alunos))
