def letras(palavras):
    count = 0
    quantidadePalavras = len(palavras)
    maisdecinco = 0
    for i in range (quantidadePalavras):
        for j in palavras[i]:
            count = count + 1
        if (count>5):
            maisdecinco = maisdecinco + 1
        count = 0
    return maisdecinco

def calcularDesconto(valorInicial, descontoPercentual):
    descontoReal = (descontoPercentual*valorInicial)/100
    valorFinal = valorInicial - descontoReal
    return valorFinal,descontoReal

def calcularMedia(somaNotas):
    media = somaNotas/4
    print("A média é:", media)
    if (media>=7):
        resultado = "Aprovado"
    else:
        provaFinal = float(input('Aluno em recuperação.\nInforme mais uma nota para avaliação: '))
        somaNotas += provaFinal
        mediaFinal = somaNotas/5
        print("Nova média: ", mediaFinal)
        if (mediaFinal>=5):
            resultado = "Aprovado"
        else:
            resultado = "Reprovado"
    return resultado
