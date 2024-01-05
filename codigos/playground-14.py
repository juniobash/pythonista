# passagem de parâmetros posicionais indefinidos com *args
def imprimirParametros(*args) :
    quantidadeParametros = len(args)
    print(f"Quantidade de parâmetros = {quantidadeParametros}")
    
    for iterador, valor in enumerate(args) :
        print(f"Posição = {iterador}, valor = {valor}")

print("\nChamada 1")
imprimirParametros("São Paulo", 10, 23.78, "João")

print("\nChamada 2")
imprimirParametros(10, "Curitiba")
