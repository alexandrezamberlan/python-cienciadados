#abrir o arquivo de inscritos.csv e popular a lista_inscritos
nome_arquivo = "dados.dat"


#abrindo o arquivo no modo leitura, onde a variavel procurado representa o arquivo na memoria

#[10/04/2024;65 , 11/04/2024;145 , 12/04/2024;98 , 13/04/2024;125]
#procurador eh a lista de cada medição de glicemia

lista_glicemias = []
with open(nome_arquivo, "r", encoding='utf8') as procurador:
    for linha in procurador:
        vetor_linha = linha.split(";")
        valor_corrigido = vetor_linha[1].replace("\n","")
        lista_glicemias.append(valor_corrigido)
        
print(lista_glicemias)

     


