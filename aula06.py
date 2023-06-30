# ----------------------------------------------------------------------------------------------------- //
# 1 - Crie um jogo de pedra, papel e tesoura, jogo deve dizer se o usuário ganhou ou perdeu e se empatar
# deve pedir ao usuário para selecionar uma opção nova
# ----------------------------------------------------------------------------------------------------- //

import auxiliaraula06

def principal():
    empate = 0
    while(empate == 0):
        jogada = int(input('As opções são:\n(1) Pedra\n(2) Papel\n(3) Tesoura\nEscolha uma opção: '))
        empate = auxiliaraula06.calcular(jogada)
if(__name__=="__main__"):
    principal()


# ----------------------------------------------------------------------------------------------------- //
# 2 - Crie um programa que conte quantas vogais há na string passada pelo usuário
# ----------------------------------------------------------------------------------------------------- //

texto = str(input('Informe uma palavra/frase: '))

cont = 0
for letra in texto:
    if letra in "aeiouAEIOU":
        cont += 1
print('A palavra/frase {} tem {} vogais'.format(texto, cont))

import random

def gerador_de_senhas():
    caracteres = 'abcdefghijklmnopqsrtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    tamanho = int(input('Qual o tamanho da senha que você deseja: '))
    senha = ''

    for i in range(tamanho):
        caract = random.choice(caracteres)
        senha+=caract
    print(senha)
if(__name__=='__main__'):
    gerador_de_senhas()
