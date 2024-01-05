# uso de funcoes padroes do python
numeroDeA = 2
numeroDeB = 1

equacao = input ("""
  Digite a formula geral da
  equacao linear (numeroDeA * valorDeX + numeroDeB)
""")

print(f"""
  \nA entrada do Usuario {equacao}
  e do tipo {type(equacao)}
""")

for valorDeX in range(5) :
    valorDeY = eval(equacao)
    print(f"\nResultado da equacao para x = {valorDeX} e {valorDeY}")