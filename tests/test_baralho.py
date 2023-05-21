import pytest
from baralho import Baralho, Carta


def test_possui_52_cartas():
    """ Testa se o baralho possui 52 cartas. """
    baralho = Baralho()
    assert len(baralho.cartas) == 52

def test_naipes_e_numeros():
    """ Testa se o baralho possui 13 cartas de cada naipe. """
    baralho = Baralho()
    copas = [carta for carta in baralho.cartas if carta.naipe == '♥']
    ouros = [carta for carta in baralho.cartas if carta.naipe == '♦']
    espadas = [carta for carta in baralho.cartas if carta.naipe == '♠']
    paus = [carta for carta in baralho.cartas if carta.naipe == '♣']
    assert len(copas) == 13
    assert len(ouros) == 13
    assert len(espadas) == 13
    assert len(paus) == 13

def test_pop():
    """ Testa se o método pop() retira a carta do topo e remove do baralho. """
    baralho = Baralho()
    carta = baralho.virar()
    assert carta not in baralho.cartas
    assert len(baralho.cartas) == 51