class Arma:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = int(poder)

    def __str__(self):
        return f"{self.nome} (+{self.poder})"
  
class Pocao:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = int(cura)

    def usar(self, alvo):
        antes = alvo.get_vida()
        nova_vida = antes + self.cura
        alvo.set_vida(nova_vida)  
        curado = alvo.get_vida() - antes
        print(f"{alvo.nome} usa {self.nome} e recupera {curado} de vida. Vida: {alvo.get_vida()}/{alvo.get_vida_maxima()}")