import pytest
from carta import Carta


def test_carta_eh_uma_instancia_de_Carta():
    """ Testa se a carta é uma instância de Carta. """
    carta = Carta('2', '♥')
    assert isinstance(carta, Carta)

def test_representacao_em_str_da_carta():
    """ Testa se a string da carta é igual a 'A de ♥'. """
    carta = Carta('A', '♥')
    assert str(carta) == 'A♥'