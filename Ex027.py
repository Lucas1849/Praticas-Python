'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''
nome = str(input('Qual o seu nome completo ?')).strip()
dividido = nome.split()
print('O seu primeiro nome é {}'.format(dividido [0]))
print('Seu último nome é {}'.format(dividido[len(dividido)-1]))

# 'len(objeto)' nos mostra o número total de index em uma cadeia de caracteres, começando do 0. Portanto len(objeto) -1 = Último index 