import requests
import json
from datetime import datetime
import pytz
def conexao_Arduino():
    url = "http://46.17.108.113:1026/v2/entities/urn:ngsi-ld:illtracker:001/attrs"

    payload = {}
    headers = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/',
    'accept': 'application/json'
    }

    responseheartrate = requests.request("GET", url + "/heartrate", headers=headers, data=payload)
    responseTemperature = requests.request("GET", url + "/temperature", headers=headers, data=payload)


    if responseheartrate.status_code == 200 and responseTemperature.status_code == 200:
        # Converte a resposta JSON para um dicionário Python
        dataHeartrate = responseheartrate.json()
        dataTemperature = responseTemperature.json()


        #### Armazena o valor do batimento cardiaco
        heartrate = dataHeartrate.get("value")
        
        #### Armazena o valor da temperatura
        temperature = dataTemperature.get("value")


        ### Armazena o valor da data e hora da última checagem ####
        timeInstant = dataTemperature.get("metadata",{}).get("TimeInstant",{}).get("value")
        
        # Converte a string para um objeto datetime
        data = datetime.strptime(timeInstant, "%Y-%m-%dT%H:%M:%S.%fZ")

        # Formata o objeto datetime para um formato mais legível
        dataFormatada = data.strftime('%d/%m/%Y %H:%M:%S')
        data = pytz.utc.localize(data).astimezone(pytz.timezone('America/Sao_Paulo'))
        dataFormatada = data.strftime('%d/%m/%Y %H:%M:%S')
        try:
            with open('db.json', 'r', encoding='utf-8') as f:
                content = f.read()
                if not content:  # Verifica se o conteúdo do arquivo está vazio
                    illTracker = {'illTracker':[]}
                else:
                    f.seek(0)  # Volta para o início do arquivo
                    illTracker = json.load(f)
        
        except FileNotFoundError:
            illTracker = {'illTracker':[]}

        dadosSensor = {
            'id': 1,
            'heartrate': heartrate,
            'temperature': temperature,
            'dataHora': dataFormatada,
        }

        # armazena os dados recebidos do sensor
        illTracker['illTracker'] = dadosSensor

        #envia os dados para o db.json
        with open('db.json', 'w', encoding='utf-8') as f:
            json.dump(illTracker, f, indent = 4, ensure_ascii=False)
        
        #Retorna os valores de distância, peso e data
    else:
        print("Erro na solicitação:", responseTemperature.status_code)
        print("Erro na solicitação:", responseheartrate.status_code)

