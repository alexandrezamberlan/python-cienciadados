################################### primeira célula
nome_arquivo = '/content/alunos.csv'
#variavel -> estrutura de dados para armazenar dados em memória principal - nome, endereço, tamanho, tipo, ...
#arquivo  -> estrutura de dados para armazenar dados em memória secundária - nome, endereço, tamanho, tipo

#manipulação de arquivo -> manipula seu procurador em memória principal
#operações
  # percorrer
  # escrever
    # iniciar uma escrita do zero
    # apendar conteúdo a partir da ultima linha do arquivo
  # ler
  # definir quando ler e quando escrever é no momento da abertura
  # sempre que um arquivo é aberto, ou delegado um procurador, no final, ele precisa ser fechado

lista_alunos = []

#abrir o arquivo de inscritos.csv e popular a lista_inscritos
try:
  #abrindo ou associando um arquivo ao procurador para ser lido
  with open(nome_arquivo, "r", encoding='utf8') as arquivo:
    #codigo de manipulação
    for linha in arquivo:
      vetor_dados = linha.split(";")
      aluno = {
          'nome' : vetor_dados[0],
          'email': vetor_dados[1],
          'idade' : vetor_dados[2].replace('\n','')
      }
      lista_alunos.append(aluno)
except:
  print('Arquivo não localizado')


################################### segunda célula
lista_alunos_jovens = []
for aluno in lista_alunos:
  if int(aluno['idade']) < 30:
    lista_alunos_jovens.append(aluno)


for aluno in lista_alunos_jovens:
  print(f"Nome: {aluno['nome']}. Email: {aluno['email']} ")

################################### terceira célula
#depois da lista de jovens criada... persistir a lista em arquivo alunosJovens.csv
nome_arquivo_saida = '/content/alunos_jovens.csv'

try:
  with open(nome_arquivo_saida, "w", encoding='utf8') as arquivo:
    for aluno in lista_alunos_jovens:
      arquivo.write(f"{aluno['nome']};{aluno['email']};{aluno['idade']}\n")
      arquivo.flush()

    print('Arquivo de saída gerado....')
except Exception as e:
  print('Erro', e)
