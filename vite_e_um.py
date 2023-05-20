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
        resposta = input('Digite S para comprar mais cartas, ou N para parar').upper()
        
        if resposta != 'S' and resposta != 'N':
            print('Digita a letra certa o miseravi!')
            return self.perguntar_jogador_proxima_jogada()
        
        else:
            if resposta == 'S':
                return self._inserir_carta_jogador()
            else:
                return self.mostrar_score_jogador()

    def mostrar_score_jogador(self):
        print(f'Score do jogador: {self.jogador.get_score()}')
        print(f'Suas cartas atuais são: {self.jogador.mao.get_cartas()}')
    
    def mostrar_score_croupier(self):
        print(f'Score do Croupier: {self.croupier.get_score()}')

    def _inserir_carta_jogador(self):
        card = self.baralho.virar()
        self.jogador.mao.insert_card(card)
        perdeu = self.jogador.mao.verifica_se_perdeu()
        return self.mostrar_score_jogador()
    
    def _inserir_carta_croupier(self):
        card = self.baralho.virar()
        self.jogador.mao.insert_card(card)
        return self.mostrar_score_jogador()



    # def registrar_saldo(self):
    #     self.jogador.set_saldo(int(input('Digite o saldo do jogador: ')))
    
    # def verifica_saldo(self):
    #     return self.jogador.saldo >= self.aposta

    # def registrar_aposta(self):
    #     self.aposta = int(input('Digite o valor da aposta: '))
    #     if self.verifica_saldo():
    #         self.jogador.set_saldo(self.jogador.saldo - self.aposta)
    #     else:
    #         print('Saldo insuficiente')
    #         self.registrar_aposta()
