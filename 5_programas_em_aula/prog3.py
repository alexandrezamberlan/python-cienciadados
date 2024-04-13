lista_glicemias = [100,98,78,45,238,390,67,98,100,98,100,98,67,55]


for item in lista_glicemias:    
    if (item < 75):
        print(item, "Abaixo")
    elif (item < 140):
        print(item, "Normal")
    else:
        print(item, "Acima")

print(lista_glicemias)

soma = 0
for item in lista_glicemias:
    soma = soma + int(item)

media = soma / len(lista_glicemias)
print("A média de glicemia: ", media)


#para calcular a mediana é necessário ordenar a estrutura
lista_glicemias.sort()

indice_meio = int(len(lista_glicemias)/2)
print("A mediana de glicemia: ", lista_glicemias[indice_meio])

vezes_hipoglicemia = 0
for item in lista_glicemias:
    if int(item) < 70:
        #vezes_hipoglicemia = vezes_hipoglicemia + 1
        vezes_hipoglicemia += 1

print("Quantidade de vezes de hipoglicemia: ", vezes_hipoglicemia)

#len(lista_glicemias) --- 100%
#vezes_hipoglicemia   --- x
porcentagem_hipoglicemia = vezes_hipoglicemia * 100 / len(lista_glicemias)

print("Porcentagem de hipo: ", porcentagem_hipoglicemia)


valor_moda = ""
qtd_moda = 0
for item in lista_glicemias:
    ocorrencias = 0
    for outro_item in lista_glicemias:
        if (item == outro_item):
            ocorrencias += 1
    
    if (ocorrencias > qtd_moda):
        valor_moda = item
        qtd_moda = ocorrencias


print("A moda: ", valor_moda,"ocorrendo ", qtd_moda,"vezes")