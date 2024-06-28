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
    url = f'https://v6.exchangerate-api.com/v6/8f5faef8a07028db76435873/pair/{de}/{para}'
    response = requests.get(url)

    if response.status_code == 200:
        dados_conversao = response.json()
        # print(dados_conversao)
        valor = dados_conversao['conversion_rate']
        print(valor)


        
        return valor
    else:
        menssagem = 'Não foi possível realizar a conversão'
        return menssagem

resposta('DOGE', 'BOB')