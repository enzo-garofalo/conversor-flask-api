from main import app
from flask import render_template
from Routes.api import opcoes_json


@app.route('/')
def index():
    return render_template('index.html', page_title='Bem vindo', opcoes_json=opcoes_json)

@app.route('/conversor', methods=['POST',])
def conversor():
    pass