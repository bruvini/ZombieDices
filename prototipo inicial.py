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

print ()

time.sleep(1)

print (100*'-')
#executa as ações de cada rodada para cada jogador na lista PLAYERS
for i in players:
    play = str(input("{} é sua vez de jogar. Digite S para continuar e N para finalizar: ".format(i)))
    play_min = play.lower()
    if 's' or 'n' in play_min:
        if play_min == "n":
           print("Ok! Vai perder de comer alguns cérebros, {}...".format(i))
        else:
            print ("ok")







