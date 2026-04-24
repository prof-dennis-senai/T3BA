class ConexaoBanco:
    _instancia = None
    _inicializado = False

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            print("Criando conexão com o banco...")
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, configs={}):
        # Evita reinicializar toda vez
        if self._inicializado:
            return

        print("Inicializando conexão...")
        self.conectado = False
        self.configs = configs
        self._inicializado = True

    def conectar(self):
        print("Conectando ao banco...")
        self.conectado = True

    def executar_query(self, sql):
        print(f"Executando: {sql}")

    def desconectar(self):
        print("Desconectando...")
        self.conectado = False


if __name__ == "__main__":
    obj1 = ConexaoBanco({"host": "localhost", "porta": 3306})
    obj2 = ConexaoBanco()
    obj3 = ConexaoBanco()

    print(obj1 is obj2 is obj3)