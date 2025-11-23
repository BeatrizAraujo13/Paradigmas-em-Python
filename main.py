from guerreiro import Guerreiro
from mago import Mago
from arqueiro import Arqueiro
from itens import Arma, Pocao
from inventario import Inventario
from inimigo import Monstro, Orc
from habilidades import AtaqueForte, BolaDeFogo
from habilidades import Dado
from batalha import Batalha

def exemplo():
    # Criando personagens
    g = Guerreiro('Arthur')
    m = Mago('Frieren')
    a = Arqueiro('Lyra')

    # Criando armas
    espada = Arma('Espada Longa', 8)
    cajado = Arma('Cajado Mágico', 5)
    arco = Arma('Arco Curvo', 6)
    pocao = Pocao('Poção de Vida', 25)

    # Equipando armas
    g.arma = espada
    m.arma = cajado
    a.arma = arco

    # Configurando inventário
    inv = Inventario()
    inv.adicionar(pocao)
    g.inventario = inv

    # Adicionando habilidades
    g.habilidades.append(AtaqueForte())
    m.habilidades.append(BolaDeFogo())

    # Criando monstros
    gob = Monstro.goblin_padrao()
    orc = Orc()

    # Config batalhas
    dado = Dado(seed=42)
    
    print("=== BATALHA 1 ===")
    batalha1 = Batalha(g, gob, dado)
    vencedor1 = batalha1.lutar()

    print('\n=== BATALHA 2 ===')
    batalha2 = Batalha(m, orc, dado)
    vencedor2 = batalha2.lutar()

    print('\n=== RESUMO FINAL ===')
    if vencedor1:
        print(f"Vencedor Batalha 1: {vencedor1.nome}")
    if vencedor2:
        print(f"Vencedor Batalha 2: {vencedor2.nome}")

if __name__ == '__main__':
    exemplo()