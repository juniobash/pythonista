"""Sequencia fibonacci com cache - pequenos problemas em python
   - recupera resultados da funcao executada.
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(numero: int) -> int:
    if numero < 2:
        return numero
    return fibonacci(numero - 1) + fibonacci(numero - 2)

if __name__ == "__main__":
    print(fibonacci(5))
    print(fibonacci(55))
    