import constantes as const

class Mao():
    def __init__(self):
        self.cartas = []
        self.score = 0

    def calcular_score_se_as(self, card):
        if self.score < 11:
            self.score += 11
        else:
            self.score += 1

    def valor_mao(self, card):
        if card.valor == 'A':
            return self.calcular_score_se_as(card)
        else:
            self.score += const.cartas_valor_no_21.get(card.valor)
    
    def insert_card(self, card):
        self.cartas.append(card)
        self.valor_mao(card)