def ficha(N='<desconhecido>',G=0):
    if N == '':
        N = '<desconhecido>'
    return f'O jogador {N} fez {G} gols no campeonato'


print('-='*30)
Jog = str(input('Nome do jogador: ')).capitalize().strip()
Gols = str(input('Quantos gols o jogador fez na partida ? '))
if Gols.isnumeric():
    Gols = int(Gols)
else:
    Gols = 0
print(ficha(Jog,Gols))