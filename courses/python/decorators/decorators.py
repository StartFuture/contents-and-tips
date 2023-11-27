# Definindo a função Decorator
def timer(func):
    # Importando o módulo datetime
    from datetime import datetime
    # Definindo a função wrapper
    def wrapper(*args, **kwargs):
        # printando o nome da função
        print(f"Nome da Função: {getattr(func, '__name__')}")
        start = datetime.now() # tempo inicial
        func(*args, **kwargs) # chamando a função
        end = datetime.now() # tempo final
        time_to_run = end - start # tempo de execução
        # printando o tempo de execução
        print(f'Tempo de execução: {time_to_run}')
    return wrapper


@timer # Decorator
# Definindo a função que será decorada
# nesse caso, criei um exemplo de uma
def wait_5_seconds():
    # Aqui você escreve o código para pegar o tempo de execução
    from time import sleep
    sleep(5)

wait_5_seconds() # chamando a função