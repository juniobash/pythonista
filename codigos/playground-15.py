# uso do kwargs
def imprimirParamentros(**kwargs) :
    print(f"Tipo de Objeto Recebido = {type(kwargs)}\n")
    quantidadeParamentros = len(kwargs)
    print(f"Quantidade de parâmetros = {quantidadeParamentros}")
    
    for chave, valor in kwargs.items() :
        print(f"variavel = {chave}, valor = {valor}")

print("\nChamada 1")
imprimirParamentros(cidade = "Curitiba", idade = 22, nome = "Samuel")

print("\nChamada 2")
imprimirParamentros(desconto = 10, valor = 1000)