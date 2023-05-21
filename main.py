from vinte_e_um import Vinte_e_um
import sys

def main():
    while True:
        game = Vinte_e_um()
        jogador_venceu = game.distribui_primeira_rodada()
        
        print('Embaralhando cartas...')
        
        if jogador_venceu:
            #CASO O JOGADOR VENÇA A PRIMEIRA RODADA, PERGUNTA SE ELE QUER JOGAR NOVAMENTE.
            resposta = input('Digite S para jogar novamente, ou N para parar de jogar: ').upper()
            
            if resposta == 'S':
                continue
            else:
                sys.exit(1)
        else:
            fim_de_jogo = False
            
            while not fim_de_jogo:
                continuar = game.perguntar_jogador_proxima_jogada()
                
                if continuar:
                    perdeu = game.inserir_carta_jogador()
                    game.mostrar_score_jogador()

                    if perdeu:
                        print(f'Ooopsss {game.jogador.name}, você estourou o limite!!!')
                        game.mostrar_score_jogador()
                        game.mostrar_score_croupier()
                        
                        resposta = input('Digite S para jogar novamente, ou N para parar de jogar: ').upper()
                        
                        if resposta == 'S':
                            fim_de_jogo = True
                        else:
                            sys.exit(1)
        
                else:
                    game.mostrar_score_jogador()
                    game.croupier_comprar_cartas_ate_passar_jogador()
                    game.definir_vencedor()
                    
                    resposta = input('Digite S para jogar novamente, ou N para parar de jogar: ').upper()
                    
                    if resposta == 'S':
                        fim_de_jogo = True
                    else:
                        sys.exit(1)

if __name__ == '__main__':
    main()


