"""Percorra os números de 2 até 10 e diga se o número é par ou impar."""
for i in range(2, 11):
    if i % 2 == 0:
        print(f"{i} é Par")
    else:
        print(f"{i} é Ímpar")
