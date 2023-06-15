import pytest
from jogador import Jogador
from carta import Carta


@pytest.fixture
def jogador():
    jogador = Jogador()
    return jogador
    
@pytest.fixture
def cartas():
    as_ouro = Carta('A' , '♦')
    valete_espada = Carta('J', '♠')
    dois_copas = Carta('2', '♥')
    cartas = [as_ouro, valete_espada, dois_copas]
    return cartas

def test_jogador(jogador):
    assert jogador.get_nome() == ''
    assert jogador.get_score() == 0
    assert jogador.get_mao() == []

def test_set_nome(jogador):
    jogador.set_nome('João')
    assert jogador.get_nome() == 'João'


def test_insert_card(jogador, cartas):
    jogador.insert_card(cartas[0])
    jogador.insert_card(cartas[1])
    jogador.insert_card(cartas[2])
    assert jogador.get_mao() == cartas