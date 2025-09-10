'''
O que é Polimorfismo?

É quando um mesmo metodo tem comportamentos diferentes dependendo da classe que o usa.

Pensa assim:

Todas as classes têm o metodo aprensentar()

Mas cada classe fala de um jeito proprio quando voce chama esse metodo
'''


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, eu sou {self.nome}")

class Cliente(Pessoa):
    def apresentar(self):
        print(F"Sou cliente {self.nome}, vim comprar algo.")

class Aluno (Pessoa):
    def apresentar(self):
        print(f"Sou aluno {self.nome}, estou estudando.")

p = Pessoa("João")
c = Cliente("Maria")
a = Aluno ("Pedro")
#chamando o mesmo metodo "apresentar"
p.apresentar()
c.apresentar()
a.apresentar()



