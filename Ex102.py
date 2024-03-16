#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, 
#que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show = False):
    """
    -----> Calcule o fatorial de um número
    1º parâmetro: Número a ser calculado
    2º parâmetro: Mostrar o processo envolvido na conta (OPCIONAL).
    return: O valor do fatorial de um número N
    """
    fact = 1
    for c in range(1,n+1):
        fact *= c
    if show == True:
        for c in range(1,n+1):
            print(f'{c}',end='')
            if c < n:
                print(' x ',end='')
            if c  == n:
                print(' = ',end= '')
    return f'{fact}'
            
           
              
print('-='*20)
help(fatorial)
print(fatorial(5,True))