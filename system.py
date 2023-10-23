from abc import ABC, abstractmethod


class Observador(ABC):
  
  @abstractmethod
  def __init__(self) -> None:
    pass

class Sistema(ABC):
  
  @abstractmethod
  def add(self, observador: Observador, lista: list):
    pass
  
  @abstractmethod
  def rm(self, observador: Observador, lista: list):
    pass