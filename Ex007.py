#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
#NOTAS OBTIDAS NO BIMESTRE
P1 = float(input('Qual é a nota referente a P1 do aluno ? '))
P2 = float(input('Qual é a nota referente a P2 do aluno ? '))
NL = float(input('Qual é a Nota Livre do aluno ?'))
S = float(input('Qual é a nota referente ao simulado do aluno ? '))
PP = float(input('Qual a nota referente ao projeto pedagógico do aluno? '))
print('A média que Lucas obteve no foi de:{:.2f}'.format((P1 + P2 + NL + S + PP)/5))
