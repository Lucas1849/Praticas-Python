#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista  = []
for c in range (0,5):
    valores = int(input(f'Digite um valor na posição {c}: '))
    lista.append(valores)

#Maior e menor
print(f'O maior valor digitado foi {max(lista)} e está nas posições: ',end='')
for p, v in enumerate(lista):
    if v == max(lista):
        print(f'{p}...',end = '')
print()
print(f'O menor valor digitado foi {min(lista)} e está nas posições: ',end='')
for p, v in enumerate(lista):
    if v == min(lista):
        print(f'{p}...',end='')