class SistemaPagamento:
    def pagar(self):
        return "Pagamento realizado"


class SistemaEnvio:
    def enviar(self):
        return "Produto enviado"
    
class SistemaEmail:
    def enviar_email(self):
        return "Email enviado"


class LojaFacade:
    def __init__(self):
        self.pagamento = SistemaPagamento()
        self.envio = SistemaEnvio()
        self.email = SistemaEmail()

    def finalizar_compra(self):
        return f"{self.pagamento.pagar()} + {self.envio.enviar()} + {self.email.enviar_email()}"

if __name__ == "__main__":
    # Uso
    loja = LojaFacade()
    print(loja.finalizar_compra())