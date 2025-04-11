class CarteiraInvestimento:
    def _init_(self):
        self.numero = 0
        self.saldo = 0.0
    def get_numero(self):
        return self.numero
    def set_numero(self, numero):
        self.numero = numero
    def get_saldo(self):
        return self.saldo
    def set_saldo(self, saldo):
        self.saldo = saldo
    def investir(self, valor):
        self.saldo += valor
    def restagar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor

class BolsaValores(CarteiraInvestimento):
    def _init_(self):
        CarteiraInvestimento._init_(self)
    def investir(self, valor):
        self.saldo += valor - 50

class Investimento(CarteiraInvestimento):
    def _init_(self):
        CarteiraInvestimento._init_(self)
    def resgatar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            self.saldo -= valor * 0.01

bolsa = BolsaValores()
bolsa.investir(3000.0)
print(bolsa.get_saldo())

investimento = Investimento()
investimento.investir(5000.0)
print(investimento.get_saldo())

bolsa.restagar(200)
print(bolsa.get_saldo())
bolsa.restagar(2800)

investimento.resgatar(700)
print(investimento.get_saldo())
investimento.resgatar(4300)