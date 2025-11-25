class Habilidade:
  def usar(self, usuario, alvo):
   raise NotImplementedError('Método usar deve ser implementado pela habilidade')


class AtaqueForte(Habilidade):
  def usar(self, usuario, alvo):
   dano = int(usuario.forca * 1.8)
   if usuario.arma:
    dano += usuario.arma.poder
    print(f"{usuario.nome} usa Ataque Forte contra {alvo.nome} causando {dano} de dano.")
    alvo.receber_dano(dano)


class BolaDeFogo(Habilidade):
  def usar(self, usuario, alvo):
   poder = getattr(usuario, 'poder_magico', 0)
   dano = int(poder * 1.5) + 5
   print(f"{usuario.nome} lança Bola de Fogo em {alvo.nome} causando {dano} de dano.")
   alvo.receber_dano(dano) 

#Dado
class Dado:
  def __init__(self, seed=1):
   self._state = int(seed)


  def _next(self):
   a = 1664525
   c = 1013904223
   m = 2 ** 32
   self._state = (a * self._state + c) % m
   return self._state


  def rolar(self, lados=6):
   val = (self._next() % lados) + 1

   return val
