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
rounds = 0 #número de rodadas jogadas
vencedor = [] #nome do vencedor da ultima rodada
dados = 3 #quantidade de dados para a rodada atual sem contar com o número de PASSOS
qtd_jogadores = 1
players = []
contagem_passos = 0 #quantidade de passos na rodada
contagem_tiros = 0 #quantidade de tiros na rodada
contagem_cerebros = 0 #quantidade de cerebros na rodada

#Mensagem de saudação aos jogadores
print("Olá, ZUMBIIIIIS! Sejam bem-vindos ao Zombie Dices, um jogo onde o melhor comedor de cérebros VENCE!")
time.sleep(1) #Pausa de 1 segundo até o próximo comando

#Informar a quantidade de jogadores e analisar se tem a quantidade mínima necessária
print("Para tudo funcionar, precisamos de pelo menos dois zumbis famintos por cérebros...")
print("Para finalizar o registro de jogadores, basta apertar ENTER para enviar a resposta em branco")
nome = str(input("Digite o nome do jogador {}: ".format((qtd_jogadores))))

while nome !=  '':
    player = [qtd_jogadores, nome]
    players.append(player)
    qtd_jogadores += 1
    nome = str(input("Digite o nome do jogador {}: ".format((qtd_jogadores))))

if qtd_jogadores <2:
    print("É necessário 2 ou mais zumbis para o jogo começar! Reinicie o Jogo!")
else:
    print("Vamos começar a caça aos cérebros?")

for i, nome in enumerate(players[nome]):
    play = str(input("{} é sua vez de jogar. Aperte enter para iniciar: ".format(player[i])))








