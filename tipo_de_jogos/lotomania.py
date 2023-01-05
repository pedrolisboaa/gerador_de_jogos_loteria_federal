from tipo_de_jogos import valores_jogos, megasena


class LotoMania(megasena.MegaSena):
    def __init__(self, numero_de_apostas, numero_de_jogos_por_aposta=50):
        super().__init__(numero_de_jogos_por_aposta, numero_de_apostas)
        self.todos_numeros = list(range(00, 100))

    def calcular_valor_total_da_aposta(self):
        return valores_jogos.LOTOMANIA[self.numero_de_jogos_por_aposta] * self.numero_de_aposta
