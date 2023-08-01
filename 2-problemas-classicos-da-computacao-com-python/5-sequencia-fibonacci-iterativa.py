"""Sequencia fibonacci iterativa - pequenos problemas em python
   - utilizacao de variaveis temporarias
"""
def fibonacci(numero: int) -> int:
    if numero == 0: return numero
    last: int = 0
    next: int = 1
    for _ in range(1, numero): last, next = next, last + next
    return next

if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))    
    print(fibonacci(5))
    print(fibonacci(55))