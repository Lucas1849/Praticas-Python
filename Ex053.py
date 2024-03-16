#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 
#Exemplos de palíndromos:APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

f = input('Digite uma frase: ').upper().split()
Join = ''.join(f)
invert = Join[::-1]
if invert == Join:
    print(f'{Join} invertido fica {invert}')
    print(f'Temos um palíndromo!')
#Professor 
inverso = ''
for invertido in range (len(Join) - 1, -1, -1):
    inverso += Join[invertido]
