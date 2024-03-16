#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print(f'\033[0;31mERRO! Digite um número inteiro válido:  \033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mUsuário prefiriu não digitar esse número.\033[m')
            return 0
        else:
            return n
    

def leiaFloat(msg):
    while True:
        try:
            numb = float(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Digite um número real válido.  \033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mUsuário preferiu não digitar esse número.')
            return 0
        else:
            return numb


inteiro = leiaInt('Digite um Inteiro: ')
flutuante = leiaFloat('Digite um número Real: ')
print(f'O número inteiro digitado foi {inteiro} e o real foi {flutuante}')