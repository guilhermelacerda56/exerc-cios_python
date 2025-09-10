#classe palavra chave no python para definir uma classe 
#carro nome que damos a classe por convenção começa com letra maiuscula se for mome composto, usamos camel case ex: minha casa
#def palavra chave que define uma função ou metodo no python 
#__int__ metodo contrutor da classe.ele e chamado automaticamente quando criamos a classe com um novo objeto serve para inicializar atributos do objeto 
# self uma referencia ao proprio objeto que esta sendo criado 
class carro:
    '''
    comente mais de uma linha 3 aspas simples
    '''
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 
    def acelerar(self):
        print(f" carro {self.marca} {self.modelo} esta acelerando")

# criando dois objetos diferentes 
carro1 = carro ("toyota", "corolla")
carro2 = carro ("honda", "civic")
carro3 = carro ("nissan","gtr r34")

# chamando metodos 
carro1.acelerar() #usa os atributos do carro1
carro2.acelerar() #use os atributos do carro2
carro3.acelerar() #use os atributos do carro3
