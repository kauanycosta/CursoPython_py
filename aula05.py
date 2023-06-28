# ----------------------------------------------------------------------------------------------------- //
# 1- Faça um programa que peça ao usuário qual operação matemática ele deseja realizar entre (+, -, /, *)
# após selecionada o usuário deve informar os valores para realizar as operações e por final printar
# # o resultado da operação as operações deverão ser feitas em outro arquivo e importadas para o arquivo principal
# ----------------------------------------------------------------------------------------------------- //
import auxiliaraula05

def principal():
  operacao = int(input('Escolha uma operação matemática:\n(1) +\n(2) -\n(3) /\n(4) *\nQual operação você escolhe? '))
    valor1 = int(input('Informe o primeiro valor da sua conta: '))
    valor2 = int(input('Informe o segundo valor da sua conta: '))
    auxiliaraula05.calcular(operacao, valor1, valor2)
if(__name__ == '__main__'):
    principal()

def mostrar(resultado):
    print('O resultado da sua conta é: {}'.format(resultado))

# ----------------------------------------------------------------------------------------------------- //
# 2 - Faça um programa que simule um dado de 6 lados e que peça ao usuário o número de vezes que ele deseja
# lançar o dado, no final o programa deverá dizer quantas vezes caiu cada lado no número de vezes
# que o jogador pediu para jogar
# ----------------------------------------------------------------------------------------------------- //

def principal2():
    jogadas = int(input('Quantas vezes você deseja jogar o dado? '))
    auxiliaraula05.sorteia(jogadas)
if(__name__=='__main__'):
    principal2()

def mostrar(lado1,lado2,lado3,lado4,lado5,lado6):
    print('O lado 1 do dado apareceu {} vezes'.format(lado1))
    print('O lado 2 do dado apareceu {} vezes'.format(lado2))
    print('O lado 3 do dado apareceu {} vezes'.format(lado3))
    print('O lado 4 do dado apareceu {} vezes'.format(lado4))
    print('O lado 5 do dado apareceu {} vezes'.format(lado5))
    print('O lado 6 do dado apareceu {} vezes'.format(lado6))
