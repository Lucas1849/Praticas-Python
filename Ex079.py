#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
verificação = 'S'
while True:
    valores = int(input('Digite um número: '))
    if valores in lista:
        print('Esse valor já está na lista, não sera contabilizado...')
        lista.remove(valores)
    lista.append(valores)
    lista.sort()
    verificação = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    if verificação  not in 'SsNn':
        str(input('Opção inválida.Tente novamente: [S/N]'))
    if verificação in 'Nn':
        break
print(f'A lista de número digitados é: {lista}')