#Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens:
#    Carioca Paulista Mineiro Outros estados

estado_dicionario = {}
estado_dicionario['RS'] = 'gaúcho'
estado_dicionario['SC'] = 'catarina'
estado_dicionario['PR'] = 'paranaense'
estado_dicionario['SP'] = 'paulista'
estado_dicionario['RJ'] = 'carioca'
estado_dicionario['MG'] = 'mineiro'


estado = input('Qual a sigla do seu estado? ').upper()

try:
    print('Olá', estado_dicionario[estado])
    calculo_errado = 12/0
except Exception as e:
    print('Erro', e)


for item in estado_dicionario:
    print(item, estado_dicionario[item])

while (True):
  try:
    idade = int(input('Qual sua idade? '))
    if (idade < 5):
      raise Exception('idade invalida')
    sono = idade / 3
    print('Vc já dormiu',sono,'anos')
    break
  except Exception as e:
    print('Erro', e)