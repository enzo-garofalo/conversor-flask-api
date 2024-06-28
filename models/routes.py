from models.options import moedas
from main import app
from flask import render_template, request
from models.api import opcoes_moedas, resposta


@app.route('/')
def index():
    opcoes_json = opcoes_moedas()
    return render_template('index.html', page_title='Conversor de Moedas', opcoes=moedas)

@app.route('/conversor', methods=['POST',])
def conversor():
    de = request.form['converter']
    para = request.form['para']
    valor = resposta(de, para)
    return render_template('resultado.html', page_title='Resultado', valor=valor, de=de, para=para, opcoes=moedas)