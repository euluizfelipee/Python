"""Crie uma função que retorne a subtração de dois elementos, mas que considere o valor absoluto deste valores."""
def func(n1, n2):
    sub = abs(n1 - n2)
    return sub
n1 = 85
n2 = -9
resultado = func(n1,n2)
print(resultado)
