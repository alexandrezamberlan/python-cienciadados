# Manipulando Virtual Environment

## Definição
Venv ou Virtual Environment é equivalente a um container ou docker,
ou seja, um ambiente virtual dentro da máquina com bibliotecas ou 
ferramentas específicas de um projeto.

## Dinâmica de trabalho

1) criar uma venv

python -m venv venv

2) ativar uma venv

Windows: venv\Scripts\activate (nao pode ser no terminal powershel)
Unix:    source venv/bin/activate

3) instalar ou configurar tecnologias

python -m pip install pandas

4) depois de criar, instalar, atualizar, configurar a venv, é necessário criar o arquivo
requirements.txt

python -m pip freeze > requirements.txt


5) toda vez que o repositório for clonado (usado pela primeira vez), é necessário:
    a) criar e ativar a venv
    b) instalar os pacotes que estão no arquivo requirements.txt
        python -m pip install -r requirements.txt


6) se for trocar de projeto ou repositório, lembre de desativar a venv
    deactivate