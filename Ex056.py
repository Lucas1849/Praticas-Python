#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
maior = 0
velho = 0
count = 0
for c in range (1,5):
    print('-'*30)
    nome = str(input('Nome da {}ª pessoa: '.format(c))).strip().capitalize()
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = int(input('Sexo da {}ª pessoa [1 = MASCULINO] ou [2 = FEMININO]: '.format(c)))
    print('-'*30)
    soma += idade
#Mulheres com menos de 20
    if idade < 20:
        if sexo == 2:
            count +=1
#Homem mais velho
    if c == 1 and sexo == 1:
        maior = idade
        velho = nome
    if sexo == 1 and idade > maior:
        maior = idade
        velho = nome 
        
print('O {} é o homem mais velho do grupo, tendo {} anos'.format(velho,maior)) 
    

#Média idade do grupo

média = soma/4

print('A média de idade do grupo é de {:.1f} anos'.format(média))
print('{} mulheres tem menos que 20 anos neste grupo'.format(count))
