import random
print("\nBem-vindo(a) ao JOGO DA SENHA\n\nObjetivo do jogo: descobrir a senha (4 números de 1-6 gerados aleatóriamente)\n*Você deve também acertar a posição correta de cada número*\n___Regras do jogo___\n1:Use 's' ou 'n' para responder as perguntas.\n2:Caso não consiga achar a reposta digite o número 0 para reiniciar.\n3:Você terá 10 tentativas para acertar a senha.\n4:Divirta-se\n")

def Ranck(listaR):
    listaR.sort()
    if len(listaR)==0:
        print("Não há rancking")
    elif len(listaR)==1:
        resultado = listaR.pop(0)
        print('====Rancking do Jogo====\nPrimeiro lugar: ', (resultado))
    elif len(listaR)==2:
        resultado = listaR.pop(0)
        resultado1 = listaR.pop(0)
        print('====Rancking do Jogo====\nPrimeiro lugar: ',(resultado),"\nSegundo lugar: ", (resultado1))
    else:
        for i in listaR:
            resultado = listaR.pop(0)
            resultado2 = listaR.pop(0)
            resultado3 = listaR.pop(0)
            Rancking = resultado + resultado2 + resultado3
            break
        print('====Rancking do Jogo====\nPrimeiro lugar: ', (Rancking[1]), "\nSegundo lugar: ", (Rancking[3]),
              "\nTerceiro lugar: ", (Rancking[-1]))

def colocadas(sorteio, chute):
    contar = []
    if sorteio[0] == chute[0]:
        contar.append(1)
    if sorteio[1] == chute[1]:
        contar.append(1)
    if sorteio[2] == chute[2]:
        contar.append(1)
    if sorteio[3] == chute[3]:
        contar.append(1)
    return contar

def sorteio():
    cont = 0
    lista = []
    while cont < 4:
        escolha = random.randint(1, 6)
        if escolha not in lista:
            lista.append(escolha)
            cont = cont + 1
    #print(lista)
    return lista

def chutes():
    a = input('Digite 4 números entre 1-6:\n->')
    if a == "0":
        saida=0
        return saida
    else:
        while len(a) != 4:
            a = input('Você não digitou a quantidade correta!\nDigite 4 números entre 1-6:\n->')
        alista = list(a)
        listachute = []
        for i in alista:
            item = int(i)
            listachute.append(item)
        return listachute

def jogo(sorteio, chute1):
    if chute1==0:
        return 0
    else:
        parametro = [1, 2, 3, 4, 5, 6]
        lista_dos_iguais = [elemento for elemento in sorteio if elemento in chute1]
        lista_dos_diferentes = [elemento for elemento in sorteio if elemento not in chute1]
        colocada = colocadas(sorteio, chute1)
        nusou = [elemento for elemento in parametro if elemento not in chute1]
        tamanho = len(colocada)
        nalista = len(lista_dos_iguais)
        foradalista = len(lista_dos_diferentes)
        return nalista, foradalista, tamanho, nusou

def pontos():
    listasorteio = sorteio()
    listachute = chutes()
    cont = 1
    if listachute == 0:
        print('você desistiu dessa partida.\nResposta: ',listasorteio)
        cont=0
        return cont
    elif listachute!=0:
        while cont <= 10:
            if listachute == 0:
                print('você desistiu dessa partida.\nResposta: ', listasorteio)
                cont = 0
                return cont
            elif listasorteio == listachute:
                print("Você acertou em", cont, "jogadas")
                return cont
            else:
                nalista, foradalista, tamanho, n_usou = jogo(listasorteio, listachute)
                print("Dentro da lista:", nalista, "\nFora da lista:", foradalista, "\nColocadas corretamente:",
                      tamanho, "\nvocê não usou os números: ", n_usou)
                cont = cont + 1
                listachute = chutes()
        if cont >= 10:
            print('você atingiu o limite de jogadas\nResposta: ', listasorteio)
            return cont

def nome():
    nam=input("Nome jogador:\n-> ")
    if nam != "stop":
        print("olá, ", nam)
        score_jogador = pontos()
        return nam, score_jogador

lista=[]
lista1=[]
jogadornome,score =nome()
while True:
    if score==0:
        novoj = input("desejá jogar novamente?\n->")
        if novoj == "n":
            print("obrigado por jogar!")
            novog = input("há outro jogador?\n->")
            if novog == "s":
                jogadornome, score = nome()
                lista1 = []
            elif novog == "n":
                print("obrigado por jogar!")
                break
        else:
            print("olá, novamente ", jogadornome)
            score = pontos()
            lista1 = []
    else:
        lista1.append(score)
        lista1.append(jogadornome)
        lista.append(lista1)
        novoj = input("desejá jogar novamente?\n->")
        if novoj == "n":
            print("obrigado por jogar!")
            novog = input("há outro jogador?\n->")
            if novog == "s":
                jogadornome, score = nome()
                lista1 = []
            elif novog == "n":
                print("obrigado por jogar!")
                break
        else:
            print("olá, novamente ", jogadornome)
            score = pontos()
            lista1 = []

Ranck(lista)