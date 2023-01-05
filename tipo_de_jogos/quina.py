from tipo_de_jogos import valores_jogos, megasena

class Quina(megasena.MegaSena):
    def __init__(self, numero_de_jogos_por_aposta, numero_de_apostas):
        super().__init__(numero_de_jogos_por_aposta, numero_de_apostas)
        self.todos_numeros = list(range(1, 81))

    def calcular_valor_total_da_aposta(self):
        return valores_jogos.QUINA[self.numero_de_jogos_por_aposta] * self.numero_de_aposta

