from oo1 import Glicemia

# abrir e capturar as linhas do arquivo dados_glicemia_oo.dat
nome_arquivo = "dados_glicemia_oo.dat"
lista_glicemias = []
with open(nome_arquivo,"r",encoding="utf8") as leitor:
    for linha in leitor:
        # splitar a linha e criar um objeto do tipo Glicemia para cada linha
        vetor_linha = linha.split(";")
        #[Quinta,2012,ac,90,6,2037,246,4]

        # inserir o objeto gerado na lista de glicemias
        #Quinta,2012,ac,90,6,2037,246,4
        obj = Glicemia(vetor_linha[0],vetor_linha[1],vetor_linha[3],vetor_linha[4],vetor_linha[5],vetor_linha[6],vetor_linha[7])
        lista_glicemias.append(obj)

# operações

lista_glicemias.sort(key = lambda glicemia: glicemia.carb)

print("Quantos dados foram capturados? " + str(len(lista_glicemias)))
for item in lista_glicemias:
    print(item)

#dia normal de glicemia são valores entre 80 e 140
qtd_dias_normais = 0
for item in lista_glicemias:
    if item.valor_glicemia >= 80 and item.valor_glicemia < 140:
        qtd_dias_normais += 1

print("Total de dias em glicemia normal: " + str(qtd_dias_normais))










