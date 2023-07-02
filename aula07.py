# ----------------------------------------------------------------------------------------------------- //
# 1 - Escreva uma função que receba uma lista de palavras como parâmetro e retorna
# a quantidade de palavras que possuem mais de cinco letras
# ----------------------------------------------------------------------------------------------------- //
import auxiliaraula07

def principal():
    palavras = ['ola', 'kauany', 'queridos', 'testezao', 'teste', 'oi', 'laranja']
    quantidade = auxiliaraula07.letras(palavras)
    print('A quantidade de palavras que contém mais do que 5 cinco letras é:',quantidade)
if(__name__=='__main__'):
    principal()

# ----------------------------------------------------------------------------------------------------- //
# 2 - Escreva uma função que receba uma lista como argumento e retorna uma nova lista contendo apenas os
#elementos únicos, removendo as duplicatas
# ----------------------------------------------------------------------------------------------------- //
def principal():
    listaPrin = ['oi', 'teste', 'oi', 'palavra', 'teste']
    semDuplicatas = listaPrin.copy()
    semDuplicatas = list(set(semDuplicatas))
    print('A lista principal é:',listaPrin)
    print('A lista sem duplicatas é:',semDuplicatas)
if(__name__=='__main__'):
    principal()

# ----------------------------------------------------------------------------------------------------- //
# 3 - Criar suas próprias funções para calcular o desconto em uma determinada compra. 
# A função deve receber o valor total da compra e o percentual de desconto como 
# parâmetros, calcular o valor do desconto e retornar o valor final a ser pago
# ----------------------------------------------------------------------------------------------------- //

def principal():
    valorInicial = float(input('Informe o valor da compra: R$'))
    descontoPercentual = float(input('Informe o percentual de desconto na compra: '))
    valorFinal,descontoReal = auxiliaraula07.calcularDesconto(valorInicial, descontoPercentual)
    print(f'O desconto é de R${descontoReal:,.2f} e o valor final da compra é: R${valorFinal:,.2f}')
if(__name__=='__main__'):
    principal()
  
# ----------------------------------------------------------------------------------------------------- //
""" 4 - Desenvolva um programa que armazene 4 notas em uma lista e que calcule a média final. 
#caso a média seja igual ou superior a 7, aprovado, caso contrario, o programa pede mais
#uma nota e armazena e recalcula a media. Caso a nova média seja igual ou superior a 5, aprovado,
#caso contrário, reprovado """
# ----------------------------------------------------------------------------------------------------- //
def principal():
    quantidadeNotas = range(4)
    notas = []
    somaNotas = 0
    parametro = 0
    for i in quantidadeNotas:
        parametro+=1
        notas.append(float(input('Informe a nota {}: '.format(parametro))))
        somaNotas = somaNotas+notas[i]
    resultado = auxiliaraula07.calcularMedia(somaNotas)
    print("Você esta: ", resultado)
if(__name__=='__main__'):
    principal()
