from flask import Flask, render_template, request
from utils import extrair_dados
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

dados_pdf = extrair_dados("uploads/682_ebserh-administrativo-resultado-final-de-aprovados-2025-06-13.pdf")

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    if request.method == "POST":
        query = request.form.get("busca").lower()
        resultados = [
            d for d in dados_pdf
            if query in d["nome"].lower() or query in d["inscricao"]
        ]
    return render_template("index.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)
