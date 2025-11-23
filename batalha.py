from personagem import Personagem

class Batalha:
    def __init__(self, combatente1, combatente2, dado=None):
        self.c1 = combatente1
        self.c2 = combatente2
        self.dado = dado

    def executar_turno(self, atacante, defensor):
        if not atacante.esta_vivo() or not defensor.esta_vivo():
            return
        
        multiplicador = 1
        if self.dado:
            multiplicador = 1 + (self.dado.rolar(6) - 3) * 0.05
        
        dano_base = atacante.forca + (atacante.arma.poder if atacante.arma else 0)
        dano = int(dano_base * multiplicador)
        
        print(f"{atacante.nome} ataca {defensor.nome} com dano {dano} (base {dano_base}, mult {multiplicador:.2f})")
        defensor.receber_dano(dano)

    def lutar(self):
        turno = 0
        print(f"Batalha iniciada: {self.c1.nome} vs {self.c2.nome}")
        
        while self.c1.esta_vivo() and self.c2.esta_vivo():
            if turno % 2 == 0:
                self.executar_turno(self.c1, self.c2)
            else:
                self.executar_turno(self.c2, self.c1)
            turno += 1

        # Determinar o vencedor
        if self.c1.esta_vivo():
            vencedor = self.c1
        elif self.c2.esta_vivo():
            vencedor = self.c2
        else:
            vencedor = None  #caso de empate

        if vencedor:
            print(f"Batalha finalizada. Vencedor: {vencedor.nome}")
        else:
            print("Batalha finalizada. Ambos morreram!")

        return vencedor