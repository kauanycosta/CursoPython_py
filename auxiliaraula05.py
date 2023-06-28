import random
import aula05

def calcular(operacao, valor1, valor2):
    if(operacao == 1):
        resultado = valor1 + valor2
    elif(operacao == 2):
        resultado = valor1 - valor2
    elif(operacao == 3):
        resultado = valor1/valor2
    elif(operacao == 4):
        resultado = valor1 * valor2
    else:
        print('Valor incorreto')

    aula05.mostrar(resultado)

from random import randint # importa n aleatorios (int e float)
import re # modulo para trabalhar com expressões regulares

def sorteador(jogadas):
    lancamentos = []
    lado1 = 0
    lado2 = 0
    lado3 = 0
    lado4 = 0
    lado5 = 0
    lado6 = 0

    for i in range(0, jogadas):  
        random = (randint(1, 6))
        lancamentos.append(int(random))
        if(lancamentos[i] == 1):
            lado1 = lado1+1
        elif(lancamentos[i] == 2):
            lado2 = lado2+1
        elif(lancamentos[i] == 3):
            lado3 = lado3+1
        elif(lancamentos[i] == 4):
            lado4 = lado4+1
        elif(lancamentos[i] == 5):
            lado5 = lado5+1
        elif(lancamentos[i] == 6):
            lado6 = lado6+1
    print(lancamentos)
    aula05.mostrar(lado1,lado2,lado3,lado4,lado5,lado6)
    return lancamentos


    
