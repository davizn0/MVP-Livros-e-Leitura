from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "123456"

# conecta no banco de dados (cria o arquivo se ainda nao existir)
conexao = sqlite3.connect("livros.db", check_same_thread=False)
cursor = conexao.cursor()

# cria as tabelas, se ainda nao existirem
cursor.execute("""
CREATE TABLE IF NOT EXISTS voluntario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    senha TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    categoria TEXT,
    quantidade_desejada INTEGER,
    quantidade_atendida INTEGER
)
""")
conexao.commit()

# cria a voluntaria de teste, se ainda nao existir
cursor.execute("SELECT * FROM voluntario WHERE email = 'voluntaria@ongleituras.org'")
resultado = cursor.fetchone()
if resultado == None:
    cursor.execute(
        "INSERT INTO voluntario (email, senha) VALUES (?, ?)",
        ("voluntaria@ongleituras.org", "minhasenha123"),
    )
    conexao.commit()


@app.route("/")
def pagina_inicial():
    cursor.execute("SELECT * FROM item")
    itens = cursor.fetchall()
    return render_template("listagem.html", itens=itens, logado=session.get("logado"))


@app.route("/login", methods=["GET", "POST"])
def login():
    mensagem_erro = ""
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        cursor.execute("SELECT * FROM voluntario WHERE email = ? AND senha = ?", (email, senha))
        usuario = cursor.fetchone()
        if usuario != None:
            session["logado"] = True
            return redirect("/cadastro")
        else:
            mensagem_erro = "E-mail ou senha incorretos."
    return render_template("login.html", erro=mensagem_erro)


@app.route("/logout")
def logout():
    session["logado"] = False
    return redirect("/")


@app.route("/cadastro")
def cadastro():
    if session.get("logado") != True:
        return redirect("/login")
    cursor.execute("SELECT * FROM item")
    itens = cursor.fetchall()
    return render_template("cadastro.html", itens=itens)


@app.route("/novo_item", methods=["POST"])
def novo_item():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    quantidade = request.form["quantidade"]
    cursor.execute(
        "INSERT INTO item (nome, categoria, quantidade_desejada, quantidade_atendida) VALUES (?, ?, ?, 0)",
        (nome, categoria, quantidade),
    )
    conexao.commit()
    return redirect("/cadastro")


@app.route("/nova_doacao", methods=["POST"])
def nova_doacao():
    item_id = request.form["item_id"]
    quantidade = request.form["quantidade"]
    cursor.execute("SELECT quantidade_atendida FROM item WHERE id = ?", (item_id,))
    atual = cursor.fetchone()[0]
    nova_quantidade = atual + int(quantidade)
    cursor.execute("UPDATE item SET quantidade_atendida = ? WHERE id = ?", (nova_quantidade, item_id))
    conexao.commit()
    return redirect("/cadastro")


if __name__ == "__main__":
    app.run(debug=True)