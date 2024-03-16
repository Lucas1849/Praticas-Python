#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Qual é o valor da sua primeira nota?'))
nota2 = float(input('Qual o valor da sua segunda nota?'))
média = (nota1 + nota2)/2

if média < 5.0:
    print('Voce foi REPROVADO, pois sua média foi de {:.1f}'.format(média))
elif média >= 5.0 and média <= 6.9:
    print('Você está de RECUPERAÇÃO, pois sua média foi de {:.1f}'.format(média))
else:
    print('Parabéns, você foi APROVADO, pois adquiriu uma média de {:.1f}'.format(média)) 