nome = "samuel oliveira"
nota = 8.5
fez_inscricao = True

print(nome)
print(nota)
print(fez_inscricao)

print(type(nome))
print(type(nota))
print(type(fez_inscricao))

nome = input("Digite seu nome: ")
print(nome)

print("Ola %s, seja bem vindo" % (nome))
print("Ola {}, seja bem vindo".format (nome))
print(f"Ola {nome}, seja bem vindo")

valorDeX = input("Informe o valor de X: ")
valorDeX = int(valorDeX)

valorDeY = input("Informe o valor de Y: ")
valorDeY = int(valorDeY)

soma = valorDeX + valorDeY
print(f"Soma: {soma}")

subtracao = valorDeX - valorDeY
print(f"subtracao: {subtracao}")

multiplicacao = valorDeX * valorDeY
print(f"multiplicacao: {multiplicacao}")

divisao = valorDeX / valorDeY
print(f"Disisao: {divisao}")

divisaoInteira = valorDeX // valorDeY
print(f"Divisao Inteira: {divisaoInteira}")

restoDivisao = valorDeX % valorDeY
print(f"Resto da Divisao: {restoDivisao}")

valorAbsolutoX = abs(valorDeX)
print(f"Valor Absoluto de X: {valorAbsolutoX}")

valorAbsolutoY = abs(valorDeY)
print(f"Valor Absoluto de Y: {valorAbsolutoY}")

potenciaXY = valorDeX ** valorDeY
print(f"x elevado a y: {potenciaXY}")

potenciaXY = pow(valorDeX, valorDeY)
print(f"x elevado a y: {potenciaXY}")

#Exercicio
mes = input("Digite o mes, que deseja o resultado!")
mes = int(mes)

crescimento = 200
previsao = crescimento * mes

print(f"Quantidade de pecas para o mes {mes}, sera de {previsao}")
