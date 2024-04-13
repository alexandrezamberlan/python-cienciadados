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