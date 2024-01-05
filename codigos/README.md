# python.noob

## Primeiros passos em python

~~~python
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

~~~

`python playground-1.py`

## Comparações em python
~~~python
valorDeA = 3
valorDeB = 5

# a menor que b
print(valorDeA < valorDeB)

#a maior que b
print(valorDeA > valorDeB)

#a menor igual a b
print(valorDeA <= valorDeB)

#a maior igual a b
print(valorDeA >= valorDeB)

#a igual de b
print(valorDeA == valorDeB)

#a diferente de b)
print(valorDeA != valorDeB)

# a identico a b / para objetos
print(valorDeA is valorDeB)

# a nao identico a b / para objetos
print(valorDeA is not valorDeB)

~~~
`python playground-2.py`

## Condicional If/Else em python
~~~python
#Teste Condicionais IF/ELSE
saldoAtualCliente = 15
saldoProximoCliente = 10

if saldoAtualCliente < saldoProximoCliente :
    print("saldo do cliente atual e menor que o saldo do proximo cliente")

    fechamentoCaixa = saldoAtualCliente + saldoProximoCliente
    print(f"Vendas do dia: {fechamentoCaixa}")
else :
    print("saldo do cliente atual e maior que o saldo do proximo cliente")
    
    fechamentoCaixa = saldoAtualCliente + saldoProximoCliente - 8
    print(f"Venda do dia - 8 reais de gastos: {fechamentoCaixa}")
~~~
`python playground-3.py`

<!---
## Subtitulo
~~~python
~~~
`python playground-0.py`
--->