from random import shuffle
from time import sleep


# criar jogador
class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def rodada(self):
        sleep(0.5)
        print("\n" f'Vez do jogador {self.name}:')
        self.temp_score = {'cerebros': 0, 'tiros': 0}
        self.dados_na_mao = []
        self.dados = criar_dados()

        while True:

            # verificação de dados na mão
            while len(self.dados_na_mao) < 3:
                self.dados_na_mao.append(self.dados.pop())

            # embaralha as faces dos dados, mostra ao usuário e verifica as faces
            for i in range(2, -1, -1):
                shuffle(self.dados_na_mao[i].sides)
                self.face_para_cima = self.dados_na_mao[i].sides[-1]
                print(f'Dado {self.dados_na_mao[i].color}, face: {self.face_para_cima}')

                if self.face_para_cima == 'tiro':
                    self.temp_score['tiros'] += 1
                    self.dados.append(self.dados_na_mao.pop(i))
                elif self.face_para_cima == "cerebro":
                    self.temp_score['cerebros'] += 1
                    self.dados.append(self.dados_na_mao.pop(i))

            print(self.temp_score)

            # verificação de tiros e se o jogador pretende continuar a rodada
            if self.temp_score['tiros'] < 3:
                print("\n")
                continuar = input('Quer continuar jogando (s/n): ')
                sleep(0.5)

                if continuar != 's':
                    self.score += self.temp_score['cerebros']
                    sleep(0.5)
                    print(f'Fim da rodada do jogador {self.name}. Cérebros: {self.score}' "\n")
                    break

            else:
                sleep(0.5)
                print(f"Perdeu a rodada, tomou três tiros e jogou fora {self.temp_score['cerebros']} cérebros." "\n")
                break


# criar dados
class Dado(object):
    def __init__(self, color, sides):
        self.color = color
        self.sides = sides


def criar_dados():
    red = Dado('Vermelho', ['tiro', 'tiro', 'tiro', 'cerebro', 'passo', 'passo'])
    yellow = Dado('Amarelo', ['tiro', 'tiro', 'cerebro', 'cerebro', 'passo', 'passo'])
    green = Dado('Verde', ['tiro', 'cerebro', 'cerebro', 'cerebro', 'passo', 'passo'])
    dados = [red, red, red, yellow, yellow, yellow, yellow, green, green, green, green, green, green]
    shuffle(dados)
    return dados


# cria jogadores usando a classe definida
def criar_jogadores():
    players = []

    while True:
        try:
            total_players = int(input('Informe o número de jogadores: '))
            if total_players > 1:
                break
            else:
                print('quantidade insuficiente de jogadores')
        except ValueError:
            print('Informar um número inteiro')

    for i in range(0, total_players):
        name = input(f'nome do jogador {i + 1}: ')
        this_player = Player(name, 0)
        players.append(this_player)

    shuffle(players)

    print('Ordem aleatória para jogar:')
    for each_player in players:
        print(f'Jogador:  {each_player.name};')

    print("\n")

    return players


if __name__ == '__main__':
    # cria jogadores usando a função e armazena a vvariavel players
    players = criar_jogadores()
    game_over = False

    # verifica se alguem fez 13 pontos, caso contrario, continua o jogo
    while game_over == False:
        for each_player in players:
            Player.rodada(each_player)
            if each_player.score >= 13:
                vencedor = each_player.name
                game_over = True

        sleep(0.5)
        print(f"Fim da rodada. Pontuação: ")

        for each_player in players:
            print(f"Jogador {each_player.name}: {each_player.score} pontos.")

# mostra o resultado final do jogo
sleep(0.5)
print("\n" "Fim de jogo. Pontuação final: ")
for each_player in players:
    print(f"Jogador {each_player.name}: {each_player.score} pontos.")

sleep(0.5)
print("\n" f"O vencedor foi {vencedor}")