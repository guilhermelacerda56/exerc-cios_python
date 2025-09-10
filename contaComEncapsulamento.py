class ContaBancaria:
    def __init__(self, titular, saldo_inicial, senha):
        # Público: Pode ser acessado Livremente
        self.titular = titular
        # Protegido: não deve ser alterado diretamente
        self._saldo = float(saldo_inicial)

        # privado: não pode ser acessado diretamente
        self._senha = str(senha)

    def ver_saldo(self, senha_digitada):
        # Verifica se a senha está correta
        if str(senha_digitada) == self._senha:
            print(f"Saldo de {self.titular}: R${self._saldo} ")
        else:
            print("Senha incorreta! Acesso negado.")

# Teste
conta2 = ContaBancaria("Guilherme", 1000.00, "1234")
# Consulta com senha correta
conta2.ver_saldo("1234")

# Tentando acessar protegido
conta2._saldo = 50.00
conta2.ver_saldo("1234")

# Tentando acessar privado (não funciona)
try:
    print(conta2._senha)
except AttributeError:
    print("Atributo privado não pode ser acessado diretamente.")