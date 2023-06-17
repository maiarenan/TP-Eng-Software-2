import pytest
import subprocess
import warnings
import os
import re
warnings.filterwarnings("ignore")

#prepara o path para o arquivo main.py
@pytest.fixture
def path():
    current_dir = os.path.abspath(os.path.dirname(__file__))

    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    path_main = os.path.join(parent_dir, "main.py")
    
    return path_main


@pytest.mark.cmd
def test_cadastro_jogador_ao_iniciar_jogo(path):
    warnings.filterwarnings("ignore")

    processo = subprocess.Popen(['python', path], 
                                stdin=subprocess.PIPE, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                universal_newlines=True)
    
    naipes = {
    'HEART SUIT': '\u2665',
    'DIAMOND SUIT': '\u2666',
    'CLUB SUIT': '\u2663',
    'SPADE SUIT': '\u2660'
    } 

    nome  = "Rodrigo"
    processo.stdin.write(nome + "\n")
    processo.stdin.flush()

    saida, _ = processo.communicate()

    processo.stdin.close()
    processo.stderr.close()

    #monta a regex para remover os naipes
    regex = re.compile('|'.join(re.escape(naipes) for naipes in naipes.values()))

    saida_limpa = regex.sub('',saida)
    
    assert f"Olá {nome}, bem vindo ao nosso jogo de 21. Esperamos que você se divirta muito!!!" in saida_limpa

@pytest.mark.flaky(reruns=5)
@pytest.mark.cmd
def test_score_do_jogador_maior_que_0_apos_primeira_jogada(path):
    warnings.filterwarnings("ignore")

    processo = subprocess.Popen(['python', path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    processo.stdin.write('Rodrigo' + "\n")
    processo.stdin.flush()
    processo.stdin.write('S' + "\n")
    processo.stdin.flush()
    
    output, errors = processo.communicate()
    processo.stdin.close()
    
    score_jogador = int(output.split("Score do jogador: ")[1][0:2])
    
    assert score_jogador > 0

