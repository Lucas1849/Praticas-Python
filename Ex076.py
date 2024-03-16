# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

prod = ('Lápis',2.00, 'Borracha',1.50, 'Tomate',3.50, 'Cadeira', 360, 'Leite',6.00, 'Banana', 5.75)
print('-='*30)
print(f'{"LOJAS LEONARDO":^60}')
print('-='*30)

for posi in range(0, len(prod)):
    if posi % 2 == 0:
        print(f'{prod[posi] :.<30}',end='')
    else: 
        print(f'{prod[posi]:>6.2f}')

