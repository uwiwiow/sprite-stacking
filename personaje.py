class Personaje:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia

    def alimentarse(self, cant):
        self.energia += cant


class Guerrero(Personaje):
    def __init__(self, nombre, energia, arma):
        super().__init__(nombre, energia)
        self.arma = arma

    def combatir(self, cant):
        self.energia -= cant
        return self.arma, cant


class Mago(Personaje):
    def __init__(self, nombre, poder):
        super().__init__(nombre, energia=100)
        self.poder = poder

    def encantar(self):
        self.energia -= 2
        return self.poder
