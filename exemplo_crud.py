import sqlite3

url_db = "meu_banco_pessoa.db"

class PessoaDAO:
    def __init__(self, caminho_arquivo="meu_banco.db"):
        self.caminho_arquivo = caminho_arquivo
        self._criar_tabela()

    def _criar_tabela(self):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100),
                idade INTEGER,
                cpf VARCHAR(11)
            )
        """)
        conn.commit()
        conn.close()

    def listar_pessoas(self) -> "PessoaModel":
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, idade, cpf FROM pessoas")
        pessoas = cursor.fetchall()
        conn.close()
        return [PessoaModel(pessoa[1], pessoa[2], pessoa[3], pessoa[0]) for pessoa in pessoas]
    
    def inserir_pessoa(self, pessoa: "PessoaModel"):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pessoas (nome, idade, cpf) VALUES (?, ?, ?)", (pessoa.nome, pessoa.idade, pessoa.cpf))
        ultimo_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return ultimo_id

    def atualizar_pessoa(self, pessoa: "PessoaModel"):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()
        cursor.execute("UPDATE pessoas SET nome = ?, idade = ?, cpf = ? WHERE id = ?", (pessoa.nome, pessoa.idade, pessoa.cpf, pessoa.id))
        conn.commit()
        conn.close()

    def remover_pessoa(self, id):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pessoas WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def buscar_pessoa(self, id):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pessoas WHERE id = ?", (id,))
        pessoa = cursor.fetchone()
        conn.close()
        return PessoaModel(pessoa[1], pessoa[2], pessoa[3], pessoa[0])


class PessoaModel:
    def __init__(self, nome, idade, cpf, id=None):
        self.id:int = id
        self.nome:str = nome
        self.idade:int = idade
        self.cpf:str = cpf

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.idade} - {self.formata_cpf()}"
    
    def limpa_cpf(self):
        return self.cpf.replace(".", "").replace("-", "")
    
    def formata_cpf(self):
        return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
    
    def pre_save(self):
        self.cpf = self.limpa_cpf()

    def salvar(self):
        self.pre_save()
        
        pessoa_dao = PessoaDAO(url_db)
        
        if self.id:
            pessoa_dao.atualizar_pessoa(self)
        else:
            self.id = pessoa_dao.inserir_pessoa(self)


# Exemplo de uso
print()
print(" Exemplo de uso ".center(50, "-"))

print("Inserindo pessoas")
pessoa1 = PessoaModel("João", 30, "123.456.789-00")
pessoa1.salvar()

pessoa2 = PessoaModel("Maria", 25, "987.654.321-00")
pessoa2.salvar()

pessoa3 = PessoaModel("Pedro", 40, "111.222.333-44")
pessoa3.salvar()


# Listar todas as pessoas
print()
print("Listando todas as pessoas")
pessoas = PessoaDAO(url_db).listar_pessoas()
for pessoa in pessoas:
    print(pessoa)

# Buscar uma pessoa
print()
print("Buscando uma pessoa")
pessoa_dao = PessoaDAO(url_db)
pessoa = pessoa_dao.buscar_pessoa(2)
print(pessoa)


# Remover uma pessoa
print()
print("Removendo uma pessoa")
pessoa_dao.remover_pessoa(2)



# Atualizar uma pessoa
print()
print("Atualizando uma pessoa")
pessoa = pessoa_dao.buscar_pessoa(3)
pessoa.idade = 35
pessoa.salvar()
print(pessoa)

# Listar todas as pessoas
print()
print("Listando todas as pessoas novamente")
pessoas = pessoa_dao.listar_pessoas()
for pessoa in pessoas:
    print(pessoa)





import sqlite3

url_db = "treinamentos.db"


# =====================================================
# CURSO
# =====================================================

class CursoDAO:
    def __init__(self, caminho_arquivo="treinamentos.db"):
        self.caminho_arquivo = caminho_arquivo
        self._criar_tabela()

    def _criar_tabela(self):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS curso (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_curso VARCHAR(110) NOT NULL,
                descricao TEXT,
                vencimento_em_mes INTEGER NOT NULL,
                alerta_dias VARCHAR(22) NOT NULL DEFAULT '60,30,15'
            )
        """)

        conn.commit()
        conn.close()

    def listar_cursos(self):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome_curso, descricao,
                   vencimento_em_mes, alerta_dias
            FROM curso
        """)

        cursos = cursor.fetchall()

        conn.close()

        return [
            CursoModel(
                curso[1],
                curso[2],
                curso[3],
                curso[4],
                curso[0]
            )
            for curso in cursos
        ]

    def inserir_curso(self, curso):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO curso
            (nome_curso, descricao,
             vencimento_em_mes, alerta_dias)
            VALUES (?, ?, ?, ?)
        """, (
            curso.nome_curso,
            curso.descricao,
            curso.vencimento_em_mes,
            curso.alerta_dias
        ))

        ultimo_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return ultimo_id

    def atualizar_curso(self, curso):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE curso
            SET nome_curso=?,
                descricao=?,
                vencimento_em_mes=?,
                alerta_dias=?
            WHERE id=?
        """, (
            curso.nome_curso,
            curso.descricao,
            curso.vencimento_em_mes,
            curso.alerta_dias,
            curso.id
        ))

        conn.commit()
        conn.close()

    def remover_curso(self, id):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM curso WHERE id=?",
            (id,)
        )

        conn.commit()
        conn.close()

    def buscar_curso(self, id):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM curso WHERE id=?",
            (id,)
        )

        curso = cursor.fetchone()

        conn.close()

        if not curso:
            return None

        return CursoModel(
            curso[1],
            curso[2],
            curso[3],
            curso[4],
            curso[0]
        )


class CursoModel:
    def __init__(
        self,
        nome_curso,
        descricao,
        vencimento_em_mes,
        alerta_dias="60,30,15",
        id=None
    ):
        self.id = id
        self.nome_curso = nome_curso
        self.descricao = descricao
        self.vencimento_em_mes = vencimento_em_mes
        self.alerta_dias = alerta_dias

    def __str__(self):
        return (
            f"{self.id} - "
            f"{self.nome_curso} - "
            f"{self.vencimento_em_mes} meses"
        )

    def salvar(self):
        curso_dao = CursoDAO(url_db)

        if self.id:
            curso_dao.atualizar_curso(self)
        else:
            self.id = curso_dao.inserir_curso(self)


# =====================================================
# TREINAMENTO
# =====================================================

class TreinamentoDAO:
    def __init__(self, caminho_arquivo="treinamentos.db"):
        self.caminho_arquivo = caminho_arquivo
        self._criar_tabela()

    def _criar_tabela(self):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS treinamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                responsavel_treinamento_colaborador INTEGER NOT NULL,
                data_realizacao DATETIME NOT NULL,
                curso_id INTEGER NOT NULL,

                FOREIGN KEY(curso_id)
                REFERENCES curso(id)
            )
        """)

        conn.commit()
        conn.close()

    def listar_treinamentos(self):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id,
                   responsavel_treinamento_colaborador,
                   data_realizacao,
                   curso_id
            FROM treinamento
        """)

        treinamentos = cursor.fetchall()

        conn.close()

        return [
            TreinamentoModel(
                treinamento[1],
                treinamento[2],
                treinamento[3],
                treinamento[0]
            )
            for treinamento in treinamentos
        ]

    def inserir_treinamento(self, treinamento):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO treinamento
            (
                responsavel_treinamento_colaborador,
                data_realizacao,
                curso_id
            )
            VALUES (?, ?, ?)
        """, (
            treinamento.responsavel_treinamento_colaborador,
            treinamento.data_realizacao,
            treinamento.curso_id
        ))

        ultimo_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return ultimo_id

    def atualizar_treinamento(self, treinamento):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE treinamento
            SET responsavel_treinamento_colaborador=?,
                data_realizacao=?,
                curso_id=?
            WHERE id=?
        """, (
            treinamento.responsavel_treinamento_colaborador,
            treinamento.data_realizacao,
            treinamento.curso_id,
            treinamento.id
        ))

        conn.commit()
        conn.close()

    def remover_treinamento(self, id):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM treinamento WHERE id=?",
            (id,)
        )

        conn.commit()
        conn.close()

    def buscar_treinamento(self, id):
        conn = sqlite3.connect(self.caminho_arquivo)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM treinamento WHERE id=?",
            (id,)
        )

        treinamento = cursor.fetchone()

        conn.close()

        if not treinamento:
            return None

        return TreinamentoModel(
            treinamento[1],
            treinamento[2],
            treinamento[3],
            treinamento[0]
        )


class TreinamentoModel:
    def __init__(
        self,
        responsavel_treinamento_colaborador,
        data_realizacao,
        curso_id,
        id=None
    ):
        self.id = id
        self.responsavel_treinamento_colaborador = responsavel_treinamento_colaborador
        self.data_realizacao = data_realizacao
        self.curso_id = curso_id

    def __str__(self):
        return (
            f"{self.id} - "
            f"Curso ID: {self.curso_id} - "
            f"Data: {self.data_realizacao}"
        )

    def salvar(self):
        treinamento_dao = TreinamentoDAO(url_db)

        if self.id:
            treinamento_dao.atualizar_treinamento(self)
        else:
            self.id = treinamento_dao.inserir_treinamento(self)


# =====================================================
# EXEMPLO DE USO
# =====================================================

print()
print(" Curso ".center(50, "-"))

curso = CursoModel(
    "NR-35",
    "Trabalho em altura",
    24,
    "60,30,15"
)

curso.salvar()

print(curso)

print()
print(" Treinamento ".center(50, "-"))

treinamento = TreinamentoModel(
    responsavel_treinamento_colaborador=1,
    data_realizacao="2026-06-16 20:00:00",
    curso_id=curso.id
)

treinamento.salvar()

print(treinamento)

print()
print(" Listando cursos ".center(50, "-"))

for curso in CursoDAO(url_db).listar_cursos():
    print(curso)

print()
print(" Listando treinamentos ".center(50, "-"))

for treinamento in TreinamentoDAO(url_db).listar_treinamentos():
    print(treinamento)