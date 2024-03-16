#Desafio 002 -Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas

nome = input('Qual o seu nome ?')
print('Boas vindas!', nome, 'É um prazer em te conhecer!')

#Outra forma de realizar
name = input('Qual é o seu nome ?')
print('Boas vindas {}!'.format(name))
