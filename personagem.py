class Personagem:
    def __init__(self, nome, vida_maxima, forca):
        self.nome = nome
        self._vida_maxima = int(vida_maxima)
        self._vida = int(vida_maxima)
        self.forca = int(forca)
        self.inventario = None
        self.arma = None
        self.habilidades = []

    def __str__(self):
        return f"{self.nome} - Vida: {self._vida}/{self._vida_maxima} - Força: {self.forca}"

    def get_vida(self):
        return self._vida

    def set_vida(self, valor):
        valor = int(valor)
        if valor < 0:
            self._vida = 0
        elif valor > self._vida_maxima:
            self._vida = self._vida_maxima
        else:
            self._vida = valor

    def get_vida_maxima(self):
        return self._vida_maxima

    def receber_dano(self, dano):
        dano = int(dano)
        self.set_vida(self.get_vida() - dano)
        print(f"{self.nome} recebeu {dano} de dano. Vida agora: {self.get_vida()}/{self.get_vida_maxima()}")

    def esta_vivo(self):
        return self.get_vida() > 0

    def atacar(self, alvo):
        dano = self.forca
        if self.arma:
            dano += self.arma.poder
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")
        alvo.receber_dano(dano)

    def usar_habilidade(self, indice, alvo):
        if indice < 0 or indice >= len(self.habilidades):
            print("Habilidade inválida")
            return
        habilidade = self.habilidades[indice]
        habilidade.usar(self, alvo)