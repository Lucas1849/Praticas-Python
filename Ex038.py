#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

primeiro = float(input('Digite o primeiro valor:'))
segundo = float(input('Digite o segundo valor:'))

if primeiro > segundo:
    print('O primeiro valor {:.2f} é maior'.format(primeiro))
elif segundo > primeiro:
    print('O segundo valor {:.2f} é maior'.format(segundo))
else:
    print('O valor {} e {} são iguais! Portanto não existe um maior.'.format(primeiro, segundo))
