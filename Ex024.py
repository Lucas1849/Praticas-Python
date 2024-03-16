 #Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'

cidade = str(input('Digite o nome de um cidade: ').title()).strip()
primeiro = cidade.split()
print('A cidade que voce digitou começa com o nome Santos ? {}'.format('Santo' in primeiro[0]))