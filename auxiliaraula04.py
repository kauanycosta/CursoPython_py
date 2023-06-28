import aula04

def calcular(temp, opcao):
    if(opcao == 1):
        tempNova = (temp*1.8)+32
        tempLiteral = "Fahrenhardt"
        aula04.mostrar(tempNova, tempLiteral)
    elif(opcao == 2):
        tempNova = (temp-32)/1.8
        tempLiteral = "Celsius"
        aula04.mostrar(tempNova, tempLiteral)
    else:
        print("Essa não é uma opção válida")

def calcular2(valor):
    # Se o número for par, multiplicar por ele mesmo. Se for impar, fazer a raiz quadrada.
    if(valor>=500 and valor<=1000):
        if (valor % 2 == 0):
            valor = valor * valor
            print(f"O número foi multiplicado por ele mesmo.\nValor novo: %.2f"%(valor))
            # aula23junho.mostrar2(valor)
        else:
            valor = valor**0.5
            print(f"Foi calculada a raiz quadrada desse número.\nValor novo: %.2f"%(valor))
            # aula23junho.mostrar2(valor)
    else:
        print("Operação encerrada!")
