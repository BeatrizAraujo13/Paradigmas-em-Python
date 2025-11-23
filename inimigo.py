from personagem import Personagem
import random

class Monstro(Personagem):
    def __init__(self, nome, vida_maxima, forca):
        super().__init__(nome, vida_maxima, forca)

    def goblin_padrao():
        return Monstro('Goblin', vida_maxima=30, forca=6)

class Orc(Monstro):
    def __init__(self, nome='Orc', vida_maxima=60, forca=12, crit_chance=20):
        super().__init__(nome, vida_maxima, forca)
        self.crit_chance = int(crit_chance)

    def atacar(self, alvo):
        roll = random.randint(1, 100)
        dano = self.forca
        
        if self.arma:
            dano += self.arma.poder
            
        if roll <= self.crit_chance:
            dano *= 2
            print(f"{self.nome} acerta um golpe crítico! (roll {roll} <= {self.crit_chance})")
        else:
            print(f"{self.nome} ataca normalmente. (roll {roll} > {self.crit_chance})")
            
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")
        alvo.receber_dano(dano)