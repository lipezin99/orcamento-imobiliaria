
class Imovel:
    def __init__(self, valor_base):
        self.valor_base = valor_base
        self.valor_final = valor_base

    def calcular_valor(self):
        return self.valor_final


class Apartamento(Imovel):
    def __init__(self, quartos, garagem, possui_criancas):
        super().__init__(700)
        self.quartos = quartos
        self.garagem = garagem
        self.possui_criancas = possui_criancas
        self.calcular()

    def calcular(self):
        if self.quartos == 2:
            self.valor_final += 200

        if self.garagem:
            self.valor_final += 300

        if not self.possui_criancas:
            self.valor_final *= 0.95


class Casa(Imovel):
    def __init__(self, quartos, garagem):
        super().__init__(900)
        self.quartos = quartos
        self.garagem = garagem
        self.calcular()

    def calcular(self):
        if self.quartos == 2:
            self.valor_final += 250

        if self.garagem:
            self.valor_final += 300


class Estudio(Imovel):
    def __init__(self, vagas):
        super().__init__(1200)
        self.vagas = vagas
        self.calcular()

    def calcular(self):
        if self.vagas >= 2:
            self.valor_final += 250
            if self.vagas > 2:
                self.valor_final += (self.vagas - 2) * 60
