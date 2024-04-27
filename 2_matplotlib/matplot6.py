from __future__ import with_statement

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nome_arquivo = ('/content/data/dados.dat')

dia_semana = []
valor_glicemico = []

dataFrame = pd.read_csv(nome_arquivo,sep=';')

dia_semana = dataFrame['dia_semana']
valor_glicemico = dataFrame['valor_glicemia']

plt.title("Medidas glicêmicas semanal")
plt.xlabel("Dia da semana")
plt.ylabel("Valor glicêmico")
plt.bar(dia_semana,valor_glicemico)
plt.show()