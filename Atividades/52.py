"""Crie um função que receba um array de números (int ou float) e retorne sua soma."""
def somaarr(arr):
    soma = 0
    for i in arr:
        soma += i
    return soma

numeros = [float(x) for x in input("Digite uma lista de números separados por espaço: ").split()]
resultado = somaarr(numeros)
print("A soma dos números é:", resultado)
