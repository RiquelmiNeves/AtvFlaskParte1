#página usuario.html dinâmica
from flask import Flask, render_template

app_rick = Flask(__name__ , template_folder='templates')
#cria o objeto da aplicação

@app_rick.route("/")  #rota para solicitação web
def homepage():          #função
    return render_template ("homepage.html")

@app_rick.route("/contato")
def contato():
    return render_template("contato.html") 

@app_rick.route("/usuario")
def dados_usuario():
    #nome_usuario="Riquelmi"
    dados_usu = {"nome": "Riquelmi", "profissao": "Estagiario", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", dados = dados_usu)
                                           #parâmetro recebe argumento
                                           #colocar o site no ar

if __name__ == "__main__": 
     app_rick.run(port = 8000)