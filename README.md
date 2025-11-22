# Sistema de Metas - Venttos Electronics

Sistema de gerenciamento de metas de produção desenvolvido em **Python + Flask**.  
Permite cadastrar modelos, calcular metas ajustadas por pessoas e calcular perdas de produção.

---

## 🔹 Funcionalidades

- Dashboard com resumo de modelos cadastrados, média de meta/hora e último cadastro.
- Cadastro de modelos (código, cliente, setor, meta/hora, pessoas padrão).
- Listagem de modelos com DataTables.
- Edição e exclusão de modelos.
- Cálculo de meta ajustada por pessoas e tempo.
- Cálculo de perda de produção.
- Layout responsivo com **Bootstrap 5**.

---

## 🔹 Tecnologias

- Python 3.11+
- Flask 2.3+
- SQLite (banco de dados local)
- HTML5, CSS3, Bootstrap 5
- DataTables (via CDN)
- JavaScript (Fetch API + AJAX)

---

## 🔹 Estrutura do projeto

```
Sistema de Metas - Venttos/
├─ static/
│   ├─ logo.png 
│       ├─ css/
│            └─ style.css  
│       ├─ js/
│            └─ main.js  
├─ templates/
│  ├─ base.html
│  ├─ cadastro.html
│  ├─ dashboard.html
│  ├─ modelos.html
│  ├─ calcular.html
│  ├─ perdas.html
├─ app.py
├─ producao.db
├─ ping.py
├─ Profile   
├─ README.md   
├─ requirements.txt 
```
---

## 📁 Como Rodar

```bash
pip install -r requirements.txt
python app.py
```

---

## 👨‍💻 Autor

* Desenvolvido por **Eduardo Libório**
* 📧 [eduardosoleno@protonmail.com](mailto:eduardosoleno@protonmail.com)

---

