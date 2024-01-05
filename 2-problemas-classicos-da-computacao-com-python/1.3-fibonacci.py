from functools import lru_cache
@lru_cache(maxsize=None)

def fibonacci(_numero):
    if _numero < 2:
        return _numero
    return fibonacci(_numero - 1) + fibonacci(_numero - 2)

if __name__ == "__main__":
    numero = 50
    resultado = fibonacci(numero)
    print(resultado)
    # nesta abordagem utiliza-se a memoria cache da ultima iteracao
    # para a execucao atual. 

