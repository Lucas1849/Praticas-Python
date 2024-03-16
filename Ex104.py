#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
#Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(n):
    n = input('Digite um número: ')
    if n.isnumeric():
        return n
    else:
        while n.isnumeric() == False:
            print(f'\033[0;31mERRO ! Digite um número válido.')
            n = input(f'\033[mDigite um número:  ')
        return f'\033[m{n}'


print('-='*30)
Numb = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {Numb}')