# 'pip install requests' # Instalando a biblioteca

# Importando Bibliotecas
import requests

# Definindo Url da API Que Será Consumida
url = 'https://www.googleapis.com/books/v1/volumes?q=teste'

# Consumindo API
resposta = requests.get(url)

# Verificando Status da Requisição
print(resposta.status_code) # 200

# Verificando o conteúdo da resposta em json
print(resposta.json())