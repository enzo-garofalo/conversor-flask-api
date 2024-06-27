import requests
import json

def opcoes_moedas():
    url = 'https://economia.awesomeapi.com.br/json/available/uniq'
    response = requests.get(url)

    if response.status_code == 200:
        opcoes_json = response.json()
        return opcoes_json
    else:
        print(f'Erro {response.status_code}-{response.text}')

def resposta(de, para):
    url = f'https://economia.awesomeapi.com.br/last/{de}-{para}'
    response = requests.get(url)

    if response.status_code == 200:
        dados_conversao = response.json()
        valor = dados_conversao[f'{de}{para}']['bid']
        return valor

    else:
        print(f'Erro {response.status_code}-{response.text}')

