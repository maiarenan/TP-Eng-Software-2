import pytest
from baralho import Baralho, Carta

@pytest.fixture
def baralho():
    baralho = Baralho()
    return baralho  

def test_quantidade_de_cartas_no_baralho(baralho):
    
    assert len(baralho.cartas) == 52

def test_quantidade_de_carta_por_naipes(baralho):
    
    copas = [carta for carta in baralho.cartas if carta.naipe == '♥']
    ouros = [carta for carta in baralho.cartas if carta.naipe == '♦']
    espadas = [carta for carta in baralho.cartas if carta.naipe == '♠']
    paus = [carta for carta in baralho.cartas if carta.naipe == '♣']
    
    assert len(copas) == 13
    assert len(ouros) == 13
    assert len(espadas) == 13
    assert len(paus) == 13

def test_baralho_sem_cartas_repetidas(baralho):
    
    quantidade_elementos_unicos = len(set(baralho.cartas))
    quantidade_de_cartas_no_baralho = len(baralho.cartas)
    
    assert quantidade_elementos_unicos == quantidade_de_cartas_no_baralho

def test_carta_removida_nao_esta_no_baralho(baralho):
    
    carta = baralho.virar()
    
    assert carta not in baralho.cartas

def test_quantidade_de_cartas_no_baralho_pos_remocao(baralho):
    
    carta = baralho.virar()
    carta = baralho.virar()
    carta = baralho.virar()
    
    assert len(baralho.cartas) == 49

def teste_quantidade_de_cartas_no_baralho_nao_embaralhado(baralho):
    
    baralho.novo_deque_nao_embaralhado()

    assert len(baralho.cartas) == 52

def teste_primeira_carta_do_baralho_nao_embaralhado(baralho):

    baralho.novo_deque_nao_embaralhado()
    carta = baralho.virar()
    primeira_carta = Carta('K', '♣')
   
    assert carta == primeira_carta
