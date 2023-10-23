from system import Sistema, Observador
from conta import ContaBancaria
from user import Usuario
import pickle, os

class Banco(Sistema):
  
  _usuarios = []
  _contas = []
  contaAtual = None
  usuario = None
  
  def listarContas(self):
    contas = [conta if conta.cpf == self.usuario.cpf else None for conta in self._contas]
    if len(contas) == 0:
      print('Sem contas para exibir.')
    
    for conta in contas:
      print(f"AGÊNCIA: {conta.AGENCIA} CONTA: {conta.id}")
  
  def selecionarConta(self):
    contas = [conta if conta.cpf == self.usuario.cpf else None for conta in self._contas]
    id = int(input("Digite a conta que deseja selecionar: "))
    for conta in contas:
      print(conta.id)
      if conta.id == id:
        self.contaAtual = conta
        return
    
    print('Nenhuma conta foi encontrada.')

  def criarUsuario(self):
    nome = input("Digite o nome do usuário: ")
    dt_nascimento = input("Digite a data de nascimento (Padrão dd/mm/yyyy): ")
    endereco = self.criarEndereco()
    cpf = self.verificarCpf()
    senha = input("Digite sua senha: ")
    
    novo_usuario = {"nome": nome, "dt_nascimento": dt_nascimento, "cpf": cpf, "endereco": endereco, "senha": senha}
    self.novoUsuario(novo_usuario)
  
  def criarEndereco(self):
    logradouro = input("Digite o logradouro: ")
    nro = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    sigla_estado = input("Digite a sigla do estado: ")
    
    return f"{logradouro}, {nro} - {bairro} - {cidade} / {sigla_estado}"
  
  def verificarCpf(self):
    cpf = int(input("Digite o CPF (apenas números): "))
    lista_cpf = [user.cpf for user in self._usuarios]
    if cpf not in lista_cpf:
      return cpf
    else:
      print("Não é possível criar um usuário com este CPF, tente novamente.")
      self.verificarCpf()
  
  def novoUsuario(self, user):
    usuario = Usuario(user)
    self._usuarios.append(usuario)
    print("Usuário criado com sucesso!")
  
  def criarConta(self, cpf):
    novoId = len(self._contas)
    novaConta = ContaBancaria(cpf, novoId)
    self.add(novaConta, self._contas)
    print(f'Conta criada! Seguem os dados: {novaConta.AGENCIA}-{novaConta.id}')
  
  def login(self, cpf, senha):
      lista_cpf = [user.cpf for user in self._usuarios]
      if cpf not in lista_cpf:
        print("Usuário não encontrado na base de dados.")
        return
      
      user = [user for user in self._usuarios][0]
      
      if senha == user.senha:
        self.usuario = user
        print("Logado com sucesso.")
        print(f'Bem-vindo de volta, {user.nome}!')
        return
      
      print("Senha incorreta")
  
  def logout(self):
    self.usuario = None
    print("Usuário deslogado com sucesso!")
  
  def salvarBanco(self):
    os.makedirs('db/usuarios', exist_ok = True)
    os.makedirs('db/contas', exist_ok = True)
    with open(r'db/banco.pkl', 'wb') as file:
        pickle.dump(self, file)
    for id, usuario in enumerate(self._usuarios):
      with open(rf'db/usuarios/{id}.pkl', 'wb') as file:
        pickle.dump(usuario, file)
    for id, conta in enumerate(self._contas):
      with open(rf'db/contas/{id}.pkl', 'wb') as file:
        pickle.dump(conta, file)
  
  def carregarBanco(self):
    try:
      with open(r'db/banco.pkl', 'rb') as file:
        self = pickle.load(file)
      for usuario in os.listdir(r'db/usuarios'):
        with open(rf'db/usuarios/{usuario}', 'rb') as usuario:
          usuario = pickle.load(usuario)
          self._usuarios.append(usuario)
      for conta in os.listdir(r'db/contas'):
        with open(rf'db/contas/{conta}', 'rb') as conta:
          conta = pickle.load(conta)
          self._contas.append(conta)
    except:
      pass
    
  def add(self, observador: Observador, lista):
    lista.append(observador)
  
  def rm(self, observador: Observador, lista: list):
    lista.remove(observador)
  