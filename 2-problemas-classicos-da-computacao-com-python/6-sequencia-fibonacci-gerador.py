"""Sequencia fibonacci com um gerador - pequenos problemas em python
   - usando gerador com a instrucao yield
"""
from typing import Generator

def fibonacci(numero: int) -> Generator[int, None, None]:
    yield 0
    if numero > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, numero):
        last, next = next, last + next
        yield next
        
if __name__ == "__main__":
    for iterator in fibonacci(50):
        print(iterator)