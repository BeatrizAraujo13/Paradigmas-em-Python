from personagem import Personagem
import random

class Arqueiro(Personagem):
    def __init__(self, nome, vida_maxima=90, forca=10, precisao=80):
        super().__init__(nome, vida_maxima, forca)
        self.precisao = int(precisao) 

    def atacar(self, alvo):
        
        chance = self.precisao
        roll = random.randint(1, 100) 
        
        if roll <= chance:
            dano = self.forca + (self.arma.poder if self.arma else 0)
            print(f"{self.nome} acerta o alvo ({roll} <= {chance}) e causa {dano} de dano.")
            alvo.receber_dano(dano)
        else:

            print(f"{self.nome} errou o ataque ({roll} > {chance}).")
