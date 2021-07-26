
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


calculadora = Calculadora(10, 2)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())

class Carro:
    def __init__(self):
        self.motor = 'desligado'
        self.movimento = False

    def ligar(self):
        self.motor = 'ligado'

    def acelerar(self):
        if self.motor == 'ligado':
            self.movimento = True

    def carro_em_movimento(self):
        return self.movimento


carro = Carro()
carro.acelerar()
carro_em_movimento = carro.carro_em_movimento()
print(carro_em_movimento)