'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2m² 
'''
L = float(input('Qual é a largura da parede em metros ?'))
A = float(input('Qual é a altura da parede em metros ?'))
área = L*A
print('A área desta parede é de {}m², sendo assim necesário {:.2F} litros de tinta para pintá-la por completo'.format(área, área/2 ))