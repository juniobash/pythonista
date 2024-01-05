from typing import Generator

def fibonacci(_numero) -> Generator[int, None, None]:
    yield 0 # caso especial
    if _numero > 0: 
        yield 1 # caso especial
    
    ultimo = 0
    proximo = 1
    for _ in range(1, _numero):
        ultimo, proximo = proximo, ultimo + proximo
        yield proximo

if __name__ == "__main__":
    numero = 50
    for iterador in fibonacci(numero):
        print(iterador)
