import random

def jogar():
    print("****************************")
    print ("**Bem vindo ao Acha Número**!")
    print("****************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 100



    print("DIFICULDADE")
    print("(1) FÁCIL (2) MÉDIO (3) DIFÍCIL")

    dif = int(input("Digite a difuculdade escolhida: "))
    if (dif==1):
        total_de_tentativas = 10
    elif (dif==2):
        total_de_tentativas = 5
    elif(dif==3):
        total_de_tentativas = 3
    else:
        print("Dificuldade inválida! Reinice o Jogo e selecione uma das opções acima.")


    for rodada in range(1, total_de_tentativas + 1):
        print("Rodada {} de {}" .format(rodada, total_de_tentativas))
        chute_usuario = input("Digite um número entre 1 e 100: ")
        print("Você digitou o número: ", chute_usuario)
        chute = int(chute_usuario)

        if (chute <1 or chute > 100):
            print("O número digitado não está entre 1 e 100, por favor digite um número entre 1 e 100.")
            continue

        acertou        = numero_secreto == chute
        chutou_maior   = chute > numero_secreto
        chutou_menor   = chute < numero_secreto

        if (acertou):
            print ("Você acertou e Fez {} pontos!".format(pontos))
            print ("Parabéns!!!!")
            break
        else:
            if(chutou_maior):
                print("Resposta Errada!")
                print("O Valor digitado está acima do número certo!")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}.".format(numero_secreto))
            elif (chutou_menor):
                print("Resposta Errada!")
                print("O Valor digitado está abaixo do número certo!")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}.".format(numero_secreto))
            pontos_perdidos = abs(numero_secreto-chute)
            pontos = pontos - pontos_perdidos


    print ("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()