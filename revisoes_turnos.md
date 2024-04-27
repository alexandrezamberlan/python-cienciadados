# Revisões
## 1ª Revisão
    - Uso do GitHub ou outro repositório sempre em projetos
        - na máquina a instalação do git (pacote de gestão do versionamento)
        - uso pode ser dinâmico:
            1) baixar na máquina pessoal e combinar com VS Code
            2) uso na Web direto no site do GitHub (logado)
            3) uso integrado com outras ferramentas Web (Replit, Google Colab)
    
    - Momento de usar 1ª vez VS Code (desktop)
        1) clonar projeto/repositório
        2) criar e ativar venv
        3) instalar os pacotes necessários do requirements.txt
    
    - Momento de usar demais vezes VS Code (desktop)
        1) puxar as atualizações do projeto
        2) ativar venv
        3) depois estabilizar a programação do código
        
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
        3) manipulação de arquivos texto (plain text)
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


