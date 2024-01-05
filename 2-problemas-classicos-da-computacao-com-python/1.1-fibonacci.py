def fibonacci(_numero):
    if _numero < 2:
        return _numero
    return fibonacci(_numero - 1) + fibonacci(_numero - 2)

if __name__ == "__main__":
    numero = 7
    resultado = fibonacci(numero)
    print(f"Fibonacci: {resultado}")

    numero = 10
    resultado = fibonacci(numero)
    print(f"Fibonacci: {resultado}")

    numero = 50
    resultado = fibonacci(numero)
    print(f"Fibonacci: {resultado}")
    # causa um erro de calculo, pois a cada chamada da funcao ela e duplicada
    # gerando assim um calculo quase infinito.