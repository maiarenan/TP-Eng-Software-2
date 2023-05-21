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

    def calcula_valor_mao(self, card):
        if card.valor == 'A':
            return self.calcular_score_se_as(card)
        
        else:
            self.score += const.cartas_valor_no_21.get(card.valor)

    def verifica_se_perdeu(self):
        return self.score > 21
    
    def verifica_se_vitoria_blackjack(self):
        #as duas cartas iniciais seriam um Ás e outra que vale 10 pontos
        return self.score == 21 and len(self.cartas) == 2

    def set_aposta(self, aposta):
        self.aposta = aposta
    
    def get_cartas(self):
        return self.cartas
    
    def insert_card(self, card):
        self.cartas.append(card)
        self.calcula_valor_mao(card)

    def get_score(self):
        return self.score