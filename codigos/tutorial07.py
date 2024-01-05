#estrutura de repeticao em python
#for

# percorre a string e retorna item a item
tituloLivro = "caibalion"
for letra in tituloLivro :
	print(letra)

# percorre string e retorna a iterador
nome = "samuel oliveira"
for iterador, letra in enumerate(nome) :
	print(f"Posição: {iterador}, letra: {letra}")
