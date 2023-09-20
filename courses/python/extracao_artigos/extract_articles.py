# instalando bibliotecas

# pip install newspaper3k

# Importando bibliotecas
from newspaper import Article


# Recebendo url artigo
url = 'https://www.tecmundo.com.br/mercado/271422-python-linguagem-tao-usada-data-science-financas.htm'

# Definindo classe artigo para variável
artigo = Article(url)

artigo.download() # Baixa o artigo
artigo.parse() # Raspa o site, buscando artigo
artigo.nlp() # Separa o sumário & Palavras Chaves

titulo = artigo.title # Recebe o conteúdo do Titulo

conteudo_texto = artigo.summary # Recebe o conteúdo do Sumário