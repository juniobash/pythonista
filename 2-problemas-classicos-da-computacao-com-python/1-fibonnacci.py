def fibonacci(_numero):
     """ Formula do calculo da sequencia fibonacci
     """
     return fibonacci(_numero - 1) + fibonacci(_numero -2)

if __name__ == "__main__":
     numero = 3
     resultado = fibonacci(numero)
     print(resultado)
    # codigo provoca um erro por nao conter um limite e execucao, 
    # isso gera um loop infinito.