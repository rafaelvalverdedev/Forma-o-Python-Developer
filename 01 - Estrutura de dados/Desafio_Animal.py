''''
#Desafio
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, 
da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três
 palavras fornecidas.

#Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, 
com todas as letras minúsculas.

# Saída
Imprima o nome do animal correspondente à entrada fornecida.

Exemplo de Entrada	Exemplo de Saída
    vertebrado   |   homem
    mamifero     |   
    onivoro      |   

Exemplo de Entrada	Exemplo de Saída
    vertebrado   |   aguia
    ave          |   
    carnivoro    |   

Exemplo de Entrada	Exemplo de Saída
    invertebrado |   minhoca
    anelideo     |   
    onivoro      |   
'''

a = input() 
b = input() 
c = input() 

if a == 'vertebrado':   # ENTRADA A
  if b == 'ave':        # ENTRADA B
    if c == 'carnivoro':
      animal = 'aguia'
    else:
      animal = 'pomba'
      
  else:                 # ENTRADA B
    if c == 'onivoro':
      animal = 'homem'
    else:
      animal = 'vaca'

elif a == 'invertebrado':    # ENTRADA A
  if b == 'inseto':
    if c == 'hematofago':
      animal = 'pulga'
    else:
      animal = 'lagarta'
  
  else:
    if c =='hematofago':
      animal = 'sanguessuga'
    else: 
      animal = 'minhoca'

print(animal)
      