#função auxiliar para o exercicio da aula 03
import aula03

def nomeando(dia, mes, ano):
    match mes:
        case '01':
            nomeMes = "Janeiro"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '02':
            nomeMes = "Fevereiro"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '03':
            nomeMes = "Março"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '04': 
            nomeMes = "Abril"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '05': 
            nomeMes = "Maio"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '06':
            nomeMes = "Junho"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '07':
            nomeMes = "Julho"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '08': 
            nomeMes = "Agosto"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '09': 
            nomeMes = "Setembro"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '10': 
            nomeMes = "Outubro"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '11': 
            nomeMes = "Novembro"
            aula21junho.mostrar(dia, nomeMes, ano)
        case '12': 
            nomeMes = "Dezembro"
            aula21junho.mostrar(dia, nomeMes, ano)
        case _:
            print('Mês inválido')
