#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
count = 0
tot = 0
plus = 0
while True:
    print('-'*30)
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M = Masculino] e [F = Feminino: ]')).upper().strip()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Opção inválida, digite seu sexo novamente: ')).upper().strip()[0]
    print('-'*30)
    if idade > 18:
            count += 1
    if sexo in 'Mm':
        tot += 1 
    if sexo in 'Ff 'and idade < 20:
        plus += 1
    confirm = str(input('Deseja registrar mais dados? [S = sim] e [N = Não] ')).upper().strip()[0]
    while confirm not in 'SsNn':
        confirm = str(input('Opção inválida.Tente novamente [S = sim] e [N = Não]: '))
    print('-'*30)
    if confirm in 'Nn':
         break

print(f'Foram registradas {count} pessoas com mais de 18 anos.')
print(f'Foram registrados {tot} homens.')
print(f'Foram registradas {plus} mulheres com menos de 20 anos.')
