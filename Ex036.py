#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o slário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

casa = float(input('Qual o valor da casa que você pretende comprar ?'))
salário = float(input('Qual o seu faturamento mensal ?'))
anos = int(input('Em quantos anos você pretende pagar ?'))
mês = anos * 12
prestação = casa//mês

if prestação <= salário * 0.3:
    print('O seu empréstimo bancário foi realizado com sucesso, a prestação mensal ficou em {:.2f}'.format(prestação))
else:
    print('O seu empréstimo foi negado!')
