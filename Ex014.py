#Realize um programa que converta temperaturas de ºC para F e para K

T = float(input('Digite a temperatura em ºC: '))
F = T*9/5 + 32
K = T + 273
print('A temperatura em Fahrenheit é igual a {} F'.format(F))
print('A temmperatura em Kelvin é igual a {} K'.format(K))