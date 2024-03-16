#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))
count = 0
for num in range(1,n+1):
    x = n%num
    if x == 0:
        count += 1
        
if count == 2:
    print('Este número é primo!')
else:
    print('Esse número não é primo')
           
            
    
   
