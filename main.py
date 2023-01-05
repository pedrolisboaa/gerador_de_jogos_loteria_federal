from tipo_de_jogos import lotofacil, megasena, outraFuncoes, quina, lotomania, duplasena
from time import sleep

RESPOSTA_DE_ERRO = 'Você informou alguma coisa errada, favor refazer.'

print(f'Bem vindo ao seu sorteador de jogos para loteria federal da CAIXA ECONÔMICA!!')

while True:
   
    print(f'Informe qual aposta deseja fazer:')

    tipo_de_jogo = input(
        'MEGASENA [1] | LOTOFACIL [2] | QUINA [3] | LOTOMANIA [4] | DUPLASENA [5] | SAIR [Outra Tecla]: ')

    if tipo_de_jogo == '1':
        print('Jogos da Mega devem ter entre 6 e 20 números.')
        print()
        dados = outraFuncoes.receber_dados()
        verificacao = 6 <= int(dados[0]) <= 20

        if verificacao:
            jogo_da_mega = megasena.MegaSena(int(dados[0]), int(dados[1]))
            jogo_da_mega.mostrar_jogos()
            print('---------------')
            print(
                f'O valor final ficou em R$ {jogo_da_mega.calcular_valor_total_da_aposta():.2f}')
        else:
            print(RESPOSTA_DE_ERRO)

    elif tipo_de_jogo == '2':
        print('Jogos da Lotofacil devem ter entre 15 e 20 números.')
        print()
        dados = outraFuncoes.receber_dados()
        verificacao = 15 <= int(dados[0]) <= 20

        if verificacao:
            jogo = lotofacil.LotoFacil(int(dados[0]), int(dados[1]))
            jogo.mostrar_jogos()
            print('---------------')
            print(
                f'O valor final ficou em R$ {jogo.calcular_valor_total_da_aposta():.2f}')
        else:
            print(RESPOSTA_DE_ERRO)
    
    elif tipo_de_jogo == '3':
        print('Jogos da Quina devem ter entre 5 e 15 números.')
        print()
        dados = outraFuncoes.receber_dados()
        verificacao = 5 <= int(dados[0]) <= 15

        if verificacao:
            jogo = quina.Quina(int(dados[0]), int(dados[1]))
            jogo.mostrar_jogos()
            print('---------------')
            print(
                f'O valor final ficou em R$ {jogo.calcular_valor_total_da_aposta():.2f}')
        else:
            print(RESPOSTA_DE_ERRO)   

    elif tipo_de_jogo == '4':
        dados = outraFuncoes.recebe_dados_lotomania()
    
        jogo = lotomania.LotoMania(numero_de_apostas=int(dados))
        jogo.mostrar_jogos()
        print('---------------')
        print(
            f'O valor final ficou em R$ {jogo.calcular_valor_total_da_aposta():.2f}')
        
    elif tipo_de_jogo == '5':
            print('Jogos da dupla sena devem ter entre 6 e 15 números.')
            print()
            dados = outraFuncoes.receber_dados()
            verificacao = 6 <= int(dados[0]) <= 15

            if verificacao:
                jogo = duplasena.DuplaSena(int(dados[0]), int(dados[1]))
                jogo.mostrar_jogos()
                print('---------------')
                print(
                    f'O valor final ficou em R$ {jogo.calcular_valor_total_da_aposta():.2f}')
            else:
                print(RESPOSTA_DE_ERRO) 
    else:
        print('Muito obrigado por utilizar nosso sitemas.')
        print('A tela será fechada em 5 segundos.')
        sleep(5)
        break
        
