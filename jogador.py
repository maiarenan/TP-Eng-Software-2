class Jogador():
    def __init__(self, name = ''):
        self.name = name
    
    def cumprimento_jogador(self):
        print(f'Olá {self.name}, seja bem vindo ao nosso jogo de 21! Espero que vocês se divirtam muito.')

    def inserir_nome(self):
        self.name = input('Qual o seu nome? ')
