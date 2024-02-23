C = int(input()) 
mensagem = ''

for i in range(C): 
    N = int(input())
    if N <= 8000:
        mensagem += 'Inseto! \n'
    else:
        mensagem += 'Mais de 8000! \n'

print(mensagem)
