# importa a biblioteca do 'FastAPI' e 'Query'
from fastapi import FastAPI, Query

# como toda a biblioteca do 'requests' sera importada, nao precisa utilizar 'from' antes
import requests

# atrui a var 'app' a classe 'FastAPI'
app = FastAPI()

# cria uma rota '/api/hello' que retorna a funcao 'hello_world()'
@app.get('/api/hello')
def hello_world():
    
    # doc string informa o que o endpoint faz
    # a documentacao pode acessada pelo '/docs' 
    '''
    DOC STRING: mensagem de hello world
    '''
    return{'hello':'world'}

# cria uma rota no servidor local que retona a lista de produtos de um restaurante a partir de outra api
@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None) ):
    # doc string informa o que o endpoint faz
    # a documentacao pode acessada pelo '/docs' 
    '''
    DOC STRING: end point que lista os itens de cada restaurante
    '''
    
    # endpoint
    url_api = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url_api)

    # caso a resposta seja sucedida
    if response.status_code == 200:
        dados_json = response.json()

        # caso nenhum parametro de nome de restaurante seja passado para o endpoint, retorna todos os dados
        if restaurante is None:
            return {'dados':dados_json}

        # variavel dicionario {key:value} que ira armazenar o nome dos restaurantes e os seus respectivos dados
        dados_restaurante = []

        # para cada item em 'dados_json', sera armazenado, de forma unica, o nome dos restaurantes juntamente com uma lista vazia
        for item in dados_json:
            
            # caso algum parametro de nome de restaurante seja passado para o endpoint, filtrada apenas ele
            if item['Company'] == restaurante:
                    
                # sera guardado os dados deles, utilizando os nomes dele como chave de acesso a todos os seus dados
                dados_restaurante.append(
                    {
                        'item': item['Item'], 
                        'preco': item['price'],
                        'descricao': item['description']
                    }
                )

        # retorna o restaurante e seus itens
        return {'restaurante':restaurante, 'itens':dados_restaurante}
    else:
        print(f'erro: {response.status_code} - {response.text}')