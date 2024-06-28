from models.options import moedas
import requests
import json

def opcoes_moedas():
    opcoes = moedas
    return opcoes

def resposta(de, para):
    url = f'https://v6.exchangerate-api.com/v6/8f5faef8a07028db76435873/pair/{de}/{para}'
    response = requests.get(url)

    if response.status_code == 200:
        dados_conversao = response.json()
        valor = dados_conversao['conversion_rate']
        return valor
    else:
        menssagem = 'Não foi possível realizar a conversão'
        return menssagem
