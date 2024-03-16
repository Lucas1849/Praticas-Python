#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
 
nome = str(input('Qual o seu nome ?').title()).strip()

print('Seu nome possuiu Silva ? {}'.format('Silva' in nome))