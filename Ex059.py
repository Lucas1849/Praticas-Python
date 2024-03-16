'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''


n1 = float(input('Digite o primeiro valor: '))
n2  = float(input('Digite o segundo valor: '))


Op = int(input(''' Oque você pretende realizar com esses números 
 [ 1 ] Somar
            
 [ 2 ] Multiplicar 
           
 [ 3 ] Saber qual é o maior
           
 [ 4 ] Escolhar Novos Números
            
 [ 5 ] Sair do progama   
: '''))


while Op != 5:
  if Op == 1:
    soma = n1 + n2
    print('A soma dos números {} e {} é {}'.format(n1,n2,soma))
  elif Op == 2:
    multi = n1 * n2
    print('A multiplicação dos números {} e {} é {}'.format(n1,n2,multi))
  elif Op == 3:
    if n1 > n2:
      maior = n1
    elif n2 > n1:
      maior = n2
      print('O maior número entre {} e {} é {}'.format(n1,n2,maior))
    else:
      print('Os números são iguais! Não existe um maior')
  elif Op == 4:
    n1 = float(input('Digite um novo número: '))
    n2 = float(input('Digite um novo número: '))
  elif Op > 5:
    print('Opção inválida, tente novamente:')
    n1 = float(input('Digite o primeiro valor: '))
    n2  = float(input('Digite o segundo valor: '))
  Op = int(input(''' Oque você pretende realizar com esses números 
[ 1 ] Somar
            
[ 2 ] Multiplicar 
           
[ 3 ] Saber qual é o maior
           
[ 4 ] Escolhar Novos Números
            
[ 5 ] Sair do progama 
: '''))
print('Obrigado por usar o programa! ')
