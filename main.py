from conta import ContaBancaria, MovimentacaoException
from banco import Banco
import sys

mensagem_boas_vindas = f"""
    BEM-VINDO AO NUITANDER!
    {'-' * 50}
    Realize seu login ou cadastro para continuar:
"""

banco = Banco()
banco.carregarBanco()



# def salvarBanco(banco):
#     with open('banco.pkl', 'wb') as file:
#         pickle.dump(banco, file)

# banco = None

# try:
#     with open('banco.pkl', 'rb') as f:
#         banco = pickle.load(f)
# except:


login = """
    [l] Login
    [c] Cadastro
    [q] Sair

=> """

menu_com_conta = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [a] Alterar conta
    [c] Criar uma nova conta
    [l] Listar minhas contas
    [q] Sair

=> """

menu_sem_conta = """
    [s] Selecionar conta
    [c] Criar uma nova conta
    [l] Listar minhas contas
    [q] Sair

=> """

print(mensagem_boas_vindas)

while True:
    if banco.usuario == None:
        opcao = input(login).lower()
        if opcao == 'l':
            cpf = int(input('Digite seu CPF: '))
            senha = input('Digite sua senha: ')
            banco.login(cpf, senha)
        elif opcao == 'c':
            banco.criarUsuario()
        elif opcao == 'q':
            banco.salvarBanco()
            sys.exit()
    else:
        if banco.contaAtual is None:
            opcao = input(menu_sem_conta).lower()
            
            if opcao == 's':
                banco.selecionarConta()
        else:
            opcao = input(menu_com_conta).lower()
            
            if opcao == 'a':
                banco.selecionarConta()
            
            if opcao == 'd':
                valor_depositar = float(input("Informe um valor que deseja depositar: "))
                banco.contaAtual.OperacaoDeposito(valor_depositar)
            
            elif opcao == 's':
                valor_sacar = float(input("Informe um valor que deseja sacar: "))
                banco.contaAtual.OperacaoSaque(valor=valor_sacar)
            
            elif opcao == 'e':
                movimentacoes = banco.contaAtual.movimentacoes
                saldo = banco.contaAtual.saldo
                banco.contaAtual.ConsultarExtrato(saldo, movimentacoes=movimentacoes)
        
        
        if opcao == 'c':
            banco.criarConta(banco.usuario.cpf)
        elif opcao == 'l':
            banco.listarContas()
        elif opcao == 'q':
            banco.logout()
        

# while True:

#         pass
#     try:
#         opcao = input(menu).lower()


#         elif opcao == 'q':
#             break

#         else:
#             print('Não foi possível realizar a operação solicitada.')

#     except MovimentacaoException as movimentacaoError:
#         print(movimentacaoError)

#     except ValueError as valueError:
#         print(f"""
#         Não consegui entender o valor inserido.
#         Se deseja fazer operações com valores decimais, troque a vírgula (,) por ponto (.).
# """)
        
#     except:
#         print("Ops... Algo de errado não está certo!")