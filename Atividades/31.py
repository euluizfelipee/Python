"""Crie um programa que receba 5 números e retorne a média aritmética entre esses números."""
chave = 0

for j in range(5):
    h = int(input("Digite um número: "))
    if h >= 0:
        chave += h
media = chave / 5
print(media)