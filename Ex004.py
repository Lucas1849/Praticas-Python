#Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

thing = input('Digite algo:') 

print('O tipo primitivo dessa formatação é:', type(thing))
print('Só tem espaços ?', thing.isspace())
print('É um número ?', thing.isnumeric())
print('É afabético ?',thing.isalpha())
print('É alfanumérico ?', thing.isalnum())
print('Está em maiúsculas ?', thing.isupper())
print('Está em minúsculas ?', thing.islower())
print('Está capitalizado ?', thing.istitle())
