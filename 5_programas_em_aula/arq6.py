nome_arquivo = "dados_glicemia.dat"

#trazer os dados do arquivo para memória principal em uma lista
lista_glicemia = []

with open(nome_arquivo,"r", encoding="utf8") as procurador:
    for linha in procurador:
        dado_corridigo = linha.replace("\n","")
        lista_glicemia.append(int(dado_corridigo))

print(lista_glicemia)

with open(nome_arquivo,"a", encoding="utf8") as procurador:
    while (True):
        valor_glicemia = input("Digite valor glicemia ou 0 para finalizar: ")
        if (valor_glicemia == "0"):
            break #sair do laço de repetição
        
        lista_glicemia.append(int(valor_glicemia))
        procurador.write(valor_glicemia+"\n")
        procurador.flush()

with open(nome_arquivo,"w", encoding="utf8") as procurador:
    lista_glicemia.sort()
    for item in lista_glicemia:
        procurador.write(str(item)+"\n")

