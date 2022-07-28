from flask import Flask, render_template, request, redirect, session, flash, url_for
import jogos, usuarios

jogoum = jogos.Jogos("Tetris", "Quebra-Cabeça", "Atari")
jogodois = jogos.Jogos("House Flipper", "Simulador", "PC/Celular")
jogotres = jogos.Jogos("It Is Take Two", "Ação-Aventura", "PC/PlayStation/Xbox")
lista = [jogoum, jogodois, jogotres]

app = Flask(__name__)
app.secret_key = "comida"

usuarioUm = usuarios.Usuarios("Leticia Americano", "LA", "doritos")
usuarioDois = usuarios.Usuarios("Marcos Cury", "MC", "cocacola")
usuarioTres = usuarios.Usuarios("Maria Eduarda", "ME", "steave")
usuarios = {usuarioUm.nickname: usuarioUm, usuarioDois.nickname : usuarioDois, usuarioTres.nickname : usuarioTres}

@app.route("/")
def index():
    return render_template("lista.html", titulo="JOGOTECA", jogos=lista)


@app.route("/novo")
def novo():
    if "usuario_logado" not in session or session["usuario_logado"] is None:
        return redirect(url_for("login", proxima=url_for("novo")))
    return render_template("novo.html", titulo="NOVO JOGO")


@app.route("/criar", methods=["POST",])
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    jogo = jogos.Jogos(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for("index"))


@app.route("/login")
def login():
    proxima = request.args.get("proxima")
    return render_template("login.html", proxima=proxima)


@app.route("/logout")
def logout():
    session["usuario_logado"] = None
    flash("Logout efetuado com sucesso")
    return redirect(url_for("index"))


@app.route("/autenticar", methods=["POST", ])
def autenticar():

    if request.form["usuario"] in usuarios:
        usuario = request.form["usuario"]
        if request.form["senha"] == usuarios[usuario].senha:
            session["usuario_logado"] = usuario.nickname
            flash(usuario.nickname + " logado(a) com sucesso!")
            proxima_pagina = request.form["proxima"]
            return redirect(proxima_pagina)
    else:
        flash("Usuário não logado.")
        return redirect(url_for("login"))


app.run(debug=True)
