from personagem import Personagem

class Mago(Personagem):
  def __init__(self, nome, vida_maxima=80, forca=8, poder_magico=20):
   super().__init__(nome, vida_maxima, forca)
   self.poder_magico = int(poder_magico)

  def atacar(self, alvo):
   dano = self.forca + int(self.poder_magico / 2)
   if self.arma:
    dano += self.arma.poder
   print(f"{self.nome} conjura magia e ataca {alvo.nome} causando {dano} de dano.")
   alvo.receber_dano(dano)