#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão desta PA: '))
a10 = a1 + 10*r - 1*r
n = a10 +1
print('Os dez primeiros termos dessa PA são:')
for c in range(a1,n,r):
    print(c, end=', ')
