import pytest
from mao import Mao
from carta import Carta
from baralho import Baralho

@pytest.fixture
def mao():
    mao = Mao()
    return mao

def carta_as_de_ouros():
    carta = Carta('A', '♦')
    return carta
def carta_valete_de_espadas():
    carta = Carta('J', '♠')
    return carta
def carta_dois_de_copas():
    carta = Carta('2', '♥')
    return carta
def carta_nove_paus():
    carta = Carta('9', '♣')
    return carta

def test_mao(mao):
    assert mao.get_cartas() == []
    assert mao.get_score() == 0

def test_insert_card(mao):
    mao.insert_card(carta_as_de_ouros())
    mao.insert_card(carta_valete_de_espadas())
    mao.insert_card(carta_dois_de_copas())
    assert mao.get_cartas() == [carta_as_de_ouros(), carta_valete_de_espadas(), carta_dois_de_copas()]

def test_blackjack(mao):
    mao.insert_card(carta_as_de_ouros())
    mao.insert_card(carta_valete_de_espadas())
    assert mao.get_score() == 21

def test_calcula_score_se_as_vale_um(mao):
    mao.insert_card(carta_valete_de_espadas())
    mao.insert_card(carta_valete_de_espadas())
    mao.insert_card(carta_as_de_ouros())
    assert mao.get_score() == 21

def test_calcula_score_se_as_vale_um_mao(mao):
    mao.insert_card(carta_nove_paus())
    mao.insert_card(carta_dois_de_copas())
    mao.insert_card(carta_as_de_ouros())
    assert mao.get_score() == 12

def test_verifica_se_perdeu(mao):
    mao.insert_card(carta_nove_paus())
    mao.insert_card(carta_dois_de_copas())
    mao.insert_card(carta_valete_de_espadas())
    assert mao.verifica_se_perdeu() == False
    mao.insert_card(carta_valete_de_espadas())
    assert mao.verifica_se_perdeu() == True

