#Funções anônimas, utilizadas uma unica vez
funcaoLambdaMono = (lambda x : x + 1) (x = 3)
print(f"Funcao anonima 1 parâmetro:  {funcaoLambdaMono}")

funcaoLambdaBi = (lambda x, y : x + y) (x = 3, y = 2)
print(f"Função anonima 2 parâmetros: {funcaoLambdaBi}")

# outra forma de implementar o codigo acima
funcaoLambda = lambda x, y : x + y
resultadoLambda = funcaoLambda(x = 6, y = 8)
print(f"Função anonima 2 parâmetros: {resultadoLambda}")
