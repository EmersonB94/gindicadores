from flask import Flask, render_template

app = Flask(__name__)

# --- Página inicial ---
@app.route("/")
def home():
    return render_template("index.html")


# --- Rotas dos serviços ---
@app.route("/FinanceiroPessoal")
def financeiro_pessoal():
    return render_template("financeiro_pessoal_login.html")

@app.route("/FinanceiroPJ")
def financeiro_pj():
    return render_template("financeiro_pj_login.html")

@app.route("/Estoque")
def estoque():
    return render_template("estoque_login.html")

@app.route("/RDO")
def rdo():
    return render_template("rdo_login.html")


# --- Iniciar localmente ---
if __name__ == "__main__":
    app.run(debug=True)
