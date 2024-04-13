lista_glicemias = [100,98,78,45,238,390,67,98,100,98,100,98,67,55]

lista_glicemias_categorizada = []

for item in lista_glicemias:  
    if (item < 55):
        lista_glicemias_categorizada.append("Risco Abaixo")  
    elif (item < 75):
        lista_glicemias_categorizada.append("Abaixo")
    elif (item < 140):
        lista_glicemias_categorizada.append("Normal")
    else:
        lista_glicemias_categorizada.append("Acima")
    

print(lista_glicemias)
print(lista_glicemias_categorizada)

vezes_hipoglicemia = 0
for item in lista_glicemias_categorizada:
    if item in ["Risco Abaixo", "Abaixo"]:        
        vezes_hipoglicemia += 1

print("Quantidade de vezes de hipoglicemia: ", vezes_hipoglicemia)

#len(lista_glicemias) --- 100%
#vezes_hipoglicemia   --- x
porcentagem_hipoglicemia = vezes_hipoglicemia * 100 / len(lista_glicemias)

print("Porcentagem de hipo: ", porcentagem_hipoglicemia)


valor_moda = ""
qtd_moda = 0
for item in lista_glicemias_categorizada:
    ocorrencias = 0
    for outro_item in lista_glicemias_categorizada:
        if (item == outro_item):
            ocorrencias += 1
    
    if (ocorrencias > qtd_moda):
        valor_moda = item
        qtd_moda = ocorrencias


print("A moda: ", valor_moda,"ocorrendo ", qtd_moda,"vezes")