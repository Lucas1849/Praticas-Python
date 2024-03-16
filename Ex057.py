#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

S = str(input('Qual o seu sexo ? [M = Masculino] ou [F = Feminino]')).strip().upper()[0]

while S != 'M' and S != 'F':
    S = str(input('Opção escolhida inválida. Tente novamente: [M = Masculino] ou [F = Feminino]')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(S))