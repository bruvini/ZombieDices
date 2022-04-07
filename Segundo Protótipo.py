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
from random import shuffle #gerar números ou dados aleatórios

## DEFINIÇÃO DE FUNÇÕES E CLASSES

# Classe que cria os dados como um objeto
class Dado(object):
    def __init__(self, cor, lados):
        self.cor = cor
        self.lados = lados

#Função que define as cores e as faces dos dados
def gerar_dados():
    dado_vermelho = Dado('Vermelho', ['tiro', 'tiro', 'tiro', 'cerebro', 'passo', 'passo'])
    dado_amarelo = Dado('Amarelo', ['tiro', 'tiro', 'cerebro', 'cerebro', 'passo', 'passo'])
    dado_verde = Dado('Verde', ['tiro', 'cerebro', 'cerebro', 'cerebro', 'passo', 'passo'])
    dados = [dado_vermelho, dado_vermelho, dado_vermelho, dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde]
    shuffle(dados)
    return dados

# Função para criar os jogadores
def criar_jogadores():
    jogadores = []
    # Verificar se tem a quantidade mínima de jogadores
    while True:
        try:
            total_de_jogadores = int(input('Informe quantos jogadores irão participar da rodada: '))
            if total_de_jogadores > 1:
                print(f'Agora com {total_de_jogadores}, podemos iniciar a comilança de cérebros no Zombie Dice\n')
                break
            else:
                print('É preciso mais do que 1 jogador para iniciar o Zombie Dice. Tente novamente!')
        except ValueError:
            print('Hey, você precisa informar um número inteiro que seja igual ou maior que 2, são as regras...')

    # Registrar jogadores
    for i in range(0, total_de_jogadores):
        nome = input(f'Digite o nome do jogador {i + 1}: ')
        jogador_atual = Jogador(nome, 0)
        jogadores.append(jogador_atual)

    shuffle(jogadores)

    print('Atenção! Embaralhamos os zumbis, a ordem para jogar é:')
    for i in jogadores:
        time.sleep(0.3)
        print(f'Zumbi >>>  {i.nome};')
    return jogadores

# Classe para definir o jogador como um objeto
class Jogador(object):
    #Função para armazenar nome e pontuação do jogador
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos

    #Função para rotina de jogar dados
    def round(self):
        time.sleep(0.5)
        print("\n" f'Vez do jogador {self.nome}:')
        self.pontuacao_na_rodada = {'Cérebros Devorados': 0, 'Tiros': 0}
        self.mao = []
        self.dados = gerar_dados()

        while True:

            # verificação de dados na mão
            while len(self.mao) < 3:
                self.mao.append(self.dados.pop())

            # embaralha as faces dos dados, mostra ao usuário e verifica as faces
            for i in range(2, -1, -1):
                shuffle(self.mao[i].lados)
                self.lado_cima = self.mao[i].lados[-1]
                print(f'O dado {self.mao[i].cor} caiu com a face "{self.lado_cima}" voltada para cima.')

                if self.lado_cima == 'tiro':
                    self.pontuacao_na_rodada['Tiros'] += 1
                    self.dados.append(self.mao.pop(i))
                elif self.lado_cima == "cerebro":
                    self.pontuacao_na_rodada['Cérebros Devorados'] += 1
                    self.dados.append(self.mao.pop(i))

            print(self.pontuacao_na_rodada)

            # verificação de tiros e se o jogador pretende continuar a rodada
            if self.pontuacao_na_rodada['Tiros'] < 3:
                print("\n")
                continuar = input('E ai? Quer ir mais uma rodada? ("s" para SIM e "n" para NÃO): \n').upper()
                time.sleep(0.5)

                if continuar != 'S':
                    self.pontos += self.pontuacao_na_rodada['Cérebros Devorados']
                    time.sleep(0.5)
                    print(f'Fim da rodada do jogador {self.nome}. Cérebros: {self.pontos}' "\n")
                    break

            else:
                time.sleep(0.5)
                print(f"Perdeu a rodada, tomou três tiros e jogou fora {self.pontuacao_na_rodada['Cérebros Devorados']} cérebros." "\n")
                break


## INÍCIO DO JOGO
if __name__ == '__main__':
    jogadores = criar_jogadores() #Chama a função que cria jogadores para dar início ao jogo
    fim_do_jogo = False

    # Verificação em cada rodada para ver qual jogador completou 13 cérebros
    while fim_do_jogo == False:
        for each_player in jogadores:
            Jogador.round(each_player)
            if each_player.pontos >= 13:
                vencedor = each_player.nome
                fim_do_jogo = True

        #imprime o resultado final da rodada
        time.sleep(0.5)
        print(f"Chegamos ao fim desta rodada. A pontuação atual é de: ")
        for i in jogadores:
            print(f">>> Jogador {i.nome}: {i.pontos} cérebros comidos <<<")

# imprime o resultado final do jogo
time.sleep(0.5)
print("\n" "O jogo acabou por aqui. Veja a pontuação final: ")
for i in jogadores:
    print(f">>> Jogador {i.nome}: {i.pontos} cérebros comidos <<<")

# Imprimir quem foi o campeão
time.sleep(0.5)
print("\n" f"O grande zumbi vencedor de Zombie Dice foi {vencedor}. Parabéns!")