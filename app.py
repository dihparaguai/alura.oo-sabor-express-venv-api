# como toda a biblioteca sera importada, nao precisa utilizar 'from'
import requests

import json

# endpoint
url_api = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

# solicita o dados para o endpoint utilizando o 'requests' utilizando os verbos http
response = requests.get(url_api)
print(response)
print(response.json())


# se a resposta http for positiva, entao os dados da api serao printados no terminal
if response.status_code == 200:
    dados_json = response.json()

    # variavel dicionario {key:value} que ira armazenar o nome dos restaurantes e os seus respectivos dados
    dados_restaurante = {}

    # para cada item em 'dados_json', sera armazenado, de forma unica, o nome dos restaurantes juntamente com uma lista vazia
    for item in dados_json:
        
        # todo os nomes de restaurante estao sendo passados para a var 'nome_restaurante'
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            
            # nome de cada restaurante com uma lista vazia
            dados_restaurante[nome_restaurante] = []
        
        # depois de criado os restaurantes, sera guardado os dados deles, utilizando os nomes dele scomo chave de acesso a todos os seus dados
        dados_restaurante[nome_restaurante].append(
            {
                'item': item['Item'], 
                'preco': item['price'],
                'descricao': item['description']
            }
        )
else:
    print(f'erro: {response.status_code}')


# itera sobre os dados do dicionario do restaurante e cria arquivos json de cada restaurante com os dados respectivos deles
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
else:
    print(f'erro: {response.status_code}')
