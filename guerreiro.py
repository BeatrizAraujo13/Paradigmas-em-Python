from personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome, vida_maxima=120, forca=15):
        super().__init__(nome, vida_maxima, forca)

    def atacar(self, alvo):
        dano = self.forca + (self.arma.poder if self.arma else 0)  # Corrigido: self.forca
        print(f"{self.nome} (Guerreiro) desfere um golpe poderoso em {alvo.nome}, causando {dano} de dano.")
        alvo.receber_dano(dano)