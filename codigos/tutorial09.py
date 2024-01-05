#calculo do imposto de renda

salarioColaborador = 0
salarioColaborador = int (
  input("Digite o salario do Colaborador! ")
)

if salarioColaborador <= 1903.98 :
	print("Insento de Imposto!")

elif salarioColaborador <= 2826.65 :
	print("R$142,80 de imposto")

elif salarioColaborador <= 3751.05 :
	print("R$354,80 de imposto")
	
elif salarioColaborador <= 4664.68 :
	print("R$ 636,13 de imposto")
	
else :
	print("R$869,36 de imposto")
