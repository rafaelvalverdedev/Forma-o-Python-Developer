''''
#Desafio
Um supermercado está fazendo uma promoção de venda de refrigerantes. Se um dia você comprar refrigerantes e levar 
os cascos vazios no dia seguinte, ela troca cada conjunto de K garrafas vazias  por uma garrafa cheia. Um cliente 
quer aproveitar ao máximo essa oferta e por isso comprou várias garrafas no primeiro dia da promoção. Agora ele quer 
saber quantas garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo.

Faça um programa para calcular isso

#Entrada
A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000) , que indica o número de casos de teste. Em cada uma das 
T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000),  respectivamente o número de refrigerantes comprados e o
 número de garrafas vazias para ganhar uma cheia.

# Saída
Para cada caso de teste imprima o número de garrafas que o cliente terá no segundo dia, se aproveitar ao máximo a oferta.
'''

'''
Exemplo de Entrada	Exemplo de Saída
    3       |   4
    7 4     |   4
    4 7     |   4
    4000 7  |   4
'''

# Função para calcular o número de garrafas ao final do segundo dia
def calcular_garrafas_segundo_dia(N, K):
    garrafas_totais = N  # Inicialmente, o cliente tem N garrafas compradas
    garrafas_vazias = N  # Inicialmente, todas as garrafas compradas estão vazias

    # Enquanto for possível trocar K garrafas vazias por uma cheia
    if garrafas_vazias >= K:
      garrafas_vazias = N // K
      garrafas_cheias = N % K
      garrafas_totais = garrafas_vazias + garrafas_cheias
    else:
      garrafas_totais = N
    return garrafas_totais

# Número de casos de teste
T = int(input())

# Loop sobre cada caso de teste
for _ in range(T):
    # Entrada para cada caso de teste: N (número de refrigerantes comprados) e K (número de garrafas vazias para ganhar uma cheia)
    N, K = map(int, input().split())
    # Chamando a função para calcular o número de garrafas ao final do segundo dia
    resultado = calcular_garrafas_segundo_dia(N, K)
    # Imprimindo o resultado para este caso de teste
    print(resultado)