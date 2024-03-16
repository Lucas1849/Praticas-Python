#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
Jogadores = {}
Gols = []
Geral = []
total = 0
confirm = 'S'
while confirm in 'Ss':
    Gols.clear()
    Jogadores.clear()
    Jogadores['Nome'] = input('Nome: ').capitalize()
    partidas = int(input(f'Quantas partidas {Jogadores["Nome"]} jogou ? '))
    for c in range (0,partidas):
        Golcont = int(input(f'Quantos gols {Jogadores["Nome"]} fez na {c+1}ª partida ? '))
        Gols.append(Golcont)
        Jogadores['Gols'] = Gols.copy()
        total += Golcont 
        Jogadores['Total'] = total
    Geral.append(Jogadores.copy())
    confirm = input('Deseja continuar [S/N] ? ')
    while confirm not in 'SsNn':
        confirm = input('Opção inválida.Deseja continuar [S/N] ? ').upper().strip()[0]

print('-='*30)
print(f'{"cod":<10} {"Nome":<10}{"Gols":<29}{"Total":<38}')
for c, v in enumerate(Geral):
    print(f'{c:<10}{v["Nome"]:<11}',end='')
    print(f'{str(v["Gols"]):<30}',end='')
    print(f'{v["Total"]:<40}',end='')
    print()
print('-='*30)

while True:
    escolha = int(input('Qual jogador voce deseja ver o aproveitamento (999 = parar) ? '))
    while escolha > len(Geral)- 1:
        escolha = int(input('Opção inválida.Qual jogador você deseja ver o aproveitamento (999 = parar)? '))
        if escolha == 999:
            break
    if escolha == 999:
        break
    print(f'{"-LEVANTAMENTO DO JOGADOR-":>5} {Geral[escolha]["Nome"]}')
    cont =0
    for c in range(0,len(Geral[escolha]['Gols'])):
        print(f'Na {c+1}ª partida fez {Geral[escolha]["Gols"][cont]} gols')
        cont += 1
