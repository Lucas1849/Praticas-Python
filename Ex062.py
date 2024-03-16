#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
#a10 = a1 + (10*r - 1*r) 
n = a1
count = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while count <= total:
        count += 1
        print('{}'.format(n),end='')
        print(' - ' if count <= total else '',end='')
        n += r
    mais = int(input('\nQuantos termos você quer ver ? '))
print('Obrigado por usar PA calculator!')