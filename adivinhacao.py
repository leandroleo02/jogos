import random

def jogar():

    print('********************************')
    print('Bem vindo ao jogo de Adivinhação')
    print('********************************')

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil)')

    nivel = int(input('Defina um nível: '))

    if(nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range (1, tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute_str = input('Digite o seu número entre 1 e 100: ')

        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('Vodê deve digitar um número entre 1 e 100')
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto

        if(acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if(maior):
                print('Você errou! Seu chute foi maior que o número secreto!')
            else:
                print('Você errou! Seu chute foi menor que o número secreto!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()