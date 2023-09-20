# instalando bibliotecas

# pip install -U textblob
# python -m textblob.download_corpora

# Importando bibliotecas
from textblob import TextBlob

# Atribuindo Objeto da classe TextBlob para variável

texto = TextBlob("I love coding in python") # OBS: Texto somente em Inglês

# Retirando Sentimento de -1 a 1

#  ------------ Tabela Sentimento ------------
# Muito Negativo  --  Neutro  --    Muito Positivo
#     -1          <<    0    >>           1

sentimento_texto = texto.sentiment.polarity # Calcula sentimento

if sentimento_texto < 0:
    print("Negativo")
elif sentimento_texto == 0:
    print("Neutro")
else:
    print('Positivo')
# Resultado Exemplo: Positivo

print(sentimento_texto) # Print Valor decimal sentimento
# Resultado Exemplo: 0.5