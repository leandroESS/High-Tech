import taa


class carro(taa.Terrestre):
    def __init__(self, velocidade, marca, valor, vendido, ruaTerminal):
        super().__init__(velocidade, marca, valor, vendido, ruaTerminal)



class caminhao(taa. Terrestre):
    def __init__(self, velocidade, marca, valor, vendido, ruaTerminal):
        super().__init__(velocidade, marca, valor, vendido, ruaTerminal)



class Remo(taa.Aquatico):
    def __init__(self, velocidade, marca, valor, vendido, oceanoOrigem):
        super().__init__(velocidade, marca, valor, vendido, oceanoOrigem)


class Barco(taa.Aquatico):
    def __init__(self, velocidade, marca, valor, vendido, oceanoOrigem):
        super().__init__(velocidade, marca, valor, vendido, oceanoOrigem)


class Aviao(taa.Aereo):
    def __init__(self, velocidade, marca, valor, vendido, escalaOrDest):
        super().__init__(velocidade, marca, valor, vendido, escalaOrDest)
        self.escalaOrDest = escalaOrDest

class Helicotero(taa.Aereo):
    def __init__(self, velocidade, marca, valor, vendido, escalaOrDest):
        super().__init__(velocidade, marca, valor, vendido, escalaOrDest)
        self.escalaOrDest = escalaOrDest