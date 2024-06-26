import requests
import json

url = 'https://economia.awesomeapi.com.br/json/available/uniq'
response = requests.get(url)


if response.status_code == 200:
    opcoes_json = response.json()
else:
    print(f' Moeda não encontrada')  