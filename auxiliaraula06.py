import aula06
import random
from random import randint

def calcular(jogada):
    random = (randint(1, 3))
    jogadaMaquina=(int(random))
    empate = 0

    if (jogadaMaquina == 1 and jogada == 3):
        print("Você perdeu! Eu joguei pedra.")
    elif (jogadaMaquina == 2 and jogada == 1):
        print("Você perdeu! Eu joguei papel.")
    elif (jogadaMaquina == 3 and jogada == 2):
        print("Você perdeu! Eu joguei tesoura.")
    elif(jogadaMaquina == jogada):
        print("Empate!\nVamos jogar de novo!")
        empate = 0
        return empate
    else:
        print("Você ganhou!!!")
