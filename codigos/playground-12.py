# Funções de parâmetros definidos e indefinidos
print("Parâmentro posicional, sem valor padrão")

def somar(valorDeA, valorDeB) :
    return valorDeB + valorDeA

resultadoSoma = somar(2, 3)

print(f"Soma: {resultadoSoma}")

# Função de parâmetros Com Valor Padrão definido
print("Parâmetro posicional, com valor padrão")

def calcularDesconto(valorDinheiro, desconto = 0) :
    valorComDesconto = valorDinheiro - ( valorDinheiro * desconto)
    return valorComDesconto

vendaSemDesconto = calcularDesconto(100)
vendaComDesconto = calcularDesconto(100, 0.25)

print(f"Venda Sem Desconto: {vendaSemDesconto}")
print(f"Venda Com Desconto: {vendaComDesconto}")

