import numpy as np

# Criando um array unidimensional
array_1d = np.array([1, 2, 3, 4, 5])
print("Array unidimensional:")
print(array_1d)

# Criando um array bidimensional
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nArray bidimensional:")
print(array_2d)


# Indexação em arrays unidimensionais
print("\nIndexação e Slicing em arrays unidimensionais:")
print("Primeiro elemento:", array_1d[0])
print("Último elemento:", array_1d[-1])
print("Slicing do segundo ao quarto elemento:", array_1d[1:4])

# Indexação em arrays bidimensionais
print("\nIndexação e Slicing em arrays bidimensionais:")
print("Elemento na segunda linha e terceira coluna:", array_2d[1, 2])
print("Primeira coluna:", array_2d[:, 0])
print("Última linha:", array_2d[-1, :])
print("Slicing da segunda e terceira linha e segunda coluna:", array_2d[1:3, 1])


# Operações básicas com arrays
print("\nOperações básicas com arrays:")
# Soma de elementos de um array unidimensional
print("Soma dos elementos do array unidimensional:", np.sum(array_1d))
# Soma de elementos de um array bidimensional
print("Soma dos elementos do array bidimensional:", np.sum(array_2d))
# Multiplicação de um array por um escalar
print("Multiplicação do array unidimensional por 2:", array_1d * 2)
# Multiplicação de dois arrays
print("Multiplicação elemento a elemento dos dois arrays:", array_1d * array_1d)
# Produto escalar de dois arrays
print("Produto escalar dos dois arrays:", np.dot(array_1d, array_1d))
