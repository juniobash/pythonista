from typing import Dict
memoria: Dict[int, int] = {0: 0, 1: 1}
print(f": {memoria}")

def fibonacci(_numero):
    if _numero not in memoria:
        memoria[_numero] = fibonacci(_numero - 1) + fibonacci(_numero - 2)
    return memoria[_numero]

if __name__ == "__main__":
    numero = 50
    resultado = fibonacci(numero)
    print(resultado)
    # nesta abordagem faz-se o uso de um dicionario de memorizacao
    # e reduz as interacoes 