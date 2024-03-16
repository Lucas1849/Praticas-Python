#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(N):
  from datetime import datetime
  Today = datetime.today().year
  idade = Today - N
  if idade < 16:
    return f'Com {idade} anos: voto NEGADO'
  elif 16 <= idade < 18 or idade > 65:
    return f'Com {idade} anos: voto OPCIONAL'
  else:
    return f'Com {idade} anos: voto OBRIGATÓRIO'
  
  


print(voto(int(input('Data de nascimento: '))))
