"""Sequencia fibonacci ponto de parada - pequenos problemas em python
"""
def fibonacci(numero: int) -> int:
    if numero < 2:
        return numero
    return fibonacci(numero - 2) + fibonacci(numero - 1)

if __name__ == "__main__":
    print("sequencia fibonacci com ponto de parada!")
    print(fibonacci(5))
    print(fibonacci(10))
    print(fibonacci(12))
    print(fibonacci(15))
    
    print("impossivel calcular a partir de 50")
    print(fibonacci(50))
