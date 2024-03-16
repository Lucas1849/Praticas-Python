#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(txt):
    Num = len(txt) + 4
    print('~'*Num)
    print(f'  {txt}')
    print('~'*Num)


escreva('Curso em vídeo')
escreva('Python')
escreva('Ghost')
escreva('Gustavo Guanabara')