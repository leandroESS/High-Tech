import meioTransporte


class Terrestre(meioTransporte.MeioTransporte):
    def __init__(self, velocidade, marca, valor, vendido, ruaTerminal):
        super().__init__(velocidade, marca, valor, vendido)
        self.ruaTerminal = ruaTerminal


class Aquatico(meioTransporte.MeioTransporte):
    def __init__(self, velocidade, marca, valor, vendido, oceanoOrigem):
        super().__init__(velocidade, marca, valor, vendido)
        self.oceanoOrigem = oceanoOrigem


class Aereo(meioTransporte.MeioTransporte):
    def __init__(self, velocidade, marca, valor, vendido, escalaOrDest):
        super().__init__(velocidade, marca, valor, vendido)
        self.escalaOrDest = escalaOrDest
