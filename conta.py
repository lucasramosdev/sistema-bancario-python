import datetime
from system import Observador

class ContaBancaria(Observador):
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    def __init__(self, cpf, id) -> None:
        self.saldo = 0
        self.limite = 500
        self.movimentacoes = ""
        self.numero_saques = 0
        self.cpf = cpf
        self.id = id

    def OperacaoSaque(self, *, valor):
        self.__sacar__(valor)
        print(f'R$ {valor:.2f} sacado com sucesso!')
    
    def OperacaoDeposito(self, valor, /):
        self.__depositar__(valor)
        print(f'R$ {valor:.2f} despositado com sucesso!')
    
    def ConsultarExtrato(self, saldo, /, *, movimentacoes):
        print(f"""
    {'EXTRATO BANCÁRIO'.center(50, '-')}
    {f'CONTA: {self.AGENCIA}-{self.id}'.center(50, ' ')}
    
    {movimentacoes if movimentacoes != "" else "Não há movimentações"}

    SALDO: R$ {saldo:.2f} - NÚMERO DE SAQUES RESTANTES: {self.LIMITE_SAQUES - self.numero_saques}
    {'-' * 50}
""")

    
    def __adicionar_movimentacao__(self, movimentacao):
        dataAtual = datetime.datetime.now()
        dataAtual = dataAtual.strftime("%d/%m/%y %H:%M:%S")
        self.movimentacoes += f'''{movimentacao} - {dataAtual}
    '''

    
    def __sacar__(self, valor):
        if valor > self.saldo:
            raise MovimentacaoException('Valor de saque maior que o saldo.')
        elif valor > self.limite:
            raise MovimentacaoException('Valor de saque maior que o limite permitido.')
        elif self.numero_saques > self.LIMITE_SAQUES:
            raise MovimentacaoException('Número de saques diários atingidos, tente novamente amanhã.')

        self.numero_saques += 1
        self.saldo -= valor
        movimentacao = f"Sacado R$ {valor:.2f}"
        self.__adicionar_movimentacao__(movimentacao)
    
    def __depositar__(self, valor):
        if valor <= 0:
            raise MovimentacaoException('Valor precisa ser maior que 0.')
        
        self.saldo += valor
        movimentacao = f"Depositado R$ {valor:.2f}"
        self.__adicionar_movimentacao__(movimentacao)

class MovimentacaoException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
