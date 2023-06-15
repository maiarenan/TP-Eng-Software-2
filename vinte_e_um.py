from baralho import Baralho, Carta
from mao import Mao
from jogador import Jogador

class Vinte_e_um():
    def __init__(self):
        self.baralho = Baralho()
        self.jogador = Jogador()
        self.croupier = Jogador()
        self._cumprimento = self._print_inicial()
        self._registrar_jogador()
    
    def _print_inicial(self):
        print()
        print('|', 28*'=' , '|')
        print('| BEM-VINDO AO JOGO VINTE E UM |')
        print('|', 28*'=' , '|')
        print()


    def _registrar_jogador(self):
        self.jogador.set_nome(input('Digite o nome do jogador: ').capitalize())
        self.jogador.cumprimentar_jogador()
        self._nome_croupier()
    
    def _nome_croupier(self):
        self.croupier.set_nome('Croupier')


    def _verifica_estado_pos_1_rodada(self):
        
        if self.jogador.mao.verifica_se_vitoria_blackjack():
            print(f'Jogador {self.jogador.name} já foi declarado vitorioso! Sua mão:')
            print(f'{self.jogador.mao.get_cartas()}')
            print('Que sorte em!!!')
            return True
       
        else:
            print(f'Primeira rodada de cartas distribuida:')
            print(f'Cartas e score de {self.jogador.name}:')
            self.mostrar_score_jogador()
            print()
            print(f'Primeira carta de Crupier:')
            cartas = self.croupier.mao.get_cartas()
            print(cartas[0])
            return False
        
    def distribui_primeira_rodada(self):
        carta1 = self.baralho.virar()
        carta2 = self.baralho.virar()

        self.jogador.mao.insert_card(carta1)
        self.jogador.mao.insert_card(carta2)

        carta3 = self.baralho.virar()
        carta4 = self.baralho.virar()

        self.croupier.mao.insert_card(carta3)
        self.croupier.mao.insert_card(carta4)
        
        return self._verifica_estado_pos_1_rodada()

    def perguntar_jogador_proxima_jogada(self):
        while True:
            resposta = input('Digite S para comprar mais cartas, ou N para parar: ').upper()

            if resposta == 'S':
                return True
            elif resposta == 'N':
                return False

            print('Entrada inválida. Digite S para comprar mais cartas, ou N para parar.')

    def mostrar_score_jogador(self):
        print(f'Score do jogador: {self.jogador.get_score()}')
        print(f'Suas cartas atuais são: {self.jogador.mao.get_cartas()}')
    
    def mostrar_score_croupier(self):
        print(f'Score do Croupier: {self.croupier.get_score()}')

    def inserir_carta_jogador(self):
        card = self.baralho.virar()
        self.jogador.mao.insert_card(card)
        perdeu = self.jogador.mao.verifica_se_perdeu()
        return perdeu
    
    def _inserir_carta_croupier(self):
        card = self.baralho.virar()
        self.croupier.mao.insert_card(card)

    def croupier_comprar_cartas_ate_passar_jogador(self):
        score_croupier = self.croupier.get_score()
        score_jogador = self.jogador.get_score()
        
        while score_croupier < score_jogador:
            self._inserir_carta_croupier()
            score_croupier = self.croupier.get_score()

    def exibir_resultado(self, vencedor_nome, score_vencedor, score_perdedor):
        print(f'O {vencedor_nome} venceu!! Com {score_vencedor} pontos, contra {score_perdedor} pontos do oponente.')
            
    def definir_vencedor(self):
        score_croupier = self.croupier.get_score()
        score_jogador = self.jogador.get_score()

        if score_croupier > 21 or score_jogador > score_croupier:
            self.exibir_resultado(self.jogador.name, score_jogador, score_croupier)
        else:
            self.exibir_resultado('Crupier', score_croupier, score_jogador)
