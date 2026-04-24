from abc import ABC, abstractmethod

class Dispositivo(ABC):

    @abstractmethod
    def ligar(self):
        pass


class TV(Dispositivo):
    def ligar(self):
        return "TV ligada"

class Radio(Dispositivo):
    def ligar(self):
        return "Rádio ligado"

class ControleRemoto:
    def __init__(self, dispositivo: Dispositivo):
        self.dispositivo = dispositivo

    def turnon(self):
        return self.dispositivo.ligar()

if __name__ == "__main__":
    # Uso
    tv = TV()
    controle = ControleRemoto(tv)

    print(controle.turnon())


    radio = Radio()
    controle = ControleRemoto(radio)

    print(controle.turnon())