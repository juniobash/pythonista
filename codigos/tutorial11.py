# criando funcoes em python

def uma_funcao( ) :
    print("eu sou uma funcao")
    
uma_funcao()

# funcao de retorno vazia 
def imprimir_mensagem(disciplina, curso) :
    print(f"""
      Minha primeira funcao em Python
      desenvolvida na disciplia:{disciplina}
      do curso: {curso}.""")

imprimir_mensagem("Python Intro", "ADS")

#funcao com retorno e armazenamento em variavel
def retorno_mensagem(disciplina, curso) :
    return(f"""
      Minha primeira funcao em Python
      desenvolvida na disciplia:{disciplina}
      do curso: {curso}.""")
    

mensagem = retorno_mensagem("Pyton Core","ASDF")
print(mensagem)
