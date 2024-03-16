#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0

for c in range(1,6):
    peso = int(input('Qual o seu peso ? '))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
        
print('O maior peso lido é de {} Kg'.format(maior))
print('O menor peso lido é de {} Kg'.format(menor))
    
    

        
    


        
        

