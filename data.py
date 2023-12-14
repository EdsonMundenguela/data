# Classe data

class Data(object):
    # Método Construtor
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Encapsulamento

    def setDia(self, dia):
        self.dia = dia

    def getDia(self):
        return self.dia

    def setMes(self, mes):
        self.mes = mes

    def getMes(self):
        return self.mes

    def setAno(self, ano):
        self.ano = ano

    def getAno(self):
        return self.ano

    # Retorna os dados da classe

    def __str__(self):
        return \
 \
            (
                    '\n Dia:' + str(self.getDia()) +
                    '\n Mes:' + str(self.getMes()) +
                    '\n Ano:' + str(self.getAno())
            )
