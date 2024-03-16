#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import getrandbits
tulp = (getrandbits(2),getrandbits(4),getrandbits(8),getrandbits(5),getrandbits(10))
print(f'Os valores sorteados foram {tulp[0]} {tulp[1]} {tulp[2]} {tulp[3]} {tulp[4]}')
'''orgn = sorted(tulp)
print(f'O maior valor é {orgn[4]}')
print(f'O menor valor é {orgn[0]}')
    '''
#Outra forma de colocar o maior e menor nas tuplas
print(f'O maior valor é {max(tulp)}')
print(f'O menor valor é {min(tulp)}')