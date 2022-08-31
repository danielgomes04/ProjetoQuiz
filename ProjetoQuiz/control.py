from model import model

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()


    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("\nEscolha uma das alternativas abaixo: "
              "\n0. Sair"  +
              "\n1. Jogar" +
              "\n2. Atualizar")
        self.setOpcao(int(input()))

    def operacao(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado.")
                break
            elif self.getOpcao() == 1:
                self.jogo()
        else:
            print("Opção inválida.")

    def jogo(self):
        contador = 0
        print("Em que ano nasceu o Corinthians?\n"
              "1. 1910\n"
              "2. 1934")
        resposta = int(input())
        if resposta == 1:
            print("Correto")
            contador = contador + 1
        else:
            print("Falso profeta")

        print("Quantos Mundiais o Palmeiras tem?\n" +
              "n\1.Zero" +
              "\n2.Um")
        resposta1 = int(input())

        if resposta1 == 1:
            print("Resposta correta!!!")
            contador = contador + 1

        else:
            print("51 é pinga!!!")

        print("sua pontuação foi:")
        print(contador)





