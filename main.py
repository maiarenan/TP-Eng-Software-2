from vite_e_um import Vinte_e_um

def main():
    while True:
        game = Vinte_e_um()
        jogador_venceu = game.distribui_primeira_rodada()
        
        if jogador_venceu:
            #CASO O JOGADOR VENÇA A PRIMEIRA RODADA, PERGUNTA SE ELE QUER JOGAR NOVAMENTE.
            resposta = input('Digite S para jogar novamente, ou N para parar de jogar').upper()
            if resposta == 'S':
                continue
            else:
                break
        else:
            fim_de_jogo = False
            while not fim_de_jogo:
                pass

if __name__ == '__main__':
    main()


