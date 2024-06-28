from temp import dic
import json

exemplo = [['AED', 'UAE Dirham'],["FJD","Fiji Dollar"]]
moedas = {}

for tuplas in dic.values():
  for valor in tuplas:
    moedas[valor[0]] = valor[1]


with open('options.json', 'w') as file:
    json.dump(moedas, file, indent=4)

