from abc import ABC, abstractmethod

# Classe Abstrata
class Veiculo(ABC):

    @abstractmethod
    def mover(self) -> str:
        pass

    @abstractmethod
    def tipo_combustivel(self) -> str:
        pass


# Classes concretas
class Carro(Veiculo):
    def mover(self):
        return "Carro andando na estrada"

    def tipo_combustivel(self):
        return "Gasolina ou Etanol"


class Moto(Veiculo):
    def mover(self):
        return "Moto acelerando"

    def tipo_combustivel(self):
        return "Gasolina"


class Barco(Veiculo):
    def mover(self):
        return "Barco navegando na água"

    def tipo_combustivel(self):
        return "Diesel"


class Bicicleta(Veiculo):
    def mover(self):
        return "Bicicleta sendo pedalada"

    def tipo_combustivel(self):
        return "Energia humana"

def printar(veiculo: Veiculo):
    print('-' * 20)
    print(veiculo.mover())
    print(veiculo.tipo_combustivel())


if __name__ == "__main__":
    veiculos = [
        Carro(),
        Moto(),
        Barco(),
        Bicicleta()
    ]

    for veiculo in veiculos:
        printar(veiculo)