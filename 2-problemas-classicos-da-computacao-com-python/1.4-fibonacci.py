def fibonacci(_numero):
    if _numero == 0: return _numero
    ultimo = 0
    proximo = 1
    for _ in range(1, _numero):
        print(f"{ultimo}, {proximo} = {proximo}, {ultimo + proximo}")
        ultimo, proximo = proximo, ultimo + proximo
    return proximo


if __name__ == "__main__":
    entrada_numero = 69
    resultado = fibonacci(entrada_numero)
    print(f"Fibonacci = {resultado}")