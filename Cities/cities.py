import json
import requests

url_base_ibge = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}/municipios"

estados = {
    1: "AC",
    2: "AL",
    3: "AP",
    4: "AM",
    5: "BA",
    6: "CE",
    7: "DF",
    8: "ES",
    9: "GO",
    10: "MA",
    11: "MT",
    12: "MS",
    13: "MG",
    14: "PA",
    15: "PB",
    16: "PR",
    17: "PE",
    18: "PI",
    19: "RJ",
    20: "RN",
    21: "RS",
    22: "RO",
    23: "RR",
    24: "SC",
    25: "SP",
    26: "SE",
    27: "TO"
}

cities_json = []

# Iterar sobre os estados
for estado_id, estado_sigla in estados.items():
    # Fazer a chamada à API do IBGE para obter as cidades do estado
    url_ibge = url_base_ibge.format(estado_sigla)
    response_ibge = requests.get(url_ibge)
    
    if response_ibge.status_code == 200:
        data_ibge = response_ibge.json()
        
        # Processar os dados das cidades do estado
        for city in data_ibge:
            city_json = {
                "model": "constant_tables.city",
                "fields": {
                    "name": city["nome"],
                    "state": estado_id
                }
            }
            cities_json.append(city_json)
    else:
        print("Erro ao fazer a solicitação do IBGE:", response_ibge.status_code)

# Salvar os objetos city_json em um arquivo JSON separado
with open('cities.json', 'w', encoding='utf-8') as file:
    json.dump(cities_json, file, ensure_ascii=False, indent=4)
