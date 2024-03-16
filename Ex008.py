#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros(conversor de medidas)

m = float(input('Digite um valor em metros ?'))
print('A medida de {}m corresponde a\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(m, m/10**3, m/10**2, m/10, m*10, m*10**2, m*10**3))
