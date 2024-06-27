from main import app
from flask import render_template, request
from models.api import opcoes_json


@app.route('/')
def index():
    return render_template('index.html', page_title='Conversor de Moedas', opcoes_json=opcoes_json)

@app.route('/conversor', methods=['POST',])
def conversor():
    pass