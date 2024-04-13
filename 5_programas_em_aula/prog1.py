#ano;glicemia;insulina;carb;kcal
linha = "2024;146;20 0;20"
linha = linha.replace(" ",";")
#manipulação de string: split e replace

vetor_linha = linha.split(";")

print(linha)
print(vetor_linha)

#[2024,146;20;0;20]
#instrucao de repeticao - for
for item in vetor_linha:
    print(item)

# for i in range(len(vetor_linha)):
#     print(vetor_linha[i])    

#regra da glicemia até 80 é abaixo; de 80 a 140 é normal; acima de 140 é acima
if int(vetor_linha[1]) < 80:
    vetor_linha[1] = "Abaixo"
elif int(vetor_linha[1]) < 140:
    vetor_linha[1] = "Normal"
else:
    vetor_linha[1] = "Acima"

#regra de carb até 100 abaixo; de 100 até 200 é normal; acima de 200 é acima
if int(vetor_linha[3]) < 100:
    vetor_linha[3] = "Abaixo"
elif int(vetor_linha[3]) < 200:
    vetor_linha[3] = "Normal"
else:
    vetor_linha[3] = "Acima"

print(vetor_linha)

