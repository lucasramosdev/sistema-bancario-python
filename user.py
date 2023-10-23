from system import Observador

class Usuario(Observador):
  def __init__(self, user):
    self.nome = user["nome"]
    self.senha = user["senha"]
    self.dt_nascimento = user["dt_nascimento"]
    self.cpf = user["cpf"]
    self.endereco = user["endereco"]