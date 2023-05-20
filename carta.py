from dataclasses import dataclass


@dataclass(frozen=True)
class Carta:
    valor: str
    naipe: str

    def __str__(self):
        return self.valor + self.naipe

    def __repr__(self):
        return self.valor + self.naipe
