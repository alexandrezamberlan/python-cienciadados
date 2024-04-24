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

#corrigir dados:

#especifico
df.at[3, 'Coluna'] = novo_valor
#condição
df.loc[df['Coluna'] == valor_incorreto, 'Coluna'] = novo_valor
#todo o DataFrame
df = df.replace(valor_incorreto, novo_valor)

