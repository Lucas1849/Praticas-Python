#Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.
lista = []
listapar = []
listaimpar = []
confirm = 'S'
while confirm in 'Ss':
    valores = int(input('Digite um número: '))
    lista.append(valores)
    if valores % 2 == 0:
        listapar.append(valores)
    else:
        listaimpar.append(valores)
    confirm = str(input('Deseja continuar a adicionar números [S/N] ? '))
    while confirm not in 'SsNn':
        confirm = str(input('Opção inválida.Deseja continuar [S/N] ? '))

print(f'A sua lista escolhida é : {lista}')
print(f'Os número pares presentes nessa lista são: {listapar}')
print(f'Os números ímpares presentes nessa lista são: {listaimpar}')