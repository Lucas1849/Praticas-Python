#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
count = 0
confirm = 'S'
while confirm not in 'Nn':
    valores = int(input('Digite um número: '))
    lista.append(valores)
    count += 1
    confirm = str(input('Deseja adicionar mais número a sua lista [S/N] ? ')).upper().strip()[0]
    while confirm not in 'SsNn':
        if confirm not in 'SsNn':
            confirm = str(input('Resposta inválida.Quer continuar [S/N]? ')).upper().strip()[0]
print(f'Foram digitados {count} número nessa lista.')
lista.sort(reverse=True)
print(f'A lista em ordem descrescente é {lista}.')
if 5 in lista:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não está na lista')
