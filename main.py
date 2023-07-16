from conta import ContaBancaria, MovimentacaoException

conta = ContaBancaria()

mensagem_boas_vindas = f"""
    BEM-VINDO AO NUITANDER!
    {'-' * 50}
    Selecione uma opção abaixo para continuar:
"""

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

print(mensagem_boas_vindas)

while True:
    try:
        opcao = input(menu).lower()

        if opcao == 'd':
            conta.OperacaoDeposito()
        
        elif opcao == 's':
            conta.OperacaoSaque()
        
        elif opcao == 'e':
            conta.ConsultarExtrato()
        
        elif opcao == 'q':
            break

        else:
            print('Não foi possível realizar a operação solicitada.')

    except MovimentacaoException as movimentacaoError:
        print(movimentacaoError)

    except ValueError as valueError:
        print(f"""
        Não consegui entender o valor inserido.
        Se deseja fazer operações com valores decimais, troque a vírgula (,) por ponto (.).
""")
        
    except:
        print("Ops... Algo de errado não está certo!")