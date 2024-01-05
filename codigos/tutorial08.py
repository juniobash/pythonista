#Controle de repeticao com Range, Break e Continue

#range
for sequencia in range(5) :
	print(sequencia)

#break
disciplina = "linguagem de programação"
for letra in disciplina :
	
	if letra == "a" :
		break
		
	else :
		print(letra)

#continue
disciplina = "linguagem de programação"
for letra in disciplina :
	
	if letra == "a" :
		continue
		
	else :
		print(letra)

#exercicio
paragrafo = """
A inserção de comentários no código do programa é uma prática normal. 
Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas. 
O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo implementado (BANIN, 2018, p. 45).
"""
contagem = 0

for busca, letras in enumerate(paragrafo) :
	if letras == "a" or letras == "e" :
		print(f"vogal: {letras} encontrada, na posição {busca}")
		contagem = contagem + 1
	else :
		continue

print(f"numero de ocorrencias: {contagem}")
	
