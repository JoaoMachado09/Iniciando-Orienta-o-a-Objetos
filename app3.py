class CarteiraInvestimento:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    # Métodos GET
    def get_numero(self):
        return self.numero

    def get_saldo(self):
        return self.saldo

    # Métodos SET
    def set_numero(self, numero):
        self.numero = numero

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.saldo = saldo
        else:
            print("Saldo não pode ser negativo!")

    def investir(self, valor):
        pass  # Método será implementado nas classes filhas

    def resgatar(self, valor):
        pass  # Método será implementado nas classes filhas


class BolsaValores(CarteiraInvestimento):
    def __init__(self, numero, saldo=0):
        super().__init__(numero, saldo)

    def investir(self, valor):
        taxa = 50
        if valor > taxa:
            self.saldo += (valor - taxa)
            print(f"Investido R$ {valor:.2f} na Bolsa de Valores. Taxa de R$ 50,00 cobrada.")
        else:
            print("Valor insuficiente para cobrir a taxa de R$ 50,00!")

    def resgatar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Resgatado R$ {valor:.2f} da Bolsa de Valores.")
        else:
            print("Saldo insuficiente para resgate!")


class Investimento(CarteiraInvestimento):
    def __init__(self, numero, saldo=0):
        super().__init__(numero, saldo)

    def investir(self, valor):
        self.saldo += valor
        print(f"Investido R$ {valor:.2f} na carteira de Investimento.")

    def resgatar(self, valor):
        taxa = valor * 0.01  # 1% de taxa
        valor_total = valor + taxa
        if self.saldo >= valor_total:
            self.saldo -= valor_total
            print(f"Resgatado R$ {valor:.2f} da carteira de Investimento. Taxa de R$ {taxa:.2f} cobrada.")
        else:
            print("Saldo insuficiente para resgate!")


# Criando as carteiras
bolsa = BolsaValores(numero=101, saldo=1000)
investimento = Investimento(numero=202, saldo=2000)

# Testando a carteira de Bolsa de Valores
print("\n--- Testando Bolsa de Valores ---")
print("Número da carteira:", bolsa.get_numero())
print("Saldo inicial:", bolsa.get_saldo())
bolsa.investir(500)   # Investe 500, taxa de 50 descontada
print("Saldo após investimento:", bolsa.get_saldo())
bolsa.resgatar(300)   # Resgata 300
print("Saldo após resgate:", bolsa.get_saldo())

# Testando a carteira de Investimentos
print("\n--- Testando Carteira de Investimentos ---")
print("Número da carteira:", investimento.get_numero())
print("Saldo inicial:", investimento.get_saldo())
investimento.investir(500)   # Investe 500 (sem taxa)
print("Saldo após investimento:", investimento.get_saldo())
investimento.resgatar(300)   # Resgata 300 (com 1% de taxa)
print("Saldo após resgate:", investimento.get_saldo())

# Modificando número e saldo com os métodos SET
print("\n--- Modificando dados das carteiras ---")
bolsa.set_numero(303)
bolsa.set_saldo(2000)
print("Novo número da carteira:", bolsa.get_numero())
print("Novo saldo da carteira:", bolsa.get_saldo())

investimento.set_numero(404)
investimento.set_saldo(3000)
print("Novo número da carteira de Investimentos:", investimento.get_numero())
print("Novo saldo da carteira de Investimentos:", investimento.get_saldo())
