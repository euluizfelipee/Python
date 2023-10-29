"""Cria um programa que printe a tabuada da divisão de um número lido por input."""

str = float(input("Digite o s string: "))

for i in range(1,11):
    div = str / i
    print("%.0f / %d = %.2f" % (str, i, div))
