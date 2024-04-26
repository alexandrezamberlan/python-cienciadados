import random
#[[1,2,34,5][5,7][][][][]]
def gerar_listas(N, M):
    # listas = []
    # for _ in range(N):
    #     lista = []
    #     for _ in range(M):
    #         lista.append(random.randint(1, 100))
    #     listas.append(lista)
    # return listas
    
    listas = []
    for _ in range(N):
        lista = [random.randint(1, 100) for _ in range(M)]
        listas.append(lista)
    return listas

def mostrar_listas(listas):
    for i, lista in enumerate(listas):
        print(f"Lista {i + 1}: {lista}")

def numeros_que_aparecem(listas):
    numeros = set()
    for lista in listas:
        numeros.update(lista)
    return numeros

def numeros_que_aparecem_em_apenas_uma(lista_generica):
    numeros_repetidos = set()
    numeros_unicos = set()
    for lista in lista_generica:
        for numero in lista:
            if numero in numeros_repetidos:
                numeros_unicos.discard(numero)
            else:
                if numero in numeros_unicos:
                    numeros_unicos.remove(numero)
                else:
                    numeros_unicos.add(numero)
                    numeros_repetidos.add(numero)
    return numeros_unicos

Listas = 1000  # Número de listas
Tamanho = 500  # Tamanho das listas

listas = gerar_listas(Listas, Tamanho)

print("EXIBIÇÃO DAS LISTAS:")
mostrar_listas(listas)

print("\nNÚMEROS QUE APARECEM NAS LISTAS:")
print(numeros_que_aparecem(listas))

print("\nNÚMEROS QUE APARECEM EM APENAS UMA LISTA:")
lista_generica = [[6], [2, 6, 8, 10], [4, 6, 8], [6, 8], [1, 3, 5]]
print(numeros_que_aparecem_em_apenas_uma(lista_generica))
