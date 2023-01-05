from random import sample
from tipo_de_jogos import valores_jogos


class MegaSena:
    def __init__(self, numero_de_jogos_por_aposta, numero_de_apostas):
        self.numero_de_jogos_por_aposta = numero_de_jogos_por_aposta
        self.numero_de_aposta = numero_de_apostas
        self.todos_numeros = list(range(1, 61))

    def sortear_jogos(self):
        todos_jogos = []
        for n in range(self.numero_de_aposta):
            jogo_novo = sample(self.todos_numeros,
                               self.numero_de_jogos_por_aposta)
            jogo_novo.sort()
            todos_jogos.append(jogo_novo)

        return todos_jogos
    
    def mostrar_jogos(self):
        for n in self.sortear_jogos():
            print(n)

    def calcular_valor_total_da_aposta(self):
        return valores_jogos.MEGA_SENA[self.numero_de_jogos_por_aposta] * self.numero_de_aposta
    
    
