nome = "gUIlherME RaFAEL"

print(nome.upper()) # Deixa todos os caracteres MAIÚSCULOS
print(nome.lower()) # Deixa todos os caracteres MINÚSCULOS
print(nome.title()) # Deixa o primeiro caractere MAIÚSCULO

texto = "  Olá mundo!    "

print(texto + ".")  # Adiciona um . no final do texto 
print(texto.strip() + ".") # Remove os espaços e adiciona um .
print(texto.rstrip())  # Remove os espaços da direita
print(texto.lstrip()) # Remove os espaços da esquerda

menu = "Python"

print("#### " + menu + " ####")
print(menu.center(50))
print(menu.center(50, "-"))
print("..".join(menu))
