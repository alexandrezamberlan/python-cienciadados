lista_glicemias = [100,98,78,45,238,390,67,89,100,98,100,98,67,55]

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