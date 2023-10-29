"""Crie uma função chamada “e_negativo” que receba um número, retorna um booleano “True” se o número for negativo, caso contrário retorna “False”."""
def e_negativo(x):
    if x < 0:
        return True
    else:
        return False
num = int(input("Digite um numero: "))
result = e_negativo(num)
print(result)
