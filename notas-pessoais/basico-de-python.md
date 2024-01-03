# 1 - Primeiros Passos em Python

## Valores Imutáveis
Constantes com valores literais, ou seja, eles existem em si, e são o que são.

~~~python
2
3
4
"eu sou uma constante literal"
'tambem sou, não mudarei!'
~~~

## Conjunto de alfanuméricos e símbolos.

`atenção: string são imutaveis em python`

uma `string` e um conjuntos de caracteres que podem ser de natureza simbólica, alfabética ou numérica.

Para Utilização de strings podemos utilizar aspas simples, aspas duplas e uma tríade de aspas.
### String de aspas simples

~~~python
'eu sou uma citação!'
~~~ 

### String de aspas duplas
~~~python
"Qual é o seu nome?"
~~~

### String de aspas em triade
~~~python
"""Sou uma citação de muitas linhas.
E posso conter informações importantes. quando se tem muito a dizer.
"""
~~~

### String com método de formatos variados
uso de string com tipos de dados variados, pode ser criado através do método "texto (0)".format(formato)
~~~python
nome = "samuel"
idade = 31

mensagem = "Ola, eu sou {0} e tenho {1} anos de idade".format(nome, idade)
print(mensagem)

mensagem = f"Ola, eu sou {nome} e tenho {idade} anos de idade"
print(mensagem)
~~~
### Sequencia de Escape em Strings
~~~python
print('What's your name?')
~~~

#### erro com acento 
causa erro por usar aspas simples. podemos utilizar aspas duplas ou sequencia de escape `\`

~~~python
print("What's your name?")
print('What\'s your name?')
~~~
#### quebrar o texto somente no momento da programação
~~~python
mensagem = "Esta e a primeira frase \
esta e a segunda frase na mesma linha"

print(mensagem)
~~~

#### String bruta
parece da forma que e escrita
~~~python
print(r"primeira linha \n segunda linha")
print("aparece as secuencias de escopo")
~~~

## Variáveis 
### Nome de Identificação
### Tipo de Dados
### Objeto

