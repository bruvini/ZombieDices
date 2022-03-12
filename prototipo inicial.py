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

#Mensagem de saudação aos jogadores
print (100*'-')
print("Olá, ZUMBIIIIIS! Sejam bem-vindos ao Zombie Dices, um jogo onde o melhor comedor de cérebros VENCE!")
print (100*'-', '\n')
time.sleep(1) #Pausa de 1 segundo até o próximo comando

#Contabilizar jogadores
qtd_jogadores = 0

while qtd_jogadores <2:
    qtd_jogadores = int(input('Para iniciar, por favor, insira a quantidade de jogadores: '))
    if qtd_jogadores <2:
        print('É necessário  2 ou mais jogadores para iniciar a partida! Tente novamente...')

print (100*'-', '\n')
time.sleep(1) #Pausa de 1 segundo até o próximo comando

#registrar nomes
print('Tudo certo! Agora precisamos saber seus nomes')
jogadores = []

for i in range(qtd_jogadores):
    jogador = str(input(f'Digite o nome do jogador {i+1}: '))
    jogadores.append(jogador)

print (100*'-', '\n')
time.sleep(1) #Pausa de 1 segundo até o próximo comando

#criação dos dados
DadoVerde = "CPCTPC"
DadoAmarelo = "TPCTPC"
DadoVermelho = "TPTCPT"

copo = [DadoVerde, DadoVerde, DadoVerde, DadoVerde, DadoVerde, DadoVerde, DadoAmarelo, DadoAmarelo, DadoAmarelo,
         DadoAmarelo, DadoVermelho, DadoVermelho, DadoVermelho]

print('Agora sim... PREPAREM-SE PARA A COMILANÇA DE CÉREBROS!!!')

print (100*'-', '\n')
time.sleep(1) #Pausa de 1 segundo até o próximo comando

#variáveis globais para incrementação
dados_sorteio = []
jogador_ativo = 0
cerebros = 0
tiros = 0
passos = 0

#início da rodada
while True:
    print('\n')
    print(f'Rodada do jogador {jogadores[jogador_ativo]}')

    print(100 * '-', '\n')
    time.sleep(1)  # Pausa de 1 segundo até o próximo comando

    #sorteio dos dados
    print('Os dados sorteados foram:')

    for i in range(0, 3, 1):
        num_sorteado = random.randint(0,12)
        dado_sorteado = copo[num_sorteado]

        if dado_sorteado == "CPCTPC":
            cor_dado = 'DADO VERDE'
        elif dado_sorteado == "TPCTPC":
            cor_dado = 'DADO AMARELO'
        else:
            cor_dado = 'DADO VERMELHO'

        print(cor_dado)

        dados_sorteio = dado_sorteado

    print(100 * '-', '\n')
    time.sleep(1)  # Pausa de 1 segundo até o próximo comando

    #sorteio das faces de cada dado sorteado anteriormente
    print('As faces sorteadas foram:')

    for i in range(0, 3, 1):
        face_sorteada = random.choice(dados_sorteio)
        if face_sorteada == "C":
            face_dado = 'cérebro'
            cerebros += 1
        elif face_sorteada == "T":
            face_dado = 'tiro'
            tiros += 1
        else:
            face_dado = 'passo'
            passos += 1

        print(face_dado)

    print(100 * '-', '\n')
    time.sleep(1)  # Pausa de 1 segundo até o próximo comando

    #mostrar placar atual com as incrementações
    print(f'Pontuação de {jogadores[jogador_ativo]}')
    print(f'cérebros: {cerebros}')
    print(f'passos: {passos}')
    print(f'tiros: {tiros}')

    print(100 * '-', '\n')
    time.sleep(1)  # Pausa de 1 segundo até o próximo comando

    #questionar se laço continua para próxima rodada
    continuar = str(input(f'{jogadores[jogador_ativo]},você quer continuar a jogar (s/n): ')).upper()

    #zerar as variaveis zeram e mudar o jogador, voltando pra linha 64, caso o atual passe a vez
    if continuar == "N":
        jogador_ativo += 1
        dados_sorteio = []
        cerebros = 0
        tiros = 0
        passos = 0

        # Encerrar se a quantidade máxima de jogadores for atingida
        if jogador_ativo == len(jogadores):
            print('FIM DO JOGO')
            break
        #caso contrário, ir para o próximo jogador
        else:
            print('próxima rodada')
            dado_sorteado = []