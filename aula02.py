#----------------------------------------------------------------------------------------------------- // //
# 1 - Somar todos os multiplos de 3 e de 5 que existem nesse valor. 
# numero = int (input('\nInforme um número:'))
# mult3 = 0;
# mult5 = 0;
# soma = 0;
# i = 0;
#----------------------------------------------------------------------------------------------------- // //

for i in range(numero+1):
  if(i%3==0):
        mult3 = mult3 + i
    if (i%5==0):
        mult5 = mult5 + i

soma = mult3+mult5
print('A soma dos múltiplos de 3 é: ',(mult3))
print('A soma dos múltiplos de 5 é: ',(mult5))
print('A soma de ambos é: ',(soma))

#----------------------------------------------------------------------------------------------------- // //
# 2 - Somar todos os números pares que existem nesse valor.
#----------------------------------------------------------------------------------------------------- // //
numero = int(input('\nInforme um número: '))
i = 0
soma =0

for i in range(numero+1):
  if(i%2==0):
        print('O número %d é par'%i)
        soma = soma + i
print('A soma dos pares é: ',(soma))

#----------------------------------------------------------------------------------------------------- // //
#3 - Printar se os números são par ou impar até o valor
#----------------------------------------------------------------------------------------------------- // //
numero = int(input('\nInforme um número: '))
i = 0

for i in range(numero+1):
    if(i%2==0):
        print('O número %d é par'%i)
    if(i%2!=0):
        print('O número %d é ímpar'%i)

#----------------------------------------------------------------------------------------------------- // //
# 4 - Calcular e imprimir o fatorial do número informado.
#----------------------------------------------------------------------------------------------------- // //
numero = int(input('Informe um número: '))
i = 1
fatorial = 1

for i in range(1,numero+1):
  fatorial *= i
print('O fatorial do número é: %d'%fatorial)

import random

def jogar():

    print('*******************************')
    print('*****jogo de adivinhação*******')
    print('*******************************')

    numero_secreto_comp = random.random()

    random.seed(100)
    numero_secreto = random.randrange(1,101)

    print(numero_secreto_comp)
    print(numero_secreto)

    numero_tentativas = 3
    print('voce tem tres tentavias')
    for i in range (1,3+1):
        print('tentativa {}'.format(i))
        chute = int(input('Digite um numero: '))
        
        if chute == numero_secreto:
            print('voce acertou')
            break
        else:
            print('voce errou')

    print('Fim do jogo')
if(__name__ == '__main__'):
    numero = 2508
