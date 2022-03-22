import Forca
import Adivinhacao

def escolhe_jogo():
    print("****************************")
    print ("*****SELECIONE SEU JOGO****")
    print("****************************")

    print("(1) FORCA | (2) ACHE O NÚMERO")

    jogo = int (input("Digite o número correspondente ao jogo que você quer jogar: "))

    if (jogo == 1):
        print("Jogando Forca...")
        Forca.jogar()
    elif (jogo == 2):
        print("Jogando Ache o número...")
        Adivinhacao.jogar()

    else:
        print ("INVÁLIDO!")
        print ("Reinicie o jogo e selecione uma das opções válidas.")

if (__name__ == "__main__"):
    escolhe_jogo()

