# SMT Production Manager

**SMT Production Manager** é um sistema web desenvolvido para **engenharia e produção SMT**, com foco em **padronização de dados**, **cálculos de performance** e **apoio à definição de metas de produção**.

---

## 🎯 Finalidade

* Cadastro de modelos SMT
* Base de dados por modelo e fase
* Definição de meta por hora
* Quantidade por blank
* Tempo padrão de montagem
* Consulta rápida de metas já definidas

---

## 📊 Página de Cálculos

O sistema conta com uma página dedicada a cálculos produtivos, incluindo:

* ⏱️ Tempo para produzir **X unidades** (resultado em `hh:mm:ss`)
* ⚙️ Cálculo do **tempo de montagem da máquina** (checagem de meta)
* 🎯 Automação do cálculo de **meta por hora**
* 🛠️ Ferramenta de **análise manual** (start / stop)
* 📉 Cálculo de **perda de produção**
* 📐 Cálculo automático de **meta por hora × minutos**, considerando fator blank

---

## 📱 Plataforma

* Desktop e mobile
* Versão mobile com layout estilo **app nativo**

---

## ☁️ Infraestrutura

* Servidor em Cloud (**Railway**)
* Sistema sempre online

---

## 🔹 Estrutura do Projeto

```text
project/
├─ app/
│   ├─ __init__.py            # create_app()
│   ├─ config.py              # Configurações / env
│   ├─ extensions.py          # DB (psycopg, etc)
│   │
│   ├─ routes/
│   │   ├─ __init__.py        # Registro de blueprints
│   │   ├─ pages.py           # Rotas HTML
│   │   └─ api.py             # Rotas REST (JSON)
│   │
│   ├─ services/              # Regras de negócio
│   │   ├─ __init__.py
│   │   ├─ modelos_service.py
│   │   └─ pcp_service.py
│   │
│   ├─ repositories/          # Acesso ao banco de dados
│   │   ├─ __init__.py
│   │   └─ modelos_repository.py
│   │
│   ├─ templates/             # Jinja2
│   │   ├─ base.html
│   │   ├─ cadastro.html
│   │   ├─ calcular.html
│   │   ├─ dashboard.html
│   │   └─ modelos.html
│   │
│   └─ static/
│       ├─ css/
│       │   └─ style.css
│       ├─ js/
│       │   ├─ main.js
│       │   └─ pcp.js
│       ├─ images/
│       └─ fonts/
│           └─ inter.woff2
│
├─ migrations/                # Alembic / Flask-Migrate
├─ tests/                     # pytest
├─ run.py                     # Entrypoint
├─ requirements.txt
├─ Procfile                   # Railway
├─ README.md
├─ .env                       # NÃO versionar
├─ .gitignore
└─ pyproject.toml
```

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Flask
* Jinja2
* HTML5 / CSS3
* JavaScript (Vanilla)
* PostgreSQL
* Bootstrap 5
* Railway

---

## ▶️ Como Rodar o Projeto Localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/venttos-factory-metrics.git
cd venttos-factory-metrics
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux / Mac
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz:

```env
FLASK_ENV=development
SECRET_KEY=supersecretkey
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### 5️⃣ Executar a aplicação

```bash
python run.py
```

Acesse:

```
http://127.0.0.1:5000
```

---

## 📌 Observações

* Não possui autenticação (por enquanto)
* Foco em uso interno / industrial
* Estrutura pronta para escalar
* Código organizado para fácil manutenção

---

## 🚀 Deploy

* Deploy contínuo via **Railway**
* Uso de `Procfile`
* Banco PostgreSQL gerenciado

---

## 👨‍💻 Autor

Desenvolvido por **Eduardo Libório**

📧 [eduardosoleno@protonmail.com](mailto:eduardosoleno@protonmail.com)

---

## 📄 Licença

Projeto de uso privado / interno.
