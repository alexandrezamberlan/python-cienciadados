import csv
import random
from faker import Faker

# Inicializa gerador de dados falsos
faker = Faker('pt_BR')

# Abrir arquivo para escrita
with open("dados_alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo, delimiter=';')
    
    # Gerar 100 linhas
    for _ in range(100):
        nome = faker.name()
        email = nome.lower().replace(" ", ".") + "@ufn.edu.br"
        idade = random.randint(18, 80)
        
        escritor.writerow([nome, email, idade])

print("Arquivo 'dados_alunos.csv' gerado com sucesso!")
