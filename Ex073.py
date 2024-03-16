#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Cruzeiro


time = ('Palmeiras','Grêmio','Atlético-MG',	'Flamengo','Botafogo','Bragantino','Fluminense','Athletico-PR','Internacional','Fortaleza','São Paulo','Cuiabá'
,'Corinthians','Cruzeiro','Vasco','Bahia','Santos','Goiás','Coritiba','América-MG')
primeiros = time[0:5]
ultimos = time[16:]
ordem = sorted(time)
Ps = time.index('Cruzeiro')+1
print(f'Os cinco primeiros times da tabela do brasileirão são:{primeiros}')
print(f'Os 4 ultimos colocados são: {ultimos}')
print(f'Os times em ordem alfabética são: {ordem}')
print(f'O time do Cruzeiro está na {Ps}ª posição ')

