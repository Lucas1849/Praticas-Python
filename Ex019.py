'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome 
deles e escrevendo o nome do escolhido
'''
import random

A1 = 'Gabriel'
A2 = 'Lucas'
A3 = 'Leonardo'
A4 = 'Tomaz'
Alunos = A1, A2, A3, A4

print('O aluno sorteado para apagar o quadro foi o {}'.format(random.choice(seq= Alunos)))
