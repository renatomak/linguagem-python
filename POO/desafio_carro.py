class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        maxima = self.velocidade_maxima
        nova = self.velocidade_atual + delta

        self.velocidade_atual = nova if nova <= maxima else maxima

        return self.velocidade_atual

    def frear(self, delta=5):
        nova = self.velocidade_atual - delta
        self.velocidade_atual = nova if nova >= 0 else 0

        return self.velocidade_atual

# def acelerar(self, value=5):
#         self.velocidade_atual += value
#         if self.velocidade_atual > self.velocidade_maxima:
#             self.velocidade_atual = self.velocidade_maxima
#         return self.velocidade_atual
# def frear(self, delta=5):
#     self.velocidade_atual -= delta
#     if self.velocidade_atual < 0:
#         self.velocidade_atual = 0
#     return self.velocidade_atual


if __name__ == '__main__':
    c1 = Carro(180)
    print('COMEÇA A ACELERRAR')
    for _ in range(25):
        print(c1.acelerar(8))
    print('COMEÇA A FREAR')

    for _ in range(10):
        print(c1.frear(delta=20))
