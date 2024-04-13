nome_arquivo = "dados_finais.csv"

with open(nome_arquivo, "w", encoding='utf8') as procurador:
    while (True):
        dados = input("Informe dia e valor de glicemia separados por ';' ou 0 para sair: ")
        if (dados == "0"):
            break
        procurador.write(dados + "\n");
        procurador.flush()