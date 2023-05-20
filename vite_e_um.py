from baralho import Baralho, Carta
from mao import Mao
from jogador import Jogador
import constantes as const

class Vinte_e_um():
    def __init__(self):
        self.baralho = Baralho()
        self.jogador = Jogador()
        self.croupier = Jogador()
        self.jogador.mao = Mao()
        self.croupier.mao = Mao()
        self._cumprimento = self._print_inicial()
    
    def _print_inicial(self):
        print()
        print('|', 28*'=' , '|')
        print('| BEM-VINDO AO JOGO VINTE E UM |')
        print('|', 28*'=' , '|')
        print()


    def registrar_jogador(self):
        self.jogador.set_nome(input('Digite o nome do jogador: ').capitalize())
    
    def nome_croupier(self):
        self.croupier.set_nome('Croupier')

    def registrar_saldo(self):
        self.jogador.set_saldo(int(input('Digite o saldo do jogador: ')))
    
    def verifica_saldo(self):
        return self.jogador.saldo >= self.aposta

    def registrar_aposta(self):
        self.aposta = int(input('Digite o valor da aposta: '))
        if self.verifica_saldo():
            self.jogador.set_saldo(self.jogador.saldo - self.aposta)
        else:
            print('Saldo insuficiente')
            self.registrar_aposta()