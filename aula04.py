# ----------------------------------------------------------------------------------------------------- //
# 1 - Fazer um programa que converta a temperatura digitada pelo usuário para celsius ou para 
# fahrenhardt dependendo da opção usada
# ----------------------------------------------------------------------------------------------------- //
import auxiliaraula04
def principal():
    temp = float(input("Informe a temperatura: "))
    opcao = int(input("Converter para:\n(1) Fahrenhardt\n(2) Celsius\nEscolha: "))
    auxiliaraula04.calcular(temp, opcao)
if(__name__=='__main__'):
    principal()

def mostrar(tempNova, tempLiteral):
    print(f"A sua temperatura convertida para {tempLiteral} é {tempNova}")

# ----------------------------------------------------------------------------------------------------- //
# 2 - Escreva um programa que peça ao usuário um valor de 500 a 1000, controlar essa entrada.
# Se o número for par, multiplicar por ele mesmo. Se for impar, fazer a raiz quadrada.
# ----------------------------------------------------------------------------------------------------- //

def principal2():
    valor = 501
    while(valor>=500 and valor<=1000):
        valor = float(input("Escolhe um valor que esteja entre o intervalo de 500 até 100.\nInforme o valor: "))
        auxiliaraula04.calcular2(valor)
if(__name__=="__main__"):
    principal2()
