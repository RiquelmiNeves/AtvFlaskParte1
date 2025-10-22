from flask import Flask

app_rick = Flask (__name__)

@app_rick.route('/')
def raiz():
    return 'Olá, turma!'

app_rick.run()
