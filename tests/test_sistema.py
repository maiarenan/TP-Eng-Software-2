import pytest
import subprocess
from vinte_e_um import Vinte_e_um
import warnings

warnings.filterwarnings("ignore")

@pytest.mark.cmd
def test_cadastro_jogador_ao_iniciar_jogo():
    path =  r"C:\Users\rodri\Desktop\Atividades\app_21\TP-Eng-Software-2\main.py"
    
    processo = subprocess.Popen(['python', path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    processo.stdin.write('Rodrigo' + "\n")

    output, errors = processo.communicate()
    processo.stdin.close()
    
    assert "Olá Rodrigo, bem vindo ao nosso jogo de 21. Esperamos que você se divirta muito!!!" in output

@pytest.mark.cmd
def test_score_do_jogador_maior_que_0_apos_comecar_jogo():
    path =  r"C:\Users\rodri\Desktop\Atividades\app_21\TP-Eng-Software-2\main.py"
    
    processo = subprocess.Popen(['python', path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    processo.stdin.write('Rodrigo' + "\n")
    
    output, errors = processo.communicate()
    processo.stdin.close()
    
    score_jogador = int(output.split("Score do jogador: ")[0])

    assert score_jogador > 0
