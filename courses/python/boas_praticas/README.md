# Boas práticas python

## Guia

### Ambientes virtuais (venv)

Ambiente virtual do python, utilizado para separar as dependências de projetos diferentes.

#### instalando o virtualenv

```bash
pip install virtualenv
```

#### Criando o virtualenv

```bash
python -m virtualenv venv
```

#### ativando o virtualenv

##### Windows (CMD)

```bash
venv/Scripts/activate
```

##### Linux

```bash
source venv/bin/activate
```

#### Desavitando o virtualenv

```bash
deactivate
```

### pep8

Conjunto de boas práticas a serem seguidas para o python

#### importação

##### Ordem

separado por espaço

1. Built-in

1. Pacotes desenvolvidos

1. Pacotes externos

##### Exemplo

```
import os
import sys

import pacote.modulo

import flask
```

#### snakecase

Recomendação de como se escrever cada tipo de elemento no python

##### Descrição snakecase

variável - sempre em minusculo com as palavras separadas por `_` conforme necessário
constante - sempre em Maiúsculo com as palavras separadas por `_` conforme necessário
função - sempre em minusculo com as palavras separadas por `_` conforme necessário
classe - Primeira letra em Maiúsculo sem separador (quando escrever sigla colocar toda a sigla em maiúsculo)

##### exemplos snakecase

###### variável

```python
alguma_variavel_bem_util = ''
```

###### constante

```python
ALGUMA_CONSTANTE_BEM_UTIL = ''
```

###### função

```python
def alguma_funcao_bem_util():
 ...
```

###### classe

```python
class AlgumaClasseBemUtil:
 ...
```

#### typehint

Como o python é uma linguagem bem versátil, você pode definir os tipos para ter funções mais legíveis e claras

##### tipos nativos

para utilizar os tipos nativos você pode simplesmente colocar : após a variável e o tipo esperado, exemplos:

```python
# Nessa função ele espera 2 parâmetros: a e b, ambos float e retorna um float também
def soma(a : float, b : float) -> float:
 c = a + b
 return c
```

Você pode utilizar tipos variados também, como no exemplo abaixo:

```python
def compra(nome_cliente : str, nome_produto : str, valor_produto : float) -> str:
 legenda = f'o cliente {nome_cliente} comprou o produto {nome_produto} pelo preço de {valor_produto}'
 return legenda
```

## Referencias

* [https://pep8.org](PEP8 - Boas Praticas Python)
* [https://docs.python.org/3/](Python - Doc oficial)
* [https://docs.python.org/pt-br/3/installing/index.html](Python - Doc oficial - Instalando módulos)
* [https://docs.python.org/pt-br/3/library/index.html](Python - Doc oficial - Bibliotecas built-in)
* [https://docs.python.org/pt-br/3/howto/index.html](Python - Doc oficial - Tutoriais básicos)
