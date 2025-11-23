class Inventario:
  def __init__(self):
   self.itens = []


  def adicionar(self, item):
   self.itens.append(item)
   print(f"{item.nome} adicionado ao inventário.")

  def remover(self, item):
   if item in self.itens:
    self.itens.remove(item)
    print(f"{item.nome} removido do inventário.")
   else:
    print(f"{item.nome} não encontrado no inventário.")


  def listar(self):
   return [getattr(i, 'nome', str(i)) for i in self.itens]


  def encontrar_pocao(self):
   for item in self.itens:
    if item.__class__.__name__ == 'Pocao':
     return item
    return None