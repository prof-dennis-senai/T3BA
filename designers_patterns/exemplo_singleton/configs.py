from singleton import ConexaoBanco

conexao = ConexaoBanco({"host": "localhost", "porta": 3306})

conexao.conectar()
conexao.executar_query("SELECT * FROM clientes")
conexao.desconectar()