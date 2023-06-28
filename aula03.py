# ----------------------------------------------------------------------------------------------------- //
#1 - Fazer um programa que peça a data de nascimento em números e retorne uma frase de saída:
#Exemplo: "Você nasceu em 25 de setembro de 1999"
# ----------------------------------------------------------------------------------------------------- //

import auxiliar21junho
def principal():
    data = str(input("Informe a sua data de nascimento (dd/mm/aaaa): "))
    dataLimpa = data.split('/')
    dia = dataLimpa[0]
    mes = dataLimpa[1]
    ano = dataLimpa[2]
    auxiliar21junho.nomeando(dia, mes, ano)

if(__name__=='__main__'):
    principal()

def mostrar(dia, nomeMes, ano):
    print(f"Você nasceu em {dia} de {nomeMes} de {ano}")


# ----------------------------------------------------------------------------------------------------- //
# Inicio do exemplo MenuJogos
# ----------------------------------------------------------------------------------------------------- //

import random

def jogar():
    print('Escolha cara ou coroa: ')
    numeroDoJogador = int(input('(1)Cara (2)Coroa'))
    numeroDeJogadas = int(input('numero de jogadas: '))
    contVitoria = 0
    contDerrota = 0
    for i in range(numeroDeJogadas):
        moeda = random.randint(1,2)
        if(numeroDoJogador == moeda):
            contVitoria = contVitoria + 1
        else:
            contDerrota = contDerrota + 1
    print('Voce ganhou {} vezes de {}'.format(contVitoria, numeroDeJogadas))
    print('Voce perdeu {} vezes de {}'.format(contDerrota, numeroDeJogadas))
if(__name__ == '__main__'):
    jogar()

print(__name__)
def novafuncao():
    print('ola')
