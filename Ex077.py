#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Esposa','Felicidade','Trabalho','Estudo','Esforço','Academia','Pensamentos','Aniversario','Faculdade','Empenho','Gato')

for words in palavras:
    print(f'\nNa palavras {words.upper()} há as vogais: ',end='')
    for vogais in words:
        if vogais in 'AaEeIiOoUu':
            print(f'{vogais}..',end='')