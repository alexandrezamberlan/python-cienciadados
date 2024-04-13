# Teoria ou paradigma de programação Orientado a Objetos, é a teoria da TERCEIRIZAÇÃO

# Ecossistema Python é rico em 
    # API                   - coleção de recursos para integração de serviços: pode conter frameworks e/ou bibliotecas
    # Framework             - coleção de classes/categorias e serviços
    # Bibliotecas/Pacotes   - coleção de serviços

class Glicemia: #todo nome de classe tende a começar com maiúsculo
    #Quinta,2012,ac,90,6,2037,246,4

    #é necessário de um método/serviço que crie ou instancie um objeto do tipo Glicemia
    def __init__(self, dia_semana, ano, valor_glicemia, valor_insulina, kcal, carb, qualidade_sono):
        self.dia_semana = dia_semana
        self.ano = ano
        self.valor_glicemia = valor_glicemia
        self.valor_insulina = valor_insulina
        self.kcal = kcal
        self.carb = carb
        self.qualidade_sono = qualidade_sono


    #estamos reescrevendo o método que gera uma string do objeto Glicemia
    def __str__(self):
        return f"Glicemia[Dia:{self.dia_semana}, Ano:{self.ano}, Valor Glicemia:{self.valor_glicemia}]"