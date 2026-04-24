from singleton import ConexaoBanco
import designers_patterns.exemplo_singleton.configs as configs

conexao = ConexaoBanco({"qualquercoisa": "qualquercoisa"})

conexao.conectar()
conexao.executar_query("SELECT * FROM clientes")
conexao.desconectar()
print(conexao.configs)

print(id(conexao))
print(id(configs.conexao))
print(conexao is configs.conexao)