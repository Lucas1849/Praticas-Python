'''
Faça um programa que leia uma frase pelo teclado e mostre
1.Quantas vezes aparece a letra 'A'
2.Em que posição ela aparece a primeira vez
3.Em que posição ela aparece a última vez
'''
frase = str(input('Digite uma frase:').lower()).strip()

print('Nesta frase a letra A apareceu {} '.format(frase.count('a')))
print('Ela apareceu primeiro na posição {}'.format(frase.find('a'[:])+1))
print('Ela apareceu a última vez na posição {}'.format(frase.rfind('a'[:])+1))

# +1 foi utilizado para substituir o espaço 0 do index