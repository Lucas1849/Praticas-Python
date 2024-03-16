#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
Num = int(input('Digite um número (0-20) para mostra-lo por extenso: '))
if  Num > 20 or Num < 0:
    Num = int(input('Opção inválida, tente novamente (0-20): '))

numbers = ('Zero', 'Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Deszessete','Dezoito','Dezenove','Vinte')
print(f'O número {Num} escrito por extenso é {numbers[Num]}')
