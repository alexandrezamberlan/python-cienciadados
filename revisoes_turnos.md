# Revisões
## 1ª Revisão
    - Uso do GitHub ou outro repositório sempre em projetos
        - na máquina a instalação do git (pacote de gestão do versionamento)
        - uso pode ser dinâmico:
            1) baixar na máquina pessoal e combinar com VS Code
            2) uso na Web direto no site do GitHub (logado)
            3) uso integrado com outras ferramentas Web (Replit, Google Colab)
    - Importância de preparar uma base de dados para receber a mineração -> processo de reconhecimento de padrões
        - trabalhar com dados literias ou strings ou categorizados - dados de referência
    - Ecossistema Python
        - bibliotecas, pacotes, frameworks (boas práticas - padrões) e API (integração)
    - Ambiente desenvolvimento - Google Colab
    - Linguagem PYthon
        - instruções - diretivas de comunicação 
            - input
            - print
            - if
            - if - else
            - if - elif
            - while
            - for
        
## 2ª Revisão
    Na programação Python, em geral, há alguns recursos muito importantes:
        1) manipulação de strings
            split
            replace
            upper ou lower
        2) manipulação de listas
            len    - tamanho da lista
            append - adicionar
            remove - remover
            in     - verificar se algo está na lista
            sort   - ordenar
        3) manipulação de dicionários
            conteúdo é formado por um par -> chave:valor
        4) manipulação de arquivos texto (plain text)
            .dat
            .csv
            .json
            .xml

            arquivo -> está em memória secundária (ssd, hd, flash)
                nome
                extensão
                tipo
                tamanho
                endereço

            variável -> prima do arquivo, só que em memória principal (RAM)
                nome
                tipo
                tamanho
                endereço

            Na manipulação de arquivos em programas, um ARQUIVO precisa de uma VARIÁVEL
            em memória principal o representando. Aqui, na disciplina, PROCURADOR

            Operações:
                - abrir ou open -> associar o procurador a um endereço de arquivo
                    - leitura - read - r
                    - escrita nova - write - w
                    - escrita adição - append - a
                - fechar a conexão do procurador com o arquivo
                - percorrer o procurador
                    - ler
                        - linha a linha
                    - escrever
                        - linha a linha
## 3ª Revisão
    O Ecossistema Python: linguagem e bibliotecas|frameworks facilitam a construção de processos de descoberta de conhecimento
        - Bibliotecas clássicas para mineração de dados, reconhecimento de padrões e descoberta de conhecimento
            - TensorFlow
            - Pandas
            - Scikit learning
            - MatplotLib
            - Seaborn
        - Processo de minerar: i) limpeza (categorizar colunas); ii) localizar dados relevantes
        - Processo de reconhecer padrões: a partir dos dados trabalhados, perceber ou notar repetição|ocorrência
        - Processo de descoberta de conhecimento: a partir dos padrões reconhecidos, é possível tomar decisões


        - Base de dados:
            - estruturada -> vindas de banco de dados; xml; csv; json
            - não estruturadas -> textos (twiter, facebook, instagram, ...); textos jurídicos, entre outros
        - Fase de limpeza:
            - ter acesso ao arquivo: csv; json
            - carregar o arquivo de dados na memória
            - manipular limpezas:
                - exclusão de colunas
                - inclusão de colunas
                - trocar valores analógicos por valores categóricos
                - atualizar a base ou o arquivo
            - Formas de realizar:
                - linguagem Python e seus recursos básicos:
                    - instruções de controle: if, while, for
                    - manipulação de string
                    - manipulação de arquivo via variável 'procurador': percorrer, ler, escrever
                    - orientação a objetos: classe (atributos e métodos) e seus objetos|instância
                - linguagem Python e suas biliotecas
                    - biblioteca csv: para manipular o arquivo
                    - biblioteca statisctics: para manipular as medidas centrais: media, mediana, moda
                    - biblioteca numpy: para manipular as medidas centrais, exceto moda

## 4ª Revisão
    - Importância do tratamento da base de dados
        - identificar linhas ou registros inconsistentes|corrompidos

******************************
nome_arquivo = "dados.dat"

#[10/04/2024;65 , 11/04/2024;145 , 12/04/2024;98 , 13/04/2024;125; 13/04/2024;]

lista_glicemias = []
with open(nome_arquivo, "r", encoding='utf8') as procurador:
    for i,linha in enumerate(procurador):
        vetor_linha = linha.split(";")
        try:
            valor_corrigido = vetor_linha[1].replace("\n","")
            lista_glicemias.append(valor_corrigido)
        except:
            print('Erro na linha: ', i)
            
print(lista_glicemias)
******************************

    - Performance dentro base de dados: lista (array de 1 dimensao) e tabela (array de 2 dimensões)
        - list comprehension -> tratar lista com lista
            lista = [85, 98, 102, 102, 68, 95, 66, 55, 201]
            lista_hipoglicemia = []
            for item in lista:
                if item <= 70:
                    lista_hipoglicemia.append(item)

            lista = [85, 98, 102, 102, 68, 95, 66, 55, 201]
            lista_hipoglicemia = [item for item in lista if item <= 70]
        
        - biblioteca Numpy: computação científica de alto desempenho (funcionalidades são lançadas em cores de cpu ou gpu)
            - transformar listas e matrizes em arrays
            - realizar operações algébricas: somas, medias, medianas, multiplicação, divisão
                -

## 5ª Revisão
    - bibliotecas
        - pandas
            - comandos ou métodos básicos


### exemplo 1
import pandas as pd

data1 = {'ID': [1, 2, 3, 4, 5, 6],
         'Name': ['Ana', 'João', 'Ricardo','Alex', 'Bernardo', 'Carlos']}
data2 = {'ID': [1, 2, 3, 4, 5, 6],
         'Age': [25, 30, 35, 49, 21, 12]}

#### associando base em data frame
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

#### mesclando um data frame pela coluna ID da base
df_mesclado = pd.merge(df1, df2, on='ID', how='inner')

print("\nData frame mesclado:")
print(df_mesclado)

#### calculando a média do data frame pela coluna idade (Age)
media_idade = df_mesclado['Age'].mean()
print(f"\nMédia idade: {media_idade:.2f}")

#### mostrando filtros de linhas em que a idade (Age) é maior que a média
acima_media_idade = df_mesclado[df_mesclado['Age'] > media_idade]
print("\nPessoas acima da média:")
print(acima_media_idade)

#### ordenando o data frame pela coluna Age | idade, de forma decrescente
df_ordenado = df_mesclado.sort_values(by='Age', ascending=False)
print("\nData frame ordenado pelo atributo Age:")
print(df_ordenado)

#### criando nova coluna 'Is_Adult' baseada no atributo Age
df_ordenado['Is_Adult'] = df_ordenado['Age'] >= 18
print("\nData frame com nova coluna:")
print(df_ordenado)

#### agrupando dados pelo atributo 'Is_Adult' e calculando a média pelo atributo 'Age' de cada grupo criado
grupo_idades = df_ordenado.groupby('Is_Adult')['Age'].mean()
print("\nMédia idade por grupo 'Is_Adult': ")
print(grupo_idades)

### exemplo 2 - arquivo no google colab
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd

#### carregar arquivo em dataframe
arquivo = '<caminho do arquivo>' #arquivo com dados de glicemia por dias da semana

#### associando base em data frame
dataFrame = pd.read_csv(arquivo)

#### exibir fatias do dataframe
print(dataFrame[:5])
print(dataFrame[['Dia Semana', 'Resultado']][:5])
print(dataFrame.iloc[5:11, 0:3])

#### aplicar as medidas centrais: media, mediana e moda
mediana = dataFrame['Resultado'].median()
moda = dataFrame['Resultado'].mode()
media = dataFrame['Resultado'].mean()

#### limpar dados   
def classificar_resultado(valor):
    if valor <= 90:
        return 'baixo'
    elif valor <= 120:
        return 'normal'
    else:
        return 'alto'

dataFrame['Resultado'] = dataFrame['Resultado'].apply(classificar_resultado)

#### salvar no csv
dataFrame.to_csv(arquivo, index=False)
print(dataFrame[['Dia Semana', 'Resultado']][:10])

#### filtrar dados
dias_resultado_alto = dataFrame.loc[dataFrame['Resultado'] == 'alto']
print(dias_resultado_alto)

quantidade_dias_resultado_alto = dias_resultado_alto.value_counts()
print(quantidade_dias_resultado_alto)

dados_quarta = dataFrame.loc[dataFrame['Resultado'] == 'alto']
print(dados_quarta)

contagem_resultado = dataFrame['Resultado'].value_counts()
print(contagem_resultado)

#### corrigir dados:

especifico
dataFrame.at[3, 'Coluna'] = novo_valor

condição
dataFrame.loc[dataFrame['Coluna'] == valor_incorreto, 'Coluna'] = novo_valor

todo o DataFrame
dataFrame = dataFrame.replace(valor_incorreto, novo_valor)



        - matplotlib
