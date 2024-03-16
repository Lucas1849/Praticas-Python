#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas 
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)
def notas(*n, sit=False):
    """
    ---> notas(*n, sit=False)
    A função notas irá coletar as notas dos alunos e organizar eles. Mostrando a maior nota, a menor nota e a média. Caso queira saber a situação das notas ---> notas(1,2,3,sit=True)
    1º parâmetro: parâmetro variável, podendo ser adicionadas várias notas.
    2º parâmetro: parâmetro opcional que analisará as notas e retornará se a situação do aluno é ruim(média < 6), boa(6 <= média <= 7 ) ou ótima(média > 7)
    return : Retornará A quantidade de notas analisadas, a maior e a menor nota mostrando também uma média dessas notas.Sendo a situação uma parâmetro OPCIONAL da função.
    """
    Dados = {}
    n = list(n)
    Quant = len(n)
    Maior = max(n)
    Menor = min(n)
    Média = sum(n)/Quant
    Dados["Total"] = Quant
    Dados["Maior"] = Maior
    Dados["Menor"] = Menor
    Dados["Média"] = Média
    if sit == True:
        if Média < 6:
            situação = 'RUIM'
        elif 6 <= Média <= 7:
            situação = 'BOA'
        else:
            situação = 'ÓTIMA'
        Dados["Situação"] = situação
    return Dados
        
        
resp = notas(5.5,9.5,10,6.5,sit=True)
print(resp)