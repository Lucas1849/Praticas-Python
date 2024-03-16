#Crie um programa que simule o funcionamento de um caixa eletrônico. 
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Qual valor você deseja sacar? '))
resto = 0
while True:
  if valor >=50:
    nota50 = valor//50
    resto = valor - 50*nota50
    print(f'Você receberá {nota50} notas de R$50')
    if resto != 0 and resto >= 20:
      nota20 = resto//20
      resto = resto - 20*nota20
      print(f'Você receberá {nota20} notas de R$20')
    if resto != 0 and resto >=10:
      nota10 = resto//10
      resto = resto - 10*nota10
      print(f'Você receberá {nota10} notas de R$10')
    if resto != 0 and resto >= 1:
      nota1 = resto//1
      print(f'Você receberá {nota1} notas de R$1')
  elif valor >=20:
    nota20 = valor//20
    resto = valor - 20*nota20
    print(f'Você recebrá {nota20} notas de R$20')
    if resto != 0 and resto >=10:
      nota10 = resto//10
      resto = resto - 10*nota10
      print(f'Você recebrá {nota10} notas de R$10')
    if resto != 0 and resto >= 1:
      nota1 = resto//1
      print(f'Você recebrá {nota1} notas de R$1')
  elif valor >=10:
    nota10 = valor//10
    resto = valor - 10*nota10
    print(f'Você recebrá {nota10} notas de R$10')
    if resto != 0 and resto >=1:
      nota1 = resto//1
      print(f'Você recebrá {nota1} notas de R$1')
  else:
    nota1 = valor//1
    print(f'Você receberá {nota1} notas de R$1')
  break





    



