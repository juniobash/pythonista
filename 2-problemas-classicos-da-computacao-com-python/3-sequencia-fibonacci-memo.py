"""Sequencia fibonacci com uso de memorization - pequenos problemas em python
   - armazena resultados de tarefas computacionais realizadas.
"""
from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}

def fibonacci(numero: int) -> int:
    if numero not in memo:
        memo[numero] = fibonacci(numero - 1) + fibonacci(numero - 2)
    return memo[numero]

if __name__ == "__main__":
    print(fibonacci(10))
    print(fibonacci(50))
