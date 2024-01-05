#o python nao possue switch, por isso usa-se ifelse aninhados

codigoCompra = input("Escolha O Modo de Pagamento : 5222, 5333 ou 5444 ")
codigoCompra = int(codigoCompra)

if codigoCompra == 5222 :
	print("compra a vista.")
	
elif codigoCompra == 5333 :
	print("compra a prazo no boleto")
	
elif codigoCompra == 5444 :
	print("compra a prazo no cartão")	
	
else :
	print("código não cadastrado")
	
print("fim do programa")
