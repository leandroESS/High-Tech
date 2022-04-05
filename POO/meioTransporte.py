class MeioTransporte():
    def __init__(self, velocidade, marca, valor, vendido):
        self.__velocidade = velocidade
        self.__marca = marca
        self.__valor = valor
        self.__vendido = vendido

    def vender(self):
        self.vendido = True
        print("O meio de transporte está vendido")


