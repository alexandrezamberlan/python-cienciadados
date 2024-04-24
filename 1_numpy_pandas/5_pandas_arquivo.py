from google.colab import drive
drive.mount('/content/drive')
import pandas as pd

#carregar arquivo em dataframe
arquivo = ""
dataFrame = pd.read_csv(arquivo)

print(dataFrame)

#exibir fatias do dataframe
print(dataFrame[:5])
print(dataFrame[['Dia Semana', 'Resultado']][:5])
print(dataFrame.iloc[5:11, 0:3])

#aplicar as medidas centrais: media, mediana e moda
mediana = dataFrame['Resultado'].median()
moda = dataFrame['Resultado'].mode()
media = dataFrame['Resultado'].mean()

print("Mediana:", mediana)
print("Moda:", moda)
print("Média:", media)

#limpar dados
def classificar_resultado(valor):
    if valor <= 90:
        return 'baixo'
    elif valor <= 120:
        return 'normal'
    else:
        return 'alto'

dataFrame['Resultado'] = dataFrame['Resultado'].apply(classificar_resultado)
#salvar no csv
dataFrame.to_csv(arquivo, index=False)
print(dataFrame[['Dia Semana', 'Resultado']][:10])

#filtrar dados
dias_resultado_alto = dataFrame.loc[dataFrame['Resultado'] == 'alto']
print(dias_resultado_alto)

quantidade_dias_resultado_alto = dias_resultado_alto.value_counts()
print(quantidade_dias_resultado_alto)

dados_quarta = dataFrame.loc[dataFrame['Resultado'] == 'alto']
print(dados_quarta)

contagem_resultado = dataFrame['Resultado'].value_counts()
print(contagem_resultado)

#corrigir dados:

#especifico
dataFrame.at[3, 'Coluna'] = novo_valor
#condição
dataFrame.loc[dataFrame['Coluna'] == valor_incorreto, 'Coluna'] = novo_valor
#todo o DataFrame
dataFrame = dataFrame.replace(valor_incorreto, novo_valor)

