import pytest
from baralho import Baralho, Carta
from mao import Mao
from jogador import Jogador

@pytest.fixture
def baralho():
    baralho = Baralho()
    baralho.novo_deque_nao_embaralhado()
    return baralho

@pytest.fixture
def jogador():
    jogador = Jogador()
    jogador.set_nome('Rodrigo')
    return jogador

@pytest.fixture
def crupier():
    crupier = Jogador()
    crupier.set_nome('Crupier')
    return crupier



def teste_criar_baralho_e_distribuir_primeiras_cartas(baralho, jogador, crupier):
       
        carta1 = baralho.virar()
        carta2 = baralho.virar()

        jogador.insert_card(carta1)
        jogador.insert_card(carta2)

        carta3 = baralho.virar()
        carta4 = baralho.virar()

        crupier.insert_card(carta3)
        crupier.insert_card(carta4)

        cartas_jogador = jogador.get_mao()
        cartas_Crupier = crupier.get_mao()

        assert str(cartas_jogador[0]) == 'K♣' 
        assert str(cartas_jogador[1]) == 'K♥'

        assert str(cartas_Crupier[0]) == 'K♠'
        assert str(cartas_Crupier[1]) == 'K♦'