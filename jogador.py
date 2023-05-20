import mao as Mao
class Jogador():
    def __init__(self, name = ''):
        self.name = name
        self.saldo = 0
        self.mao = Mao.Mao()
    
    def set_nome(self, name):
        self.name = name
    
    def get_nome(self):
        return self.name
    
    def set_saldo(self, saldo):
        self.saldo = saldo
    
    def insert_card(self, card):
        self.mao.insert_card(card)
    
    def get_mao(self):
        return self.mao.get_cartas()
    
    def get_score(self):
        return self.mao.score

    
# Compare this snippet from test_jogador.py:
