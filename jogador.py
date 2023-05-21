import mao as Mao
class Jogador():
    def __init__(self, name = ''):
        self.name = name
        self.mao = Mao.Mao()
    
    def cumprimentar_jogador(self):
        print(f'Olá {self.name}, bem vindo ao nosso jogo de 21. Esperamos que você se divirta muito!!!')
        print()

    def set_nome(self, name):
        self.name = name
    
    def get_nome(self):
        return self.name
    
    def insert_card(self, card):
        self.mao.insert_card(card)
    
    def get_mao(self):
        return self.mao.get_cartas()
    
    def get_score(self):
        return self.mao.score

    
