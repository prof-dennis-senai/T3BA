from abc import ABC, abstractmethod
from enum import Enum

class TipoEventoEnum(Enum):
    PEDIDO_CRIADO = "pedido_criado"
    PEDIDO_CANCELADO = "pedido_cancelado"
    PEDIDO_ATUALIZADO = "pedido_atualizado"
    PEDIDO_ENTREGUE = "pedido_entregue"


# Observador
class Listener(ABC):

    @abstractmethod
    def atualizar(self, evento: TipoEventoEnum, dados):
        pass


# Observadores concretos
class EmailService(Listener):
    def atualizar(self, evento, dados):
        if evento == TipoEventoEnum.PEDIDO_CRIADO:
            print(f"Email enviado para {dados['cliente']}")


class EstoqueService(Listener):
    def atualizar(self, evento, dados):
        if evento == TipoEventoEnum.PEDIDO_CRIADO:
            print("Estoque atualizado")


class LogService(Listener):
    def atualizar(self, evento, dados):
        print(f"[LOG] Evento: {evento.value}, Dados: {dados}")


# Dispatcher (sujeito)
class EventBus:
    def __init__(self):
        self.listeners:list[Listener] = []

    def registrar(self, listener: Listener):
        self.listeners.append(listener)

    def emitir(self, evento: TipoEventoEnum, dados):
        for l in self.listeners:
            l.atualizar(evento, dados)

if __name__ == "__main__":
    # Uso
    bus = EventBus()

    bus.registrar(EmailService())
    bus.registrar(EstoqueService())
    bus.registrar(LogService())

    bus.emitir(TipoEventoEnum.PEDIDO_CRIADO, {"cliente": "Dennis"})