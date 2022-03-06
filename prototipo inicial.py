'''
Bruno Vinícius da Silva
Tecnologia em Análise e Desenvolvimento de Sistemas

Checkpoint 1:
- Interação com o jogador, entradas e saídas de dados utilizando as estruturas de repetição.
- Criação de uma opção para lançar os três dados aleatoriamente, verificar qual foi o resultado de cada um dos dados.
- Criação das variáveis para contabilizar os tiros, cérebros e passos.
'''

#importar bibliotecas
import time #inserir pausas entre ações
import random #gerar números ou dados aleatórios

#definir variáveis iniciais
qtd_jogadores = 1
players = []
dados = 13
copo = ['CPCTPC', 'CPCTPC', 'CPCTPC', 'CPCTPC', 'CPCTPC', 'CPCTPC', 'TPCTPC', 'TPCTPC', 'TPCTPC', 'TPCTPC', 'TPTCPT', 'TPTCPT', 'TPTCPT']
pontuação = []

'''
DadoVerde = "CPCTPC"
DadoAmarelo = "TPCTPC"
DadoVermelho = "TPTCPT"
'''

#Mensagem de saudação aos jogadores
print (100*'-')
print("Olá, ZUMBIIIIIS! Sejam bem-vindos ao Zombie Dices, um jogo onde o melhor comedor de cérebros VENCE!")
time.sleep(1) #Pausa de 1 segundo até o próximo comando
print (100*'-')

print ()

#Informar a quantidade de jogadores e analisar se tem a quantidade mínima necessária
print("Para tudo funcionar, precisamos de pelo menos dois zumbis famintos por cérebros...")
print("Escreva o nome dos jogadores em cada linha, e quando não tiver mais, basta apertar ENTER para enviar a resposta em branco")

print ()

print (100*'-')
nome = str(input("Digite o nome do jogador 1: ")) #armazena o nome dos jogadores

#Estrutura para armazenar o nome dos jogadores em uma lista assim como atualizar a quantidade de jogadores
while nome !=  '':
    players.append(nome) #armazena o nome dos jogadores na lista PLAYERS
    qtd_jogadores += 1 #armazena a quantidade de jogadores
    nome = str(input("Digite o nome do jogador {}: ".format((qtd_jogadores)))) #gera input para a inserção de outro jogador
    if nome == '':
        qtd_jogadores -= 1 #se o output for vazio, não irá contabilizar no número total de jogadores

print ()

#identifica se há jogadores em quantidade suficiente
if qtd_jogadores <2:
    print("É necessário 2 ou mais zumbis para o jogo começar! Reinicie o Jogo!") #fecha se tiver menos que 2 jogadores
else:
    print("Vamos começar a caça aos cérebros?") #continua para a rodada se tiver 2 ou mais jogadores

    print (100*'-')

    time.sleep(1)

    for i in players:
        start = str(input(f"{i}, digite 'S' para iniciar a rodada ou 'N' para passar a vez: \n"))
        start_lower = start.lower()
        if start_lower == "s" or start_lower == "n":
            if start_lower == "n":
                input(f"{i}, você passou a sua vez! Pressione ENTER!")
            else:
                contagem_passos = 0  # quantidade de passos na rodada
                contagem_tiros = 0  # quantidade de tiros na rodada
                contagem_cerebros = 0  # quantidade de cerebros na rodada
                dados_atual = dados - contagem_passos

                while contagem_cerebros < 13 or contagem_tiros < 3:
                    try:
                        for i in range(dados_atual):
                            dado = random.choice(copo)
                            face_dado = random.choice(dado)
                            copo.remove(dado)

                            if face_dado == "T":
                                face_dado = "TIRO"
                                contagem_tiros = contagem_tiros + 1
                            elif face_dado == "P":
                                face_dado = "PASSO"
                                contagem_passos = contagem_passos + 1
                            else:
                                face_dado == "C"
                                face_dado = "CÉREBRO"
                                contagem_cerebros = contagem_cerebros + 1

                            print(face_dado)

                            print(f"Você tem {contagem_tiros} tiros, {contagem_passos} passos e {contagem_cerebros} cérebros.\n")

                    except IndexError:
                        print("Sem dados suficientes no copo!")
                        break

                pontuação.append(i)
                pontuação.append(contagem_tiros)
                pontuação.append(contagem_cerebros)
                pontuação.append(contagem_passos)

                print(pontuação)

                if contagem_cerebros < 13 and contagem_tiros < 3:
                    start = str(input(f"{i}, digite 'S' para iniciar a rodada ou 'N' para passar a vez: \n"))





















        elif start_lower != "s" or start_lower != "n":
            print("Digite 'S' ou 'N' apenas!")

