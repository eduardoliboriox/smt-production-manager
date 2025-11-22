from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB = "producao.db"

os.environ["NO_PROXY"] = "127.0.0.1,localhost"

# ---------------------------
# BANCO DE DADOS
# ---------------------------
def inicializar_bd():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS modelos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE,
            cliente TEXT,
            setor TEXT,
            meta_padrao REAL,
            pessoas_padrao INTEGER
        )
    """)
    conn.commit()
    conn.close()

inicializar_bd()

def carregar_codigos():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT codigo FROM modelos ORDER BY codigo")
    codigos = [r[0] for r in cur.fetchall()]
    conn.close()
    return codigos

# ---------------------------
# PÁGINAS DO SISTEMA (LAYOUT B)
# ---------------------------
@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html", codigos=carregar_codigos())

@app.route("/modelos")
def modelos():
    return render_template("modelos.html", codigos=carregar_codigos())

@app.route("/calculo")
def calculo():
    return render_template("calcular.html", codigos=carregar_codigos())

@app.route("/perdas")
def perdas():
    return render_template("perdas.html")

# ---------------------------
# FUNÇÕES DO SISTEMA
# ---------------------------
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    codigo = request.form["codigo"]
    cliente = request.form["cliente"]
    setor = request.form["setor"]
    meta = request.form["meta"]
    pessoas = request.form["pessoas"]

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO modelos (codigo, cliente, setor, meta_padrao, pessoas_padrao)
            VALUES (?, ?, ?, ?, ?)
        """, (codigo, cliente, setor, meta, pessoas))
        conn.commit()
        msg = f"Modelo {codigo} cadastrado!"
        sucesso = True
    except sqlite3.IntegrityError:
        msg = "Código já existe!"
        sucesso = False
    finally:
        conn.close()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({"mensagem": msg, "sucesso": sucesso})

    return render_template("cadastro.html", codigos=carregar_codigos(), mensagem=msg)

@app.route("/editar", methods=["POST"])
def editar():
    codigo = request.form["codigo"]
    nova_meta = request.form.get("nova_meta")
    novas_pessoas = request.form.get("novas_pessoas")

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT id FROM modelos WHERE codigo = ?", (codigo,))
    r = cur.fetchone()

    if not r:
        conn.close()
        return render_template("modelos.html",
                               codigos=carregar_codigos(),
                               mensagem="Modelo não encontrado!")

    if nova_meta:
        cur.execute("UPDATE modelos SET meta_padrao = ? WHERE codigo = ?", (nova_meta, codigo))

    if novas_pessoas:
        cur.execute("UPDATE modelos SET pessoas_padrao = ? WHERE codigo = ?", (novas_pessoas, codigo))

    conn.commit()
    conn.close()

    return render_template("modelos.html", codigos=carregar_codigos(),
                           mensagem=f"Modelo {codigo} atualizado!")

@app.route("/excluir", methods=["POST"])
def excluir():
    codigo = request.form["codigo"]
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DELETE FROM modelos WHERE codigo = ?", (codigo,))
    conn.commit()
    conn.close()

    return render_template("modelos.html", codigos=carregar_codigos(),
                           mensagem=f"Modelo {codigo} excluído!")

@app.route("/listar")
def listar():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT codigo, cliente, setor, meta_padrao, pessoas_padrao FROM modelos")
    dados = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify({"data": dados})  # chave "data" é obrigatória para o DataTables

@app.route("/calcular_meta", methods=["POST"])
def calcular_meta():
    codigo = request.form["codigo"]
    pessoas_atuais = int(request.form["pessoas_atuais"])
    minutos = int(request.form["minutos"])

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT meta_padrao, pessoas_padrao FROM modelos WHERE codigo = ?", (codigo,))
    r = cur.fetchone()
    conn.close()

    if not r:
        return jsonify({"resultado": "Modelo não encontrado!"})

    meta_padrao, pessoas_padrao = r

    meta_ajustada = round(meta_padrao * (pessoas_atuais / pessoas_padrao) * 0.85) \
                     if pessoas_atuais != pessoas_padrao else round(meta_padrao)

    qtd_minutos = round(meta_ajustada * (minutos / 60))

    return jsonify({
        "resultado": f"Meta ajustada: {meta_ajustada} peças/hora<br>"
                     f"{minutos} min → {qtd_minutos} peças"
    })

@app.route("/calcular_perda", methods=["POST"])
def calcular_perda():
    meta_hora = float(request.form["meta_hora"])
    producao_real = float(request.form["producao_real"])

    perda = meta_hora - producao_real

    if perda > 0:
        frac_hora = perda / meta_hora
        minutos = int(frac_hora * 60)
        segundos = int((frac_hora * 60 - minutos) * 60)
        resultado = f"{perda:.0f} peças → {minutos:02d}min {segundos:02d}s perdidos"
    else:
        resultado = "Sem perda"

    return jsonify({"resultado": resultado})

# ---------------------------
# INICIAR SERVIDOR
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
