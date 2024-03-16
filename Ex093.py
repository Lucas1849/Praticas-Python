#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
Dados = {}
Dados['Nome'] = input('Nome do jogador: ').capitalize()
Partidas = int(input(f'Quantas partidas {Dados["Nome"]} jogou ? '))
soma = 0
Gols = []
for c in range(0,Partidas):
    pontuação = int(input(f'Quantos gols o jogador {Dados["Nome"]} fez na {c+1}ª partida ? '))
    Gols.append(pontuação)
    soma += pontuação
    Dados['Gols'] = Gols
    Dados['Total'] = soma
print("-="*30)
print(Dados)
print("-="*30)
for k,v in Dados.items():
    print(f'O campo {k} tem o valor {v}')
print("-="*30)
print(f'O jogador {Dados["Nome"]} jogou {Partidas} partidas.')
for c, i in enumerate(Gols):
    print(f'{"=>":>5} Na {c+1}ª partida, fez {i} gols.')
print(f'Foi um total de {Dados["Total"]} gols')
print("-="*30)
