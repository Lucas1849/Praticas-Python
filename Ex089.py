#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
temp = []
Dados = []
Boletim = []
cont = 0
confirm = 'S'
while confirm in 'Ss':
    print(('-=')*30)
    nome = input('Nome do aluno: ').capitalize()
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    print(('-=')*30)
    média = (nota1 + nota2) / 2 
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    Dados.append(temp[:])
    temp.clear()
    temp.append(nome)
    temp.append(média)
    Boletim.append(temp[:])
    temp.clear()
    confirm = input('Quer continuar [S/N] ? ').upper().strip()[0]
    while confirm not in 'SsNn':
        confirm = input('Opção inválida. Quer continuar [S/N] ? ').upper().strip()[0]
print('{:^2} {:^10} {:^30}'.format('Nº','Nome','Nota'))
while cont != len(Boletim):
    for D in Boletim:
        print(f'{cont:^2}',end='')
        print(f' {D[0]:^11}',end='')
        print(f' {D[1]:.>16}',end='\n')
        cont += 1

while True:
    verific = int(input('Mostrar nota de qual aluno ? (999 = Parar) '))
    if verific == 999:
        break
    if verific <= cont:
        print(('-=')*30)
        print(f'{Dados[verific][0]} tirou as notas {Dados[verific][1]} e {Dados[verific][2]}')
        print(('-=')*30)

print('Finalizando....')
print('Obrigado por utilizar nossos recursos !')
