'''
Crie um programa que leia o nome completo de uma pessoa e mostre :
1. O nome com todas a letras maiúsculas
2. O nome com todas minúsculas
3. Quantas letra ao todo (sem considerar espaços)
4. Quantas letras tem o primeiro nome
'''

nome = str(input('Qual é o seu nome completo ?')).strip()
# 1
print('Seu nome com todas as letras maiúsculas é {}'.format(nome.upper()))
# 2
print('Seu nome com todas as letras minúsculas é {}'.format(nome.lower()))
# 3
lista = nome.split()
print('Seu nome possui {} letras'.format(len(''.join(lista))))
# 4
print('Seu primeiro nome possui {} letras'.format(len(lista [0])))
