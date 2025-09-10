'''
O que é abstração?

 É esconder os detalhes internos de implementação e mostrar apenas o necessario.

A ideia é trabalhar no nível mais generico e deixar que as classes
mais especificas implementem os detalhes

'''

from abc import ABC, abstractmethod

# Classe abstrata (não pode ser instanciada diretamente)
class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def apresentar(self):
        pass

#Classe concreta Cliente
class Cliente(Pessoa):
    def apresentar(self):
        print(f"Sou cliente {self.nome}, comprando no sistema.")

# Classe Concreta Aluno
class Aluno(Pessoa):
    def apresentar(self):
        print(f"Sou aluno {self.nome}, estudando no sistema.")

# p = Pessoa("Carlos") # Isso dá erro: Pessoa é abstrata!

c = Cliente("Ana")
a = Aluno("Marcos")

c.apresentar()
a.apresentar()