# 'pip install speedtest-cli' # Instalar biblioteca

# Importando Biblioteca
import speedtest

# Recebe resultado Teste de velocidade
velocidade = speedtest.Speedtest()

# Atribui velocidade de Download
download = round(velocidade.download()/1000000,2)

# Atribui velocidade de Upload
upload = round(velocidade.upload()/1000000,2)
# Dividindo por 1 milhão para converter bit para MB/s 
# arrenda para duas casas decimais com round

# Mostrando Resultado
print(f"Velocidade de Download em Mbps: {download}")
# Velocidade de Download em Mbps: 52.11

print(f"Velocidade de Upload em Mbps: {upload}")
# Velocidade Upload em Mbps: 10.23