from abc import ABC, abstractmethod

class Relatorio(ABC):

    def gerar(self):
        self.cabecalho()
        self.corpo()
        self.rodape()

    def cabecalho(self):
        print("Cabeçalho padrão")

    @abstractmethod
    def corpo(self):
        pass

    def rodape(self):
        print("Rodapé padrão")


class RelatorioPDF(Relatorio):
    def corpo(self):
        print("Conteúdo em PDF")

if __name__ == "__main__":
    # Uso
    rel = RelatorioPDF()
    rel.gerar()