""" Primeiros Passos em Python
"""
__author__ = "juniobash"

# Primeiro programa em python, utilizando a funcao print() e um comentario com 
## o simbolo [ # ]
print("ola, mundo cruel!")

# Constantes Literais em python
2
5.15

# Tipos de numeros
## numeros de tipo inteiro
2
-3

## numeros de tipo de ponto flutuante
2.33
52.3E-4

# Variaveis & nomes validos, armazena texto ou numeros
nome = 'samuel'
nome_cliente = 'joao'
i = 0
_senha = 'segredo'

# Objetos, tudo em python e um objeto, texto numero e funcoes
texto_objeto = 'objeto'
numero_objeto = 0
def objeto(): print("objeto")

# Strings sao imutaveis.
## aspas simples, usada em variaveis, identificadoes ou atributos e expressoes
## regulares, como no caso de sql
'tudo o que esta escrito, e preservado. espacos e tabs'
cor = 'azul'
def funcao(self): self.nome = 'Samuel'
create_database_query = 'CREATE DATABASE school'

## aspas dupla, utilizada em saida de textos informativos ou longos
## onde possivelmente pode ocorrer o uso de aspas simples.
"funciono de forma identica que as aspas simples"
message = "Hey! he's my friend!"
print("Quem e, o 'fulano de tal'?")

## aspas triplas, utilizada em comentarios ou em situacoes onde necessita
## de texto com varias linhas. ou o uso de aspas duplas ou simples no texto
print("""_"you can programming softly and beautiful" said @codenymhps""")

''' Eu sou uma string de multiplas linhas
    e posso ser escrita com as aspas simples
    '''

""" Eu sou uma string de multiplas linhas
    e posso tambem ser escrita com aspas duplas
    """

create_client_table = """
CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40) NOT NULL,
  address VARCHAR(60) NOT NULL,
  industry VARCHAR(20)
);
"""

# Manupulando strings com format()
name = 'samuel'
favorite_color = 'blue'
favorite_passtime = "play games and read book's"

print("Hi!, i'm {0} and i like {1} and my favorite passtime, is {2}"
      .format(name, favorite_color, favorite_passtime))

print(f"Hi!, i'm {name} and i like {favorite_color} "
      + f"and my favorite passtime, is {favorite_passtime}")

# Imprimir mensagem na tela, sem quebra de linha
print(1, end='')
print(2)

print("Ola, o texto nao tem quebra de linha,", end=' ')
print("e termina com espaco! agora quebrou.")

# Sequencias de Escape 'dentro das aspas'
## \ - e utilizado para dividir o codigo em varias linhas, mas sendo uma linha
print("oi, eu sou uma linha \
agora contino o texto em outra linha \
mas continuo sendo uma so linha!")
      
## \n - e utilizado para quebra de o texto em nova linha
print("ola!\neu sou uma\nquebra de linha")

## \t - e utilizado para inserir espacos 'tab' dentro do texto
print("idade:\tsamuel")
print("nome:\t32")
## \\ - imprimi a contra barra, mas recomenda-se utilizar r"\" ao inves "\\"
caminho_arquivo = '\\home\\nymphs\\'
print(caminho_arquivo)
print("cd \\home\\nymphs")

## \'
promome_abreviado = 'he\'s'
print(promome_abreviado)

## String raw ou string crua
print(r"\home\nymphs")

# variaveis e constantes
i = 5
print(i)

i = i + 1
print(i)

poema = """Os labios da sabedoria
estao fechados. exceto 
aos ouvidos do entendimento.
 - Hermes Trimegisto"""
print(poema)

# uma linha, uma logica de comando
i = 5
print(i)

i =5; print(i)  # nao recomendado

numero_com_nome_de_variavel_longa = 2
numero_com_nome_de_variavel_mais_longa_ainda = 5

resultado_com_nome_de_variavel_logo = numero_com_nome_de_variavel_longa + \
numero_com_nome_de_variavel_mais_longa_ainda
print(resultado_com_nome_de_variavel_logo)  # uso nao recomendado

# identacao, blocos de codigos em python sao feitos atraves a identacao
print("bloco principal")
lista = {1,2,3,4,5,6,7,8,9}
for item in range(0, len(lista)):
    print(f"bloco auxiliar: {item}")