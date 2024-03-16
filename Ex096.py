#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def área(a,b):
    A = a * b
    print(f'A área do terreno escolhido {a}x{b} é {A}m²')


def título():
    print('-='*30)
    print(f'{"Controle de terrenos":^60}')
    print('-='*30)


título()
área(float(input('Largura (m): ')),float(input('Comprimento (m): ')))
