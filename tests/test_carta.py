import pytest
from carta import Carta

def test_carta_eh_uma_instancia_de_Carta():
    """ Testa se a carta é uma instância de Carta. """
    carta = Carta('A', '♥')
    assert isinstance(carta, Carta)

def test_string_de_carta_eh_igual_a_A_de_copas():
    """ Testa se a string da carta é igual a 'A de ♥'. """
    carta = Carta('A', '♥')
    assert str(carta) == 'A♥'