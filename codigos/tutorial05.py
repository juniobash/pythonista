#estruturas logicas em python

quantidadeFaltas = int(
  input("Digite a quantidade de faltas: ")
)

mediaFinal = float(
  input("Digite a media final:")
)

if quantidadeFaltas <= 5 and mediaFinal >= 7 :
	print("Aluno Aprovado")
	
else :
	print("Aluno Reprovado")

#ordem de precedencia (not, and, or)

tamanhoRato = 15
tamanhoGato = 9
tamanhoCachorro = 9

print(
  tamanhoGato == tamanhoCachorro 
  or tamanhoRato < tamanhoGato 
  and tamanhoRato < tamanhoCachorro
)

print(
  (tamanhoGato == tamanhoCachorro 
   or tamanhoRato < tamanhoGato) 
   and tamanhoRato < tamanhoCachorro
)
