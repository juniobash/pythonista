"""Sequencia fibonacci recursiva - pequenos problemas em python
"""
def fibonacci(numero: int) -> int:
    return fibonacci(numero - 1) + fibonacci(numero - 2)

if __name__ == "__main__":
    print("fibonacci recursiva que gera um loop infinito!")
    print(fibonacci(5))
            
