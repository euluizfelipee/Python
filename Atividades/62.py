"""Sem usar “ifs”, crie uma função que receba dois números e retorne a soma dos mesmos, mas o valor retornado não pode passar de 10000 e deve ser 
        sempre maior que 0. """
def func(n1, n2):
    soma = n1 + n2
    resultado = min(max(soma, 1), 10000)
    return resultado

n1 = 85
n2 = -9
resultado = func(n1, n2)
print(resultado)
