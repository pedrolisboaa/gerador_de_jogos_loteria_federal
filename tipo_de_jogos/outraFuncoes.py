def recebe_dados_lotomania():
    qtd_jogos = input('Informe quantos jogos você deseja realizar: ')
    return qtd_jogos


def receber_dados():
    numeros_por_jogos = input('Informe a quantidade de números por jogo: ')
    qtd_jogos = input('Informe quantos jogos você deseja realizar: ')
    return [numeros_por_jogos, qtd_jogos]