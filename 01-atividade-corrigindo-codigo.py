""""
Você está fazendo parte de uma equipe de desenvolvimento e precisa corrigir um código que um de seus colegas não concluiu. O objetivo é criar um algoritmo que leia 5 números inteiros e, em seguida, mostre na tela:

A quantidade de números pares e ímpares.
A quantidade de números positivos e negativos.
A quantidade de números inseridos.
O maior e o menor número.
A média de números pares.
A média de números ímpares.
A média de todos os números inseridos.
Mostrar os números lidos na ordem inversa.

"""
# Inicialização das variáveis

import os
os.system("cls || clear")

numeros = []
pares = []
ímpares = []
positivos = 0
negativos = 0
soma_pares = 0
soma_ímpares = 0
soma_total = 0


for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
    
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    
    
    if numero % 2 == 0:
        pares.append(numero)
        soma_pares += numero
    else:
        ímpares.append(numero)
        soma_ímpares += numero
    
    
    soma_total += numero

media_pares = soma_pares / len(pares) if pares else 0
media_ímpares = soma_ímpares / len(ímpares) if ímpares else 0
media_total = soma_total / len(numeros) if numeros else 0

# Encontrar o maior e o menor número
maior_numero = max(numeros)
menor_numero = min(numeros)

# Mostrar os resultados
print("\nResultados:")
print(f"Quantidade de números pares: {len(pares)}")
print(f"Quantidade de números ímpares: {len(ímpares)}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade total de números inseridos: {len(numeros)}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_ímpares:.2f}")
print(f"Média de todos os números inseridos: {media_total:.2f}")

# Mostrar os números na ordem inversa
print("Números lidos na ordem inversa:")
for numero in reversed(numeros):
    print(numero)
