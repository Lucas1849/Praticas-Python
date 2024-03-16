#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal   
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

H = float(input('Qual a sua altura ?'))
P = float(input('Qual o seu peso ?'))
IMC = P/H**2

if IMC < 18.5:
    print('Você está abaixo do peso, seu IMC é de {:.2f}'.format(IMC))
elif IMC >= 18.5 and IMC <= 25:
    print('O seu peso está ideal, seu IMC é de {:.2f}'.format(IMC))
elif  IMC > 25 and IMC <= 30:
    print('Você está com sobrepeso, seu IMC é de {:.2f}'.format(IMC))
elif IMC > 30 and IMC <= 40:
    print('Você está com obesidade, seu IMC é de {:.2f}'.format(IMC))
else:
    print('Você está com obesidade mórbida, seu IMC é de {:.2f}'.format(IMC))
