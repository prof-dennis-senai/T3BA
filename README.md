# 🏭 SafeIndustry – Sistema Integrado de Gestão de Segurança do Trabalho

## 📖 Sobre o Projeto

Este projeto tem como objetivo desenvolver um sistema web para gerenciamento de treinamentos obrigatórios (NRs), atendendo às necessidades de uma indústria do setor têxtil.

O sistema permitirá:

- Gerenciamento de Empresas
- Gerenciamento de Colaboradores
- Gerenciamento de Treinamentos obrigatórios
- Controle de Certificados e Validades
- Emissão de Relatórios
- Identificação automática de treinamentos vencidos ou a vencer

O projeto foi desenvolvido como parte das atividades práticas do curso técnico do SENAI, contemplando modelagem, banco de dados, desenvolvimento e testes automatizados.

---

## 🎯 Objetivo do Sistema

Automatizar o controle de validade de treinamentos obrigatórios, garantindo:

- Conformidade com normas regulamentadoras (NRs)
- Redução de falhas em auditorias
- Melhor controle gerencial
- Alertas de vencimento

---

## 🛠 Tecnologias Utilizadas

- Python 3.12+
- Django
- SQLite (ambiente de desenvolvimento)
- Pytest / Django Test
- Coverage

---

## 📂 Estrutura do Projeto

```

.
├── docs/
│   ├── requisitos_funcionais.md
│   ├── requisitos_nao_funcionais.md
│   ├── regras_negocio.md
│   └── modelagem/
│       ├── entidades_atributos.md
│       ├── relacionamentos.md
│       ├── normalizacao.md
│       └── der/
│           ├── der.drawio
│           └── der.png
│
├── SafeIndustry/
│   ├── manage.py
│   ├── SafeIndustry/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── empresas/
│   ├── colaboradores/
│   ├── treinamentos/
│   └── certificados/
│
├── requirements.txt
├── .gitignore
└── README.md

```

---

# 🚀 Como Executar o Projeto

## 🔹 1. Clonar o Repositório

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```

---

## 🔹 2. Criar Ambiente Virtual

### 🪟 Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 🐧 Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 🔹 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## 🔹 4. Acessar a Pasta do Projeto Django

```bash
cd SafeIndustry
```

---

## 🔹 5. Aplicar as Migrations

```bash
python manage.py migrate
```

---

## 🔹 6. Criar Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

---

## 🔹 7. Executar o Servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

# 🧪 Executando os Testes

```bash
pytest --cov=.
```

ou

```bash
python manage.py test
```

Cobertura mínima exigida:

> ✔ 95% ou superior

---

# 📌 Fluxo de Contribuição

1. Fazer fork do projeto
2. Criar branch baseada na issue
3. Desenvolver a funcionalidade
4. Implementar testes
5. Garantir cobertura > 95%
6. Abrir Pull Request referenciando a issue

Exemplo de commit:

```
feat: implementa gerenciamento de empresas (#12)
```

---

# 👨‍💻 Contribuidores

* [dennis-rocha](https://github.com/dennis-rocha) - Planejamento e Gerenciamento do Projeto.

> Exemplo:
> 
> * [João Silva](https://github.com/joaosilva) - Implementação do CRUD de Empresas
> * [Maria Souza](https://github.com/mariasouza) - Implementação dos Testes de Integração
> * [Carlos Lima](https://github.com/carloslima) - Desenvolvimento do DER e Modelagem do Banco

---

# 🎓 Projeto Acadêmico – Desafio Empresarial

Este projeto foi desenvolvido pelos estudantes do Curso Técnico de Desenvolvimento de Sistemas do SENAI, a partir de um desafio baseado em uma situação real enfrentada por uma empresa do setor industrial.

O desafio consistiu em analisar um problema real relacionado ao controle de treinamentos obrigatórios (NRs) e propor uma solução tecnológica capaz de:

- Automatizar processos manuais;
- Reduzir não conformidades em auditorias;
- Melhorar a rastreabilidade de certificados;
- Garantir maior confiabilidade das informações.

Durante o desenvolvimento, foram aplicados conhecimentos técnicos relacionados a:

- Modelagem de Sistemas;
- Banco de Dados e Normalização;
- Desenvolvimento Web com Django;
- Implementação de Testes Automatizados;
- Boas Práticas de Versionamento e Controle de Código.

O projeto simula um cenário corporativo real, integrando análise, modelagem, desenvolvimento e validação de software.

