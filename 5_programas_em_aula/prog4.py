lista_glicemias = [100,98,55,55,238,55,55,98,100,98,100,98,100,55]

lista_moda = []
valor_moda = ""
qtd_moda = 0
for item in lista_glicemias:
    ocorrencias = 0
    for outro_item in lista_glicemias:
        if (item == outro_item):
            ocorrencias += 1
    
    if (ocorrencias == qtd_moda):
        qtd_moda = item
        if item not in lista_moda:
            lista_moda.append(item)
        qtd_moda = ocorrencias
    elif (ocorrencias > qtd_moda):
        lista_moda.clear()
        qtd_moda = item
        if item not in lista_moda:
            lista_moda.append(item)
        qtd_moda = ocorrencias


print("A moda eh ou sao: ")
print(lista_moda, "ocorrendo", qtd_moda)