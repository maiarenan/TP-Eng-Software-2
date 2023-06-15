import pytest
from mao import Mao
from carta import Carta
from baralho import Baralho
import constantes as const

@pytest.fixture
def mao():
    mao = Mao()
    return mao  

@pytest.fixture
def carta_as_de_ouros():
    carta = Carta('A', '♦')
    return carta

@pytest.fixture
def carta_valete_de_espadas():
    carta = Carta('J', '♠')
    return carta

@pytest.fixture
def carta_dois_de_copas():
    carta = Carta('2', '♥')
    return carta

@pytest.fixture
def carta_nove_paus():
    carta = Carta('9', '♣')
    return carta

@pytest.fixture
def cartas_valem_10():
    cartas = [Carta('J', '♠'), Carta('Q', '♠'), Carta('K', '♠'), Carta('10', '♠')]
    return cartas

def test_mao(mao):
    assert mao.get_cartas() == []
    assert mao.get_score() == 0

def test_insert_card(mao, carta_as_de_ouros, carta_valete_de_espadas, carta_dois_de_copas):
    mao.insert_card(carta_as_de_ouros)
    mao.insert_card(carta_valete_de_espadas)
    mao.insert_card(carta_dois_de_copas)
    assert mao.get_cartas() == [carta_as_de_ouros, carta_valete_de_espadas, carta_dois_de_copas]

def test_blackjack(mao, carta_as_de_ouros, carta_valete_de_espadas):
    mao.insert_card(carta_as_de_ouros)
    mao.insert_card(carta_valete_de_espadas)
    assert mao.get_score() == 21

def test_calcula_score_se_as_vale_um(mao, carta_valete_de_espadas, carta_as_de_ouros):
    mao.insert_card(carta_valete_de_espadas)
    mao.insert_card(carta_valete_de_espadas)
    mao.insert_card(carta_as_de_ouros)
    assert mao.get_score() == 21

def test_calcula_score_se_as_vale_um_mao_maior_que_dez(mao, carta_dois_de_copas, carta_as_de_ouros, carta_nove_paus):
    mao.insert_card(carta_nove_paus)
    mao.insert_card(carta_dois_de_copas)
    mao.insert_card(carta_as_de_ouros)
    assert mao.get_score() == 12

def test_verifica_se_perdeu(mao, carta_nove_paus, carta_dois_de_copas, carta_valete_de_espadas):
    mao.insert_card(carta_nove_paus)
    mao.insert_card(carta_dois_de_copas)
    mao.insert_card(carta_valete_de_espadas)
    assert mao.verifica_se_perdeu() == False
    mao.insert_card(carta_valete_de_espadas)
    assert mao.verifica_se_perdeu() == True

def test_cartas_valem_10(cartas_valem_10):
    '''Testa se todas as cartas que valem 10 valem 10 pontos'''
    assert all (const.cartas_valor_no_21.get(carta.valor) == 10 for carta in cartas_valem_10)