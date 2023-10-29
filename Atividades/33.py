"""Cria um programa que receba um número arbitrário (definido pelo usuário) de números que serão lidos e retorne a soma de todos eles."""
i = int(input("Digite a quantidade de numeros a ser lido:"))
chave = 0
for j in range(i):
    h = int(input("Digite um número: "))
    chave += h
print(chave)