def cadastrarPessoa(nome, idade, cidade) :
    print("\nDados a serem cadastrados: ")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

cadastrarPessoa("Jõao", 23, "São Paulo")
cadastrarPessoa("São Paulo", "Jõao", 23)

print("erro de logica, ao armazenar os dados trocados")

# Definição de parâmetros nominais
def converterMaiuscula(texto, flagMaiuscula) :
    if flagMaiuscula :
        return texto.upper()
    else :
        return texto.lower()

textoEmMaiusculo = converterMaiuscula(flagMaiuscula = True, texto = "João")

print(f"{textoEmMaiusculo}")

def converterMinuscula(texto, flagMinuscula = True) :
    if flagMinuscula :
        return texto.lower()
    else :
        return texto.upper()
        
textoEmMinusculo1 = converterMinuscula(flagMinuscula = True, texto = "OiO")
textoEmMinusculo2 = converterMinuscula(texto = "Linguagem de Programação")

print(f"Passagem Nominal, Sem valor padrão: \n{textoEmMinusculo1}")
print(f"Passagem Nominal, Com valor padrão: \n{textoEmMinusculo2}")