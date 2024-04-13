nome_arquivo = input("Nome arquivo: ")

try:
    with open(nome_arquivo, "r", encoding='utf8') as procurador:
        print("Arquivo localizado!!")
        for linha in procurador:
            print(linha,end="")
except:
    print("Algum problema para localizar o arquivo...")