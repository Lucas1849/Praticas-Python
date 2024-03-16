#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
#No final, mostre a lista ordenada na tela.

numb = []
for n in range (0,5):
    valores = int(input('Digite um número: '))
    if n == 0 or valores > numb[-1]:
        numb.append(valores)
        print(f'Adicionado ao fim da lista...')
    else:
        pos = 0
        while pos < len(numb):
            if valores <= numb[pos]:
                numb.insert(pos,valores)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
    
print(numb)


