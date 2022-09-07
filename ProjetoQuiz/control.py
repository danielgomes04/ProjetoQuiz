from model import model

class control:
    def __init__(self):
        self.opcao1 = 0
        self.opcao = -1
        self.modelo = model()

    def getOpcao1(self):
        return self.opcao1

    def setOpcao1(self, opcao1):
        self.opcao1 = opcao1

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("\nEscolha uma das alternativas abaixo: "
              "\n0. Sair"  +
              "\n1. Jogar" +
              "\n2. Consultar")
        self.setOpcao(int(input()))

    def menu2(self):
        print("Escolha um dos temas abaixo: \n"
              "\n0. Sair" +
              "\n1. O quanto voce sabe sobre o Luffy" +
              "\n2. Conhecimentos Gerais")
        self.setOpcao1(int(input()))

    def operacoes(self):
        while self.getOpcao != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado")
                break
            elif self.getOpcao == 1:
                self.menu2()
                if self.getOpcao1() == 1:
                    self.luffy()
                else:
                    self.conhecimentos()
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
        else:
            print("Opção escolhida inválida digite novamente.")




    def luffy(self):
        pontuacao = 0
        print("Informe seu nome para iniciar o jogo: ")
        nome = input()
        print("\n1. Qual foi a quantidade da primeira recompensa de Luffy?"
              "\n\n1. 100 beries" +
              "\n2. 66 milhões de beries" +
              "\n3. 30 milhões de beries" +
              "\n4. 1 bilhão de beries")
        resposta = int(input())

        while resposta > 4 or resposta < 1:
            print("Resposta inválida, digite um número válido: ")
            print("\n\n1. Qual foi a quantidade da primeira recompensa de Luffy?"
                  "\n1. 100 beries" +
                  "\n2. 66 milhões de beries" +
                  "\n3. 30 milhões de beries" +
                  "4. 1 bilhão de beries")
            resposta = int(input())

        if resposta == 1:
            print("Respota errada.")
        elif resposta == 2:
            print("Resposta errada.")
        elif resposta == 3:
            print("Resposta correta.")
            pontuacao = pontuacao + 1
        elif resposta == 4:
            print("Resposta errada.")

        print("\n\n2. Qual o primeiro tripulante que Luffy encontra depois do Timeskipe?"
              "\n1. Nami" +
              "\n2. Zoro" +
              "\n3. Sanji")
        resposta = int(input())

        while resposta > 3 or resposta < 1:
            print("Resposta inválida, digite um número válido: ")
            print("\n\n2. Qual o primeiro tripulante que Luffy encontra depois do Timeskipe?"
                  "\n1. Nami" +
                  "\n2. Zoro" +
                  "\n3. Sanji")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada.")
        elif resposta == 2:
            print("Resposta correta.")
            pontuacao = pontuacao + 1
        elif resposta == 3:
            print("resposta errada.")

        print("\n\n3. Quem é o pai biológico de Luffy?"
              "\n1. Monkey D.Dragon" +
              "\n2. Teach" +
              "\n3. Gol D.Roger" +
              "\n4. Monkey D.Garp")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("\n\n3. Quem é o pai biológico de Luffy?"
                  "\n1. Monkey D.Dragon" +
                  "\n2. Teach" +
                  "\n3. Gol D.Roger" +
                  "\n4. Monkey D.Garp")
            resposta = int(input())

        if resposta == 1:
            print("Resposta correta")
            pontuacao = pontuacao + 1
        elif resposta == 2:
            print("Resposta errada")
        elif resposta == 3:
            print("Resposta errada")
        elif resposta == 4:
            print("Resposta errada")

        print("\n\n4. MOnkey D.Dragon é o que?"
              "\n1. Almirante e um grande defesor da justica" +
              "\n2. O yonkou mias forte" +
              "\n3. Revolucionario e o homem mais procurado pelo governo mundial" +
              "\n4. Um shishibukai leal a marinha")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("\n\n4. MOnkey D.Dragon é o que?"
                  "\n1. Almirante e um grande defesor da justica" +
                  "\n2. O yonkou mias forte" +
                  "\n3. Revolucionario e o homem mais procurado pelo governo mundial" +
                  "\n4. Um shishibukai leal a marinha")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada")
        elif resposta == 2:
            print("Resposta errada")
        elif resposta == 3:
            print("Resposta correta")
            pontuacao = pontuacao + 1
        elif resposta == 4:
            print("Resposta errada")

        print("\n\n5. Quem é o avô do Luffy?"
              "\n1. Rayleigh" +
              "\n2. Kaido" +
              "\n3. Garp" +
              "\n4. Barba Branca")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("\n\n5. Quem é o avô do Luffy?"
                  "\n1. Rayleigh" +
                  "\n2. Kaido" +
                  "\n3. Garp" +
                  "\n4. Barba Branca")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada")
        elif resposta == 2:
            print("Resposta errada")
        elif resposta == 3:
            print("Resposta correta")
            pontuacao = pontuacao + 1
        elif resposta == 4:
            print("Resposta errada")

        print("\n\n6. Quem são os dois irmãos de Luffy?"
              "\n1. Ace e Sabo"
              "\n2. Sanji e Zoro"
              "\n3. Crocodile e Doflamingue"
              "\n4. Shanks e Mihawk")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("\n\n6. Quem são os dois irmãos de Luffy?"
                  "\n1. Ace e Sabo"
                  "\n2. Sanji e Zoro"
                  "\n3. Crocodile e Doflamingue"
                  "\n4. Shanks e Mihawk")
            resposta = int(input())

        if resposta == 1:
            print("Resposta correta")
            pontuacao = pontuacao + 1
        elif resposta == 2:
            print("Resposta errada")
        elif resposta == 3:
            print("Resposta errada")
        elif resposta == 4:
            print("Resposta errada")

        print("\n\n7. Quem foi o primerio shishibukai que Luffy derrotou?"
              "\n1. Doflanmingo" +
              "\n2. Mihawk" +
              "\n3. Hanckok" +
              "\n4. Crocodile")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("\n\n7. Quem foi o primerio shishibukai que Luffy derrotou?"
                  "\n1. Doflanmingo" +
                  "\n2. Mihawk" +
                  "\n3. Hanckok" +
                  "\n4. Crocodile")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada")
        elif resposta == 2:
            print("Resposta errada")
        elif resposta == 3:
            print("Resposta errada")
        elif resposta == 4:
            print("Resposta correta")
            pontuacao = pontuacao + 1

        print("\n\n8. Quem são da tripulação de Luffy?"
              "\n1. Shanks, Buggy e Mihawk"
              "\n2. Zoro, Sanji e Nami"
              "\n3. Barba Negra, Kaido e Big Mom"
              "\n4. Crocodile, Donflamingo e Hanckok")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("\n\n8. Quem são da tripulação de Luffy?"
                  "\n1. Shanks, Buggy e Mihawk"
                  "\n2. Zoro, Sanji e Nami"
                  "\n3. Barba Negra, Kaido e Big Mom"
                  "\n4. Crocodile, Donflamingo e Hanckok")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada")
        elif resposta == 2:
            print("Resposta correta")
            pontuacao = pontuacao + 1
        elif resposta == 3:
            print("Resposta errada")
        elif resposta == 4:
            print("Resposta errada")

        print("\n\n9. Quem entregou o chapéu pro Luffy?"
              "\n1. Kaino" +
              "\n2. Dragon" +
              "\n3. Shanks" +
              "\n4. Roger")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("\n\n9. Quem entregou o chapéu pro Luffy?"
                  "\n1. Kaino" +
                  "\n2. Dragon" +
                  "\n3. Shanks" +
                  "\n4. Roger")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada")
        elif resposta == 2:
            print("Resposta errada")
        elif resposta == 3:
            print("Resposta correta")
            pontuacao = pontuacao + 1
        elif resposta == 4:
            print("Resposta errada")

        print("\n\n10. Qual é o sonho do Luffy?"
              "\n1. Ter a maior recompensa e ser famoso"
              "\n2. Ser o rei dos piratas e poder ser livre"
              "\n3. Destruir o mundo e trazer o caos"
              "\n4. Se tornar marinheiro e trazer orgulho para o seu avo")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("\n\n10. Qual é o sonho do Luffy?"
                  "\n1. Ter a maior recompensa e ser famoso"
                  "\n2. Ser o rei dos piratas e poder ser livre"
                  "\n3. Destruir o mundo e trazer o caos"
                  "\n4. Se tornar marinheiro e trazer orgulho para o seu avo")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada")
        elif resposta == 2:
            print("Resposta correta")
            pontuacao = pontuacao + 1
        elif resposta == 3:
            print("Resposta errada")
        elif resposta == 4:
            print("Resposta errada")
        print("Sua pontuação foi de: {} ".format(pontuacao))
        self.modelo.inserir(nome, pontuacao)

    def conhecimentos(self):
        pontuacao = 0
        print("Informe seu nome para iniciar o jogo.")
        nome = input()
        print("\n\n1. O que a palavra legend significa em português?"
                "\n1. Legenda" +
                "\n2. Conto" +
                "\n3. História" +
                "\n4. Lenda")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("\n\n1. O que a palavra legend significa em português?"
                  "\n1. Legenda" +
                  "\n2. Conto" +
                  "\n3. História" +
                  "\n4. Lenda")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada")
        elif resposta == 2:
            print("Resposta errada.")
        elif resposta == 3:
            print("Resposta errada")
        elif resposta == 4:
            print("Resposta correta")
            pontuacao = pontuacao + 1

        print("\n\n2. Qual o número mínimo de jogadores numa partida de futebol?"
                "\n1. 8" +
                "\n2. 10" +
                "\n3. 9" +
                "\n4. 7")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("\n\n2. Qual o número mínimo de jogadores numa partida de futebol?"
                  "\n1. 8" +
                  "\n2. 10" +
                  "\n3. 9" +
                  "\n4. 7")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada")
        elif resposta == 2:
            print("Resposta errada.")
        elif resposta == 3:
            print("Resposta errada")
        elif resposta == 4:
            print("Resposta correta")
            pontuacao = pontuacao + 1

        print("3. Quais os principais autores do Barroco no Brasil?"
                "1. Gregório de Matos, Bento Teixeira e Manuel Botelho de Oliveira" +
                "2. Miguel de Cervantes, Gregório de Matos e Danthe Alighieri" +
                "3. Padre Antônio Vieira, Padre Manuel de Melo e Gregório de Matos" +
                "4. Castro Alves, Bento Teixeira e Manuel Botelho de Oliveira")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("3. Quais os principais autores do Barroco no Brasil?"
                  "1. Gregório de Matos, Bento Teixeira e Manuel Botelho de Oliveira" +
                  "2. Miguel de Cervantes, Gregório de Matos e Danthe Alighieri" +
                  "3. Padre Antônio Vieira, Padre Manuel de Melo e Gregório de Matos" +
                  "4. Castro Alves, Bento Teixeira e Manuel Botelho de Oliveira")
            resposta = int(input())

        if resposta == 1:
            print("Resposta correta")
            pontuacao = pontuacao + 1
        elif resposta == 2:
            print("Resposta errada.")
        elif resposta == 3:
            print("Resposta errada")
        elif resposta == 4:
            print("Resposta errada")

        print("4. Quais as duas datas que são comemoradas em novembro?"
                "1. Independência do Brasil e Dia da Bandeira" +
                "2. Proclamação da República e Dia Nacional da Consciência Negra" +
                "3. Dia do Médico e Dia de São Lucas" +
                "4. Dia de Finados e Dia Nacional do Livro")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("4. Quais as duas datas que são comemoradas em novembro?"
                  "1. Independência do Brasil e Dia da Bandeira" +
                  "2. Proclamação da República e Dia Nacional da Consciência Negra" +
                  "3. Dia do Médico e Dia de São Lucas" +
                  "4. Dia de Finados e Dia Nacional do Livro")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada")
        elif resposta == 2:
            print("Resposta correta.")
            pontuacao = pontuacao + 1
        elif resposta == 3:
            print("Resposta errada")
        elif resposta == 4:
            print("Resposta errada")

        print("5. Quem pintou Guernica ?"
                "1. Paul Cézanne" +
                "2. Pablo Picasso" +
                "3. Diego Rivera" +
                "4. Tarsila do Amaral")
        resposta = int(input())

        while resposta < 1 or resposta > 4:
            print("Resposta inválida, digite um número válido.")
            print("5. Quem pintou Guernica ?"
                  "1. Paul Cézanne" +
                  "2. Pablo Picasso" +
                  "3. Diego Rivera" +
                  "4. Tarsila do Amaral")
            resposta = int(input())

        if resposta == 1:
            print("Resposta errada")
        elif resposta == 2:
            print("Resposta correta.")
            pontuacao = pontuacao + 1
        elif resposta == 3:
            print("Resposta errada")
        elif resposta == 4:
            print("Resposta errada")

        print("Sua pontuação foi de: {} ".format(pontuacao))
        self.modelo.inserir(nome, pontuacao)